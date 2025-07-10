import streamlit as st
from loader import load_pdf_text
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# LLM setup
model = OllamaLLM(model="llama3")

# Prompt template
prompt_template = """
You are a helpful assistant reading a PDF document.

PDF Content:
{context}

User Question:
{question}

Answer:"""

prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | model

# Streamlit UI
st.set_page_config(page_title="📄 PDF Chatbot (Local)", layout="centered")
st.title("📄 PDF Chatbot (Local LLaMA 3)")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    pdf_text = load_pdf_text(uploaded_file)
    st.success("PDF Loaded Successfully!")

    question = st.text_input("Ask a question about the PDF:")

    if question:
        with st.spinner("Thinking..."):
            response = chain.invoke({
                "context": pdf_text[:15000],  # limit long inputs
                "question": question
            })
            st.markdown("**🧠 Answer:**")
            st.write(response)
