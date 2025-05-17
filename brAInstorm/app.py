import openai
import streamlit as st
import os
from openai import OpenAI

api_key = st.secrets["OPENROUTER_API_KEY"]

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def brainstorm_startup(idea):
    prompt = f"""
You are an AI startup brainstorming assistant.

Given the startup idea/problem statement below, generate:

1. 7 creative and brandable product names  
2. 4 catchy and compelling taglines  
3. 3 viable business model ideas  
4. 3 smart and engaging launch strategies

Startup idea/problem statement:
{idea}

Your response:
"""

    response = client.chat.completions.create(
        model="mistralai/mixtral-8x7b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=600
    )

    return response.choices[0].message.content.strip()

# ----- Streamlit UI -----
st.set_page_config(page_title="brAInstorm", page_icon="🚀", layout="centered")

st.title("🤖 brAInstorm buddy")
st.markdown("Enter your startup idea and get AI-generated product names, taglines, business models, and launch strategies.")

idea_input = st.text_area("💡 Startup Idea: ", height=200)

if st.button("🚀 Brainstorm Now"):
    if not idea_input.strip():
        st.warning("Please enter your startup idea.")
    else:
        with st.spinner("Generating ideas..."):
            try:
                output = brainstorm_startup(idea_input)
                st.success("Here’s your brainstorm!")
                st.markdown(output.replace("\n", "\n\n"))
            except Exception as e:
                st.error(f"An error occurred: {e}")
