import streamlit as st
import google.generativeai as genai

# ১. টাইটেল ও স্টাইল সেটআপ
st.set_page_config(page_title="Mastor AI", page_icon="🎓")
st.title("🎓 Mastor AI")
st.write("আপনার পড়াশোনা ও ক্যারিয়ারের বিশ্বস্ত সহযোগী")
st.divider()

# ২. এআই কনফিগারেশন (আপনার API Key এখানে)
API_KEY = "AIzaSyAMr6ggmKoZLmqQ47WIaUiOEYW_PunYCQE"
genai.configure(api_key=API_KEY)

# ৩. চ্যাট হিস্ট্রি
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ৪. ইনপুট ও এআই রেসপন্স
if prompt := st.chat_input("আপনার প্রশ্নটি এখানে লিখুন..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # সঠিক মডেল ব্যবহার নিশ্চিত করা
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(f"Tumi Mastor AI expert. Friendly Banglay point akare uttor dao: {prompt}")
            
            if response.text:
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            else:
                st.error("এআই কোনো উত্তর তৈরি করতে পারেনি।")
                
        except Exception as e:
            # এখানে এরর মেসেজটি দেখা যাবে যাতে আমরা বুঝতে পারি কেন হচ্ছে
            st.error(f"সমস্যাটি হলো: {str(e)}")
