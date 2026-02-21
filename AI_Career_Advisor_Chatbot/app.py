import streamlit as st
from services.gemini_service import GeminiService
from services.prompt_manager import (
    career_guidance_prompt,
    resume_analysis_prompt,
    image_resume_prompt
)
from services.memory_manager import (
    init_memory,
    add_message,
    get_history
)
from services.resume_parser import extract_text_from_pdf
from services.image_analyzer import read_image
from utils.logger import get_logger

# -------------------------------
# Initialize Logger
# -------------------------------
logger = get_logger()
logger.info("Application started")
for handler in logger.handlers:
    handler.flush()

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="AI Career Advisor",
    layout="wide"
)

st.title("🤖 AI Career Advisor Chatbot")

# -------------------------------
# Initialize Memory & Gemini
# -------------------------------
init_memory()
gemini = GeminiService()

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("📂 Upload Resume")

pdf_file = st.sidebar.file_uploader(
    "Upload PDF Resume",
    type=["pdf"]
)

image_file = st.sidebar.file_uploader(
    "Upload Resume Image",
    type=["png", "jpg", "jpeg"]
)

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.chat_history = []
    logger.info("Chat history cleared")
    for handler in logger.handlers:
        handler.flush()
    st.success("Chat cleared successfully")

# -------------------------------
# Display Chat History
# -------------------------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["parts"][0])

# -------------------------------
# Chat Input
# -------------------------------
user_input = st.chat_input("Ask career-related questions...")

if user_input:
    add_message("user", user_input)

    logger.info(f"User input received: {user_input}")
    for handler in logger.handlers:
        handler.flush()

    with st.chat_message("assistant"):
        with st.spinner("Analyzing..."):

            prompt = career_guidance_prompt(user_input)

            response = gemini.generate_text_response(
                prompt,
                history=get_history()
            )

            st.markdown(response)

            add_message("model", response)

            logger.info("Text response generated successfully")
            for handler in logger.handlers:
                handler.flush()

# -------------------------------
# PDF Resume Analysis
# -------------------------------
if pdf_file:
    st.subheader("📄 Resume Analysis")

    logger.info("PDF uploaded for analysis")
    for handler in logger.handlers:
        handler.flush()

    with st.spinner("Extracting text from PDF..."):
        resume_text = extract_text_from_pdf(pdf_file)

    prompt = resume_analysis_prompt(resume_text)

    with st.spinner("Analyzing Resume..."):
        response = gemini.generate_text_response(prompt)

        st.markdown(response)

        logger.info("PDF resume analyzed successfully")
        for handler in logger.handlers:
            handler.flush()

# -------------------------------
# Image Resume Analysis
# -------------------------------
if image_file:
    st.subheader("🖼 Resume Image Analysis")

    logger.info("Image uploaded for analysis")
    for handler in logger.handlers:
        handler.flush()

    image_bytes = read_image(image_file)
    prompt = image_resume_prompt()

    with st.spinner("Analyzing Image..."):
        response = gemini.generate_multimodal_response(
            prompt,
            image_bytes,
            mime_type=image_file.type
        )

        st.markdown(response)

        logger.info("Image analyzed successfully")
        for handler in logger.handlers:
            handler.flush()
