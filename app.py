import streamlit as st
from groq import Groq

# 1. Groq API Configuration
# Ekhane apnar gsk_... key-ti boshan
GROQ_API_KEY = "APNAR_GROQ_API_KEY"
client = Groq(api_key=GROQ_API_KEY)

# 2. Page Setup & Modern UI Design (Gemini Style)
st.set_page_config(page_title="Mastor AI", page_icon="🎓", layout="centered")

# Custom CSS for Dark Mode & Clean Chat
st.markdown("""
    <style>
    /* Main Background: Pure Deep Black */
    .stApp {
        background-color: #000000;
    }
    
    /* Mastor AI Glowing Title */
    .glow-header {
        font-size: 40px;
        color: #FFFFFF;
        text-align: center;
        font-weight: 600;
        text-shadow: 0 0 12px #00FFA2;
        padding: 30px 0px 10px 0px;
        letter-spacing: 1px;
    }

    /* Chat Messages: Professional Look */
    .stChatMessage {
        background-color: #111111 !important;
        border-radius: 12px !important;
        border: 1px solid #222 !important;
        margin-bottom: 8px !important;
    }

    /* Text: Soft White (Easy to Read) */
    .stMarkdown p {
        color: #D1D1D1 !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }

    /* Hide unnecessary elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Input Box styling */
    .stChatInputContainer {
        border-top: 1px solid #333 !important;
        padding-top: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# UI Title
st.markdown('<div class="glow-header">Mastor AI</div>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>আপনার স্মার্ট এআই সহযোগী</p>", unsafe_allow_html=True)

# 3. Memory & Chat History System
# 'messages' session state-e thakar karone tab refresh na kora porjonto memory thakbe
if "messages" not in st.session_state:
    st.session_state.messages = []

# Screen-e ager sob kotha (History) dekhano
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Chat Logic with Memory
if prompt := st.chat_input("Amake jekono kichu jiggesh korun..."):
    # User message save and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response generation
    with st.chat_message("assistant"):
        try:
            # Full history AI-er kache pathano hoy jate se purano kotha mone rakhte pare
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "Tumi Mastor AI. Ekdam professional ebong friendly Banglay uttor dabe. Purano context mone rekhe kotha bolbe."},
                    *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                ],
            )
            full_response = chat_completion.choices[0].message.content
            st.markdown(full_response)
            
            # AI response save kora (Memory)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Error: {str(e)}")
