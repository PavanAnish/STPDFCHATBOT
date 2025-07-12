# PDFCHATBOT
with stremlit 
And Ollama Llama 3

PDF Chatbot with Ollama and Streamlit
=====================================

A local AI-powered chatbot that can read and understand PDF files using an open-source LLM via Ollama. It provides a simple Streamlit web interface to upload PDFs and ask questions based on the document content.

Features
--------
- Upload and read PDFs in the browser
- Ask questions and get answers based on the PDF content
- Runs entirely locally using Ollama and open-source LLMs (e.g., LLaMA3, Mistral, etc.)
- Simple and clean UI built with Streamlit

Technologies Used
-----------------
- Python
- Streamlit
- PyPDF2 or pdfplumber (for reading PDFs)
- Ollama (local LLM runtime)
- LangChain or direct prompt pipeline (for LLM interaction)

Project Structure
-----------------
pdf_chatbot/
│
├── app.py               -> Main Streamlit app
├── pdf_utils.py         -> PDF reading and processing
├── llm_chain.py         -> Ollama model connection and response logic
├── README.txt           -> Project description
└── requirements.txt     -> Python dependencies

Setup Instructions
------------------
1. Install Python 3.8 or above.

2. Install Ollama and run a model (e.g. LLaMA3):
       https://ollama.com
       ollama run llama3

3. Clone this project:
       git clone https://github.com/YourUsername/pdf_chatbot.git
       cd pdf_chatbot

4. Install Python dependencies:
       pip install -r requirements.txt

5. Run the Streamlit app:
       streamlit run app.py

6. Use the interface to upload a PDF and start chatting!

Sample Usage
------------
- Upload a PDF (e.g., a research paper or invoice)
- Ask: "What is the main topic of this paper?"
- Ask: "List all the payment dates mentioned."

Security Note
-------------
Since Ollama runs locally, no data is sent to external servers.
Ideal for private documents and offline use.

Author
------
Created by [Your Name or GitHub Username]

License
-------
MIT License
