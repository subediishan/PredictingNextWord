import pickle as pkl
import numpy as np 
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

#Load the model 
model =  load_model('model.h5')


with open('tokenizer.pkl','rb') as file:
  tokenizer = pkl.load(file)

def predict_next_word(tokenizer,text,max_sequence_len,model):
  text_sequences = tokenizer.texts_to_sequences([text])[0]
  if(len(text_sequences)>=max_sequence_len):
    text_sequences = text_sequences[-(max_sequence_len-1):]
  text_sequences= pad_sequences([text_sequences],maxlen = max_sequence_len, padding = 'pre')
  predicted = model.predict(text_sequences,verbose = 0)
  predicted_word = np.argmax(predicted, axis= 1)[0]
  for words, index in tokenizer.word_index.items():
    if predicted_word == index:
      return words
  return None
  
  
st.title('Next word Prediction')
text = st.text_input("Hey enter any text")
if st.button('predict next word'):
  max_sequence_len = model.input_shape[1]
  st.text(predict_next_word(tokenizer,text,max_sequence_len,model))