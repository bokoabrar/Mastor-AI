import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Mastor AI", page_icon="🎓")

# API Setup
genai.configure(api_key="AIzaSyAMr6ggmKoZLmqQ47WIaUiOEYW_PunYCQE")

# UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    .stChatMessage { border-radius: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Mastor AI")
st.caption("Honors, Diploma & Nursing Admission Expert")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Tumi Mastor AI expert. Banglay uttor dao: {prompt}")
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
