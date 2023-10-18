import streamlit as st
import openai
import os  

# Set up OpenAI API credentials
openai.api_type = "azure"
openai.api_base = ""
openai.api_version = "2023-03-15-preview"
openai.api_key = ""

# Define Streamlit app layout
st.title("Code Explainer")
language = st.selectbox("Select Language", ["Python", "JavaScript"])
code_input = st.text_area("Enter code to explain")



# Define function to explain code using OpenAI Codex
def explain_code(input_code, language):

    model_engine = "gpt-35-turbo-16k" # Change to the desired OpenAI model
    prompt = f"Explain the following {language} code: \n\n{input_code}"
    with st.spinner("In Progress"):
        response = openai.ChatCompletion.create(
            engine=model_engine,
            messages = [
                {"role": "system", "content":"you are a helpful code assistant"},
                {"role":"user", "content": prompt}
            ],
            max_tokens = tokens,
            temperature = temperature
        )
        return response.choices[0].message.content

# Temperature and token slider
temperature = st.sidebar.slider(
    "Temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.1
)
tokens = st.sidebar.slider(
    "Tokens",
    min_value=64,
    max_value=2048,
    value=256,
    step=64
)
# Define Streamlit app behavior
if st.button("Explain"):
    output_text = explain_code(code_input, language)
    #st.text_area("Code Explanation", output_text)
    st.success(output_text)