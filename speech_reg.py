import streamlit as st
import speech_recognition as sr

# Set up Streamlit app
st.title("Speech Recognition App")

st.markdown("<h1 style = 'color: #FFACAC'>VOICE REECOGNITION APP</h1> ", unsafe_allow_html = True)
st.markdown("<h6 style = 'top_margin: 0rem; color: #F2921D'>Built by GoMyCode Pumpkin Reedemers</h6>", unsafe_allow_html = True)

# Add an image to the page
st.image('pngwing.com (1).png', caption = 'VOICE OF REDEEMERS, width = 400)

# Create a line and a space underneath
st.markdown('<hr><hr><br>', unsafe_allow_html= True)



# Record audio from user
def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please start speaking...")
        try:
            audio = r.listen(source)
            return audio
        except sr.RequestError:
            st.write("Sorry, there was an error accessing the microphone.")
        except sr.UnknownValueError:
            st.write("Sorry, couldn't record audio.")

# Recognize speech from audio
def recognize_speech(audio):
    r = sr.Recognizer()
    try:
        st.write("Recognizing...")
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, couldn't recognize speech.")
    except sr.RequestError:
        st.write("Sorry, there was an error processing the request.")

# Main Streamlit app logic
def main():
    # Record audio
    audio = record_audio()

    # Recognize speech
    if st.button("Recognize Speech"):
        if audio:
            text = recognize_speech(audio)
            if text:
                st.success("Speech recognized: {}".format(text))

if __name__ == "__main__":
    main()
