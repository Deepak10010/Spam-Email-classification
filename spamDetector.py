import pickle
import streamlit as st
from win32com.client import Dispatch



def speak(text):
    speak=Dispatch(("SAPI.SpVoice"))
    speak.Speak(text)
    
    
#Loading our model
model=pickle.load(open("spam.pkl", "rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))


def main():
    st.title("Email Spam classification application")
    st.subheader("Build with Streamlit and Python")
    msg=st.text_input("Enter a text: ")
    if st.button("Predict"):
        data=[msg]
        vect=cv.transform(data).toarray()
        prediction = model.predict(vect)
        result=prediction[0]
        if result==1:
            st.error("This is a Spam email")
            speak("This is a Spam email")
        else:
            st.success("This is not a Spam email")
            speak("This is not a Spam email")
            
            
main()    