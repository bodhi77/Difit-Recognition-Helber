import tkinter as tk
import cv2
import numpy as np
import time
from PIL import ImageTk, Image
from tensorflow.keras.models import load_model

# set up timer
last_frame_time = time.time()
frame_interval = 1/30 # 30 fps

# set up main canvas
root = tk.Tk()
root.title("Main Canvas")

# create main canvas
canvas_width = 1920
canvas_height = 720
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# create sub-canvases for each captured video
sub_canvas_width = 800
sub_canvas_height = 600
sub_canvas_margin = 20
sub_canvas_row = 0
sub_canvas_col = 0

cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
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
    frame_copy = frame.copy()

    bbox_size = (60, 60)
    bbox = [(int(WIDTH // 2 - bbox_size[0] // 2), int(HEIGHT // 2 - bbox_size[1] // 2)),
            (int(WIDTH // 2 + bbox_size[0] // 2), int(HEIGHT // 2 + bbox_size[1] // 2))]

    img_cropped = frame[bbox[0][1]:bbox[1][1], bbox[0][0]:bbox[1][0]]
    img_gray = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.resize(img_gray, (200, 200))
    result, probability = prediction(img_gray, model)

    # convert image to tkinter format
    img_tk = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(frame_copy, cv2.COLOR_BGR2RGB)))
    # create sub-canvas
    sub_canvas = tk.Canvas(canvas, width=sub_canvas_width, height=sub_canvas_height, bg='white')
    # add sub-canvas to main canvas
    canvas.create_window(canvas_width//2, canvas_height//2, window=sub_canvas)

    # add image to sub-canvas
    sub_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

     # draw bounding box on sub-canvas
    sub_canvas.create_rectangle(bbox[0][0], bbox[0][1], bbox[1][0], bbox[1][1], outline='red')


    sub_canvas.create_text(sub_canvas_width // 2, sub_canvas_height - 20, text=f"Prediction: {result}")
    sub_canvas.create_text(sub_canvas_width // 2, sub_canvas_height - 40, text=f"Probability: {probability:.2f}")

    # update sub-canvas if enough time has passed since last frame update
    current_time = time.time()
    if current_time - last_frame_time > frame_interval:
        sub_canvas.update()
        last_frame_time = current_time

    # release tkinter image reference to avoid memory leak
    sub_canvas.img_tk = None

    if cv2.waitKey(1) & 0xFF == 27:
        break

# release resources
cap.release()
cv2.destroyAllWindows()

# start main loop
root.mainloop()
