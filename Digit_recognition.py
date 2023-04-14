import cv2
import numpy as np
from tensorflow.keras.models import load_model

camera_source = 0

cap = cv2.VideoCapture(camera_source + cv2.CAP_DSHOW)
WIDTH = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
HEIGHT = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

model = load_model('model/digits.h5')


def prediction(image, model):
    img = cv2.resize(image, (28, 28))
    img = img / 255
    img = img.reshape(1, 28, 28, 1)
    predict = model.predict(img)
    prob = np.amax(predict)
    class_index = model.predict_classes(img)
    result = class_index[0]
    if prob < 0.75:
        result = 0
        prob = 0
    return result, prob


while True:

    _, frame = cap.read()
    # frame = cv2.rotate(frame, cv2.ROTATE_180)
    frame_copy = frame.copy()

    key = cv2.waitKey(1) & 0xFF

    bbox_size = (60, 60)
    bbox = [(int(WIDTH // 2 - bbox_size[0] // 2), int(HEIGHT // 2 - bbox_size[1] // 2)),
            (int(WIDTH // 2 + bbox_size[0] // 2), int(HEIGHT // 2 + bbox_size[1] // 2))]

    img_cropped = frame[bbox[0][1]:bbox[1][1], bbox[0][0]:bbox[1][0]]
    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.resize(img_gray, (200, 200))
    cv2.imshow("cropped", img_gray)

    result, probability = prediction(img_gray, model)
    cv2.putText(frame_copy, f"Result: {result}", (40, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 191, 0), 2, cv2.LINE_AA)
    cv2.putText(frame_copy, "Probability: " + "{:.2f}". format(probability*100) + "%", (40, 430), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 191, 0), 2, cv2.LINE_AA)

    if camera_source == 1:
        cv2.putText(frame_copy, "Web Cam", (260, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(frame_copy, "Built-in Camera", (210, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
    
    cv2.rectangle(frame_copy, bbox[0], bbox[1], (0, 255, 0), 3)

    cv2.imshow("Main", frame_copy)

    # create dictionary to store image file names and result values
    img_dict = {
        0: 'image0.jpg',
        1: 'image1.jpg',
        2: 'image2.jpg',
        3: 'image3.jpg',
        4: 'image4.jpg',
        5: 'image5.jpg',
        6: 'image6.jpg',
        7: 'image7.jpg',
        8: 'image8.jpg',
        9: 'image9.jpg'
        }
    
    # retrieve file name and print result based on input result
    if result in img_dict:
        img = cv2.imread(img_dict[result])
        cv2.imshow('image', img)
        print(result)
    
    # else:
    #     print("0")

    if key == ord('1'):  # switch to webcam
        camera_source = 1
        cap.release()
        cap = cv2.VideoCapture(camera_source + cv2.CAP_DSHOW)
       
    elif key == ord('0'):  # switch to laptop camera
        camera_source = 0
        cap.release() 
        cap = cv2.VideoCapture(camera_source + cv2.CAP_DSHOW)
        
    elif key == 27:  # press Esc key to exit
        break

cv2.destroyAllWindows()