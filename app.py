import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

st.title("Sentimental Analysis Using Lexicon Based Approach...")
st.header("Please use proper spelling!")

iput = st.text_input("Enter Text:")
oput_dict =  analyzer.polarity_scores(iput)

if st.button('Analyze'):
  if oput_dict['compound'] >= 0.05:
    st.write(' *Positive* :smile:')
  elif oput_dict['compound'] <= -0.05:
    st.write('*Negative* :angry:')
  else:
    st.write('*Neutral* :unamused:')
 
