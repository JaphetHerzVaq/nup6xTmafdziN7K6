# MonReader Project

## Overview

**MonReader** is an innovative solution designed to enhance document digitization through artificial intelligence and computer vision. The system offers an accessible and automated document scanning experience, benefiting the visually impaired, researchers, and others requiring efficient bulk scanning. It includes:

- **Automatic Page Flip Detection:** Using video input, MonReader identifies and processes page flips.
- **Document Cropping and Dewarping:** Detects document edges and adjusts them for a bird's-eye view.
- **Text Recognition and Correction:** Extracts text while maintaining formatting, enhanced by machine learning.

## Features

1. **AI-Powered Page Flip Detection:** Uses image-based analysis to determine flipping actions.
2. **High-Resolution Processing:** Captures and sharpens document text for clarity.
3. **Multi-Device Compatibility:** Integrates with smart devices seamlessly.

## Project Goals

- Predict whether a page flip is occurring using single-image inputs.
- Achieve high model performance with F1-score as the primary evaluation metric.

---

## Contents of the Repository

### 1. Data Preparation

- **Data Structure:** 
  - Training and testing datasets are structured into "flip" and "notflip" classes.
  - Images are labeled using a consistent naming convention for easy retrieval.

- **Preprocessing:**
  - Images are resized to 224x224 pixels.
  - Pixel values are normalized and standardized.
  - Data augmentation techniques (random rotations, flips, color adjustments) are employed.

### 2. Model Building

- **Frameworks Used:**
  - PyTorch and TensorFlow for deep learning model implementation.
  - Pre-trained models like ResNet, EfficientNet, and MobileNet are utilized and fine-tuned.

- **Customizations:**
  - Custom datasets and DataLoaders manage data efficiently.
  - Early stopping mechanism ensures optimal model performance without overfitting.

### 3. Exploratory Data Analysis (EDA)

- **Includes:**
  - Image quality checks.
  - Class distribution analysis.
  - Dimensional and color spectrum evaluations.

### 4. Training Pipeline

- **Data Splitting:**
  - Training, validation, and testing datasets are created with an 80-10-10 split.
  
- **Metrics Tracked:**
  - Loss, accuracy, and F1-score for training and validation.

- **Visualization:**
  - Training metrics are plotted for insights into model convergence and validation performance.

### 5. Optical Character Recognition (OCR)

- **Technologies:**
  - Tesseract OCR and PaddleOCR for extracting text from images.
- **Post-processing:**
  - Text is formatted and corrected using machine learning redaction tools.

### 6. Outputs and Visualizations

- Predictions are visualized with true vs. predicted labels.
- Extracted text from processed documents is displayed for validation.

---

## Requirements

### Python Libraries

```bash
pip install numpy pandas matplotlib torch tensorflow opencv-python Pillow pytesseract paddleocr
```

### Setup Instructions

1. Install the required libraries using the command above.
2. Prepare the dataset by organizing the images into appropriate folders.
3. Run the training script to fine-tune the model.
4. Use the evaluation script to assess performance and visualize results.

---

## Usage

1. **Train the Model:** Execute the training pipeline with preprocessed datasets.
2. **OCR Processing:** Use the provided scripts to extract text from documents.
3. **Visualization:** Analyze model performance and visualize predictions.

## Implementation with DockerHub in AWS EC2
1. **Flask code**
2. **Configuration in AWS EC2**
3. **Walkthrough video**
---

## Contact

**Author:** Japhet Hernández-Vaquero  
**Company:** Apziva  
For inquiries, please reach out to [japhet.hernandezv@gmail.com / linkedin.com/in/japhethernandezv].
