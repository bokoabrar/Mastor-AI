import streamlit as st
from mistralai import Mistral

# 1. Mistral API Key (Apnar key-ti ekhane thik vabe boseyechi)
MISTRAL_API_KEY = "Ag_019cac33e1d977f3acd14a6650c89d9b"
client = Mistral(api_key=MISTRAL_API_KEY)

# 2. Gemini/ChatGPT Style Full UI Config
st.set_page_config(page_title="Mastor AI", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
    /* Dark Mode Theme - Huhu amar moto */
    .stApp {
        background-color: #131314;
    }
    
    /* Title Style */
    .glow-text {
        font-size: 38px;
        color: #E3E3E3;
        text-align: center;
        font-weight: 600;
        margin-top: 20px;
        letter-spacing: -0.5px;
    }

    /* Chat Messages - Modern Bubble Look */
    .stChatMessage {
        background-color: transparent !important;
        border-radius: 0px !important;
        padding: 20px 0px !important;
        margin-bottom: 5px !important;
        border-bottom: 1px solid #282829 !important;
    }

    /* AI Assistant Profile Icon Style */
    .stChatMessage[data-testimonial="assistant"] {
        background-color: #1E1F20 !important;
        border-radius: 12px !important;
        padding: 15px !important;
        border: none !important;
    }

    /* Text Clarity (Fix for 2973.png) - Ekdom Sada ebong Sposto */
    .stMarkdown p, .stChatMessage p {
        color: #E3E3E3 !important;
        font-size: 17px !important;
        font-family: 'Inter', sans-serif !important;
        line-height: 1.7 !important;
    }

    /* Input Box Styling */
    .stChatInputContainer {
        border-top: 1px solid #333 !important;
        background-color: #131314 !important;
    }

    /* Appgeyser Advertisement ba Header Hide kora */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# UI Branding
st.markdown('<div class="glow-text">Mastor AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8E918F; font-size: 15px;'>How can I help you today?</p>", unsafe_allow_html=True)

# 3. Persistent Chat Memory (Memory Fix)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Screen-e purano chatti dekhano (History Visibility)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. User Interaction & AI Logic
if prompt := st.chat_input("Enter a prompt here..."):
    # User message update
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response (Mistral Large 3 - Best for Reasoning)
    with st.chat_message("assistant"):
        try:
            # Mistral Large model call
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=[
                    {"role": "system", "content": "Tumi Mastor AI. Gemini-r moto intelligent, clean and professional Banglay uttor dabe. Bullet point use korbe."},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ],
            )
            full_res = response.choices[0].message.content
            st.markdown(full_res)
            # Memory-te save kora jate poreo mone thake
            st.session_state.messages.append({"role": "assistant", "content": full_res})
        except Exception as e:
            st.error("Error: Apnar Mistral API key-te shomoshya thakte pare.")
