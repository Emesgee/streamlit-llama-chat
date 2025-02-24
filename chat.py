# streamlit_llama_query_app_danish.py
import streamlit as st
import os
from dotenv import load_dotenv
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
from openai import OpenAI

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("OPENAI_API_KEY mangler fra miljøvariablerne.")
    st.stop()
os.environ['OPENAI_API_KEY'] = api_key

# OpenAI client initialization
client = OpenAI(api_key=api_key)

# Constants
DATA_DIR = "data"
PERSIST_DIR = "./storage"

# Function to load or create the index
@st.cache_resource
def get_or_create_index():
    if not os.path.exists(DATA_DIR):
        st.error(f"Datamappe '{DATA_DIR}' findes ikke.")
        st.stop()

    if not os.path.exists(PERSIST_DIR):
        documents = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index

# Translate text to Danish
def translate_to_danish(text):
    prompt = f"Translate the following English text to Danish:\n\n{text}\n\nDanish translation:"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Koncern-IT")
st.markdown("### Hejsa! Hvordan kan jeg hjælpe dig? ###")

# Initialize index
index = get_or_create_index()
query_engine = index.as_query_engine()

# User input
query = st.text_input("Skriv din forspørgsel:")

# Query handling
if query:
    with st.spinner('Søger i indekset...'):
        response = query_engine.query(query)
        translated_response = translate_to_danish(response.response)

    st.markdown("**Svar:**")
    st.write(translated_response)
