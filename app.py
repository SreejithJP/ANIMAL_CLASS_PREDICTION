from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = load_model("D:\\Downloads\\archive 3\\Training Data\\TUNED_model.keras")

# Define the class names
class_names = [
    "Beetle", "Butterfly", "Cat", "Cow", "Dog", "Elephant", 
    "Gorilla", "Hippo", "Lizard", "Monkey", "Mouse", "Panda", 
    "Spider", "Tiger", "Zebra"
]

# Define a function to preprocess the image
def preprocess_image(img_path):
    img = image.load_img(img_path, target_size=((224, 224)))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Rescale to [0, 1]
    return img

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Check if the user uploaded a file
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        if file:
            # Save the file to a temporary directory
            filepath = os.path.join("uploads", file.filename)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            file.save(filepath)
            
            # Preprocess the image and make a prediction
            img = preprocess_image(filepath)
            prediction = model.predict(img)
            os.remove(filepath)  # Clean up
            
            # Get the class with the highest predicted probability
            predicted_class = class_names[np.argmax(prediction)]
            
            return render_template("result.html", prediction=predicted_class)
    return render_template("index.html")

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
