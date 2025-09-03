import streamlit as st
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="💡", layout="centered")

st.title("💡 Random Quote Generator")

# List of sample quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Dream big and dare to fail. – Norman Vaughan",
    "Happiness is not something readymade. It comes from your own actions. – Dalai Lama",
    "Do what you can with all you have, wherever you are. – Theodore Roosevelt",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. – William James",
]

# Button to generate random quote
if st.button("✨ Generate Quote"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button above to get a motivational quote!")

