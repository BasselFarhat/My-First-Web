import streamlit as st

st.title("Bassel's Official Website")

# أي شيء تكتبه هنا سيظهر لكل الناس فوراً بعد رفع الملف
my_news = [
    "Welcome to my personal blog!",
    "I'm currently studying AI at University of Jeddah.",
    "Updates on my 2008 Pajero facelift coming soon!"
]

for news in my_news:
    st.info(news)