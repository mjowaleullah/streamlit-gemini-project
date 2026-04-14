import streamlit as st
from api_calling import note_generate, audio_transcription, quiz_generate
from PIL import Image
from mdclense.parser import MarkdownParser
parser = MarkdownParser()

st.title("Note Summery & Quiz Generator", anchor=False)
st.markdown("Upload 3 images to generate Note Summery and Quiz")
st.divider()

with st.sidebar:
    images=st.file_uploader("Enter Notes Images:",
                     type=["jpeg", "jpg", "png"],
                     accept_multiple_files=True)
    pil_imgs =list()

    for i in images:
        pil_img = Image.open(i)
        pil_imgs.append(pil_img)

    if images:
        st.subheader("uploaded Images")

        if len(images)>3:
            st.error("Insert max 3 images")
        else:
            cols = st.columns(len(images))

            for i, img in enumerate(images):
                with cols[i]:
                    st.image(img)

    deficulty = st.selectbox("Select Deficulty: ",
                 options=["Easy", "Medium", "Hard"],
                 index=None,
                 placeholder="Select an Option")

    button = st.button("Click the Button & initiate AI", type="primary")


if button:
    if not images:
        st.error("Please Upload photo fristly")
    if not deficulty:
        st.error("Please select a option of Dificulty.")

    if images and deficulty:

        ## Notes
        with st.container(border=True):
            st.subheader("Your Note Here...")
            with st.spinner("Processing Your Note..."):
                gen_note = note_generate(pil_imgs)
                st.markdown(gen_note)

        st.divider()

        ## Audio Transcript
        with st.container(border=True):
            plain_text = parser.parse(gen_note)
            st.subheader("Audio Here...")
            with st.spinner("Your Audio is Processing..."):
                audio = audio_transcription(plain_text)
                st.audio(audio)

            # st.text("Api Generate Here")
        st.divider()

        ## Quiz
        with st.container(border=True):
            st.subheader(f"Quiz Level: ({deficulty})")
            with st.spinner("Making Your Quizzes..."):
                quize = quiz_generate(pil_imgs, deficulty)
                st.markdown(quize)

