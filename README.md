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
ANIMAL_CLASS_PREDICTION/
│
├── app.py # Main Flask application file for the web interface
├── requirements.txt # Python package dependencies
│
├── static/
│ ├── style.css # CSS file for styling the web application
│
├── templates/
│ ├── index.html # HTML file for the image upload page
│ ├── result.html # HTML file for displaying classification results
│
├── model/
│ ├── animal_model.h5 # Saved model weights
│
├── data/
│ ├── train/ # Training dataset directory
│ ├── validation/ # Validation dataset directory
│
├── scripts/
│ ├── data_preprocessing.py # Script for data loading and preprocessing
│ ├── model_training.py # Script for training the model
│
└── README.md # This file

