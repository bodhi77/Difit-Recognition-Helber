import tensorflow.keras.models as models

def load_tf_model(model_path):
    return models.load_model(model_path)
