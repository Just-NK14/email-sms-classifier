# Email/SMS Spam Classifier

This repository contains a simple Streamlit web application for classifying emails or SMS messages as spam or not spam. The model is trained using natural language processing techniques and is capable of predicting whether a given message is likely to be spam or not.

## Requirements
Make sure you have the following dependencies installed before running the application:

- `streamlit`
- `pickle`
- `nltk`

You can install them using the following command:
```bash
pip install streamlit nltk
```

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Just-NK14/email-sms-classifier.git
   cd email-sms-classifier
   ```

2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

3. Open your browser and navigate to the local host.

4. Enter the email or SMS message in the provided textarea and click the "Predict" button to see if the message is classified as spam or not.

## Functions

### Text Transformation
The `transform_text` function is responsible for preprocessing the input text. It converts the text to lowercase, tokenizes it, removes alphanumeric characters, stopwords, and punctuation, and performs stemming using the Porter Stemmer.

### Model Loading and Prediction
The trained model (`modelmnb.pkl`) and TF-IDF vectorizer (`vectorizer.pkl`) are loaded using `pickle`. The input text is preprocessed using the `transform_text` function, vectorized, and then passed through the model for prediction.

### Web App
The Streamlit web app allows users to input an email or SMS message and predicts whether it is spam or not. The result is displayed below the input, indicating whether the message is classified as spam or not.
