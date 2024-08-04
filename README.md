# Pneumonia Detection Webpage

## Overview

This project is a Pneumonia Detection Webpage developed using Python, Flask, and a Convolutional Neural Network (CNN). The app detects pneumonia from chest X-ray images and provides a user-friendly web interface for uploading images and viewing results.

## Features

- **Pneumonia Detection**: Identify and classify pneumonia from uploaded chest X-ray images.
- **Real-time Results**: Display prediction results immediately after image upload.
- **User-friendly Interface**: Simple and intuitive web interface for uploading images and viewing results.

## Technology Stack

- **Backend**: Python, Flask, Keras
- **Model**: Pre-trained CNN model
- **Frontend**: HTML, CSS

## Installation

### Prerequisites

- Python 3.8+
- Flask

### Step-by-Step Guide

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd pneumonia-detection-webpage
    ```

2. **Install Python Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Download the Pre-trained Model**:
    - Ensure the pre-trained model file (`model.hdf5`) is in the project directory.

4. **Run the Flask Application**:
    ```sh
    python app.py
    ```

## Usage

1. **Launching the App**:
    - Open your web browser and navigate to `http://localhost:5000`.

2. **Using the Interface**:
    - Upload a chest X-ray image using the file uploader.
    - View the prediction result and confidence score displayed on the interface.

## Project Structure

```plaintext
pneumonia-detection-webpage/
│
├── app.py                # Main Flask application file
├── config.py             # Configuration file
├── model.hdf5            # Pre-trained CNN model
├── requirements.txt      # List of Python dependencies
├── templates/
│   └── index.html        # HTML template for the web interface
├── static/
│   └── style.css         # CSS file for styling
├── README.md             # Project readme file
└── ...                   # Additional files and directories
```

## Model

The model used in this application is a pre-trained convolutional neural network (CNN) designed to detect pneumonia from chest X-ray images. The model classifies images as either pneumonia-positive or pneumonia-negative.

---

Feel free to reach out with any questions or feedback!

---

*Happy Coding!*
