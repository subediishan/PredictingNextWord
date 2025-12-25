# PredictingNextWord

**PredictingNextWord** is an interactive next-word prediction application built with TensorFlow/Keras and Streamlit.  
The model used in this project was built and trained from scratch on the Shakespeare Hamlet dataset. It tokenizes input text, feeds it into an LSTM-based neural network, and predicts the most likely next word, enabling basic autocomplete functionality.

---

This project demonstrates a simple natural language processing (NLP) workflow:

1. Train and load  model (`model.h5`) and tokenizer (`tokenizer.pkl`)
2. Preprocess user input with padding and tokenization
3. Predict the next word using the model
4. Display the prediction in a Streamlit web app


## Features

- Accepts user input via a web interface  
- Uses sequence padding and tokenization  
- Predicts the next word using a trained deep learning model  
- Built with Python, Keras, and Streamlit  


## Repository Structure

PredictingNextWord
```
├── app.py  
├── model.h5
├── tokenizer.pkl
├── experiments.ipynb
├── hamlet.txt
├── requirements.txt
└── README.md
```
Requirements

``` bash

- Python 3.7+
- TensorFlow
- Streamlit
- NumPy
- Pickle


```
### Installation

Clone the repository:

```bash
git clone https://github.com/subediishan/PredictingNextWord.git 

cd PredictingNextWord

Install dependencies:

pip install -r requirements.txt

 
