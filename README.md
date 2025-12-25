# PredictingNextWord

**PredictingNextWord** is an interactive next-word prediction application built with **TensorFlow/Keras** and **Streamlit**.  
It tokenizes input text, feeds it into a trained LSTM-based model, and predicts the most likely next word enabling basic autocomplete functionality. 

---

This project demonstrates a simple natural language processing (NLP) workflow:

1. Load a pre-trained model (`model.h5`) and tokenizer (`tokenizer.pkl`)
2. Preprocess user input with padding and tokenization
3. Predict the next word using the model
4. Display the prediction in a Streamlit web app


## Features

- Accepts user input via a web interface  
- Uses sequence padding and tokenization  
- Predicts the next word using a trained deep learning model  
- Built with Python, Keras, and Streamlit  


## Repository Structure

PredictingNextWord/
├── app.py
├── model.h5
├── tokenizer.pkl
├── experiments.ipynb
├── hamlet.txt
├── requirements.txt
└── README.md




Requirements

- Python 3.7+
- TensorFlow
- Streamlit
- NumPy
- Pickle

---

### Installation

Clone the repository:

```bash
git clone https://github.com/subediishan/PredictingNextWord.git
cd PredictingNextWord
Install dependencies:

Copy code
pip install -r requirements.txt

 How It Works
1. Model and Tokenizer
The model.h5 is a pre-trained Keras model that accepts text sequences and predicts the next word based on learned patterns in training data.

The tokenizer.pkl is a fitted tokenizer that converts text into numerical sequences that the model understands.

2. Streamlit App
Run the web interface:

streamlit run app.py

Then open the displayed URL in your browser.


