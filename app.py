
import streamlit as st
import uuid
import pandas as pd
import json
import chromadb
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

# Configure Gemini API
genai.configure(api_key="AIzaSyAG1o_3LIFtEpsmHrxqBF5p0arw3o8RsT4")  # <-- Replace with your real Gemini API Key

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key="AIzaSyAG1o_3LIFtEpsmHrxqBF5p0arw3o8RsT4",
    temperature=0.2
)

# Load your data
jobs_df = pd.read_csv('./data/job_listing_data.csv')

with open('./data/session_details.json', 'r') as f:
    sessions_data = json.load(f)

with open('./data/faqs.json', 'r') as f:
    faqs_data = json.load(f)

# Create knowledge text chunks
text_data = []

# Add jobs
for idx, row in jobs_df.iterrows():
    text_data.append(f"Job ID: {row['job_id']}
Job Title: {row['job_title']}
Description: {row['job_description']}")

# Add sessions
for session in sessions_data:
    text_data.append(f"Session Title: {session['title']}
Session ID: {session['session_id']}
Description: {session['description']}")

# Add FAQs
for faq in faqs_data:
    text_data.append(f"FAQ Question: {faq['question']}
FAQ Answer: {faq['answer']}")

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.create_documents(text_data)

# Create vectorstore
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectordb = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory='./chroma_db'
)

retriever = vectordb.as_retriever()

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# Bias Detection
def detect_bias(user_query):
    bias_keywords = ["women can't", "female leadership bad", "only men can", "men are better", "are women weak"]
    if any(keyword in user_query.lower() for keyword in bias_keywords):
        return True
    return False

def handle_bias(user_query):
    return "🌟 Women have consistently demonstrated excellence in leadership, innovation, and collaboration across all industries!"

# Session Context Storage
session_context = {}

def get_session_id():
    return str(uuid.uuid4())

def asha_bot(user_query, session_id=None):
    if not session_id:
        session_id = get_session_id()

    if detect_bias(user_query):
        bot_response = handle_bias(user_query)
    else:
        bot_response = qa_chain.run(user_query)

    if session_id not in session_context:
        session_context[session_id] = []
    session_context[session_id].append({"user": user_query, "bot": bot_response})

    return bot_response, session_id

# ========== Streamlit Frontend ==========

st.set_page_config(page_title="🌟 Asha - Women's Career Assistant", page_icon="✨")

st.title("🌟 Asha Bot - Empowering Women's Careers")

st.write("Welcome! Ask me about job opportunities, mentorship sessions, career events, FAQs, and more.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("How can I assist you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    bot_response, session_id = asha_bot(prompt)

    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
