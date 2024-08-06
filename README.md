# Animal Classification Using TensorFlow, VGG16, and Flask

## Project Description

This project involves developing an image classification model to classify images of animals into 15 distinct categories using TensorFlow, VGG16, and Flask. The goal is to build an efficient model and deploy it as a web application where users can upload images and receive predictions in real-time.

### Key Points

- **Model Architecture**: Utilizes the VGG16 pre-trained model for transfer learning, with additional dense layers for classification.
- **Training**: The model is trained using data augmentation techniques to improve generalization.
- **Evaluation**: Performance metrics include accuracy, precision, recall, and F1 score. The current model metrics are:
  - **Precision**: 0.844
  - **Recall**: 0.567
  - **F1 Score**: 0.590
  - **Accuracy**: 0.567
- **Web Application**: Developed using Flask to allow users to upload images and get predictions from the trained model.
- **Future Work**: Further fine-tuning and experimentation with different architectures or data augmentation techniques to improve performance.

## Folder Structure

The project directory is organized as follows:
│
├── ANIMAL_CLASS_PREDICTION/ # Folder for the Flask web application
│ ├── app.py # Main Flask application file for the web interface
│ ├── templates/
│ │ ├── index.html # HTML file for the image upload page
│ │ └── result.html # HTML file for displaying classification results
│
├── Training Data/ # Directory for training datasets
│
├── Testing Data/ # Directory for testing datasets
│
├── uploads/ # Directory for uploaded images
│
├── ANIMAL_CLASSIFICATION_CNN.ipynb # Jupyter notebook for model training and evaluation
├── animal_model.keras # Saved model weights
├── TUNED_model.keras # Tuned model weights
│
└── README.md # This file── README.md # This file

