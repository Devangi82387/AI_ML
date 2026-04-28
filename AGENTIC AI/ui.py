import streamlit as st
from youtube_analyzer import build_youtube_agent

st.set_page_config(
    page_title="YouTube Analyzer",
    layout="centered",

)

st.title("AI YouTube video Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

video_url = st.text_input("Enter YouTube video URL")
button = st.button("Analyze Video")

if button and video_url:
    with st.spinner("Analyzing video..."):
        response = agent.run(
            f"Analyze this video: {video_url}"
        )

    st.markdown(response.content)