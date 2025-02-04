import streamlit as st
import pyttsx3  # For text-to-speech
import os
import time
from threading import Thread
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Set up Streamlit UI
st.set_page_config(page_title="AI Storytelling Universe", layout="wide")
st.title("🎭 Interactive AI-Driven Storytelling Universe")
st.sidebar.title("Features")

# Session Management
if "store" not in st.session_state:
    st.session_state.store = {}

session_id = st.sidebar.text_input("Enter Session ID", "default_session")

# Input for the Groq API Key
api_key = st.text_input("Enter your Groq API Key:", type="password")
if api_key:
    llm = ChatGroq(groq_api_key=api_key, model_name="Gemma2-9b-It")
else:
    st.warning("Please enter the Groq API Key.")

# Manage session history
def get_session_history(session: str) -> ChatMessageHistory:
    if session not in st.session_state.store:
        st.session_state.store[session] = ChatMessageHistory()
    return st.session_state.store[session]

session_history = get_session_history(session_id)

def create_rag_chain():
    system_prompt = (
        "You are an AI storyteller. Use context to generate engaging lore, plot twists, or character arcs."
        "If no context exists, create something innovative. Keep it compelling and immersive."
        "\n\n{context}"
    )
    qa_prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ])
    return create_stuff_documents_chain(llm, qa_prompt)

# Sidebar Feature Selection
feature = st.sidebar.selectbox("Select Feature", [
    "Generate Story Lore", "Suggest Plot Twists", "Character Development", "Generate Full Storyline"])

# UI for Different Features
if feature == "Generate Story Lore":
    st.header("📜 Generate Story Lore")
    user_input = st.text_input("Enter your story idea:")
    if user_input and st.button("Generate Lore"):
        response = create_rag_chain().invoke({"input": f"Generate lore for: {user_input}", "context": "", "chat_history": session_history.messages})
        st.write("**Generated Lore:**", response)
        session_history.add_message({"role": "ai", "content": response})

elif feature == "Suggest Plot Twists":
    st.header("🎭 Suggest Plot Twists")
    story_input = st.text_area("Enter your story so far:")
    if story_input and st.button("Generate Plot Twist"):
        response = create_rag_chain().invoke({"input": f"Suggest a plot twist for: {story_input}", "context": "", "chat_history": session_history.messages})
        st.write("**Plot Twist:**", response)
        session_history.add_message({"role": "ai", "content": response})

elif feature == "Character Development":
    st.header("🧑‍🎭 Character Development")
    character_input = st.text_input("Describe your character:")
    if character_input and st.button("Generate Character Details"):
        response = create_rag_chain().invoke({"input": f"Develop this character: {character_input}", "context": "", "chat_history": session_history.messages})
        st.write("**Character Development:**", response)
        session_history.add_message({"role": "ai", "content": response})

elif feature == "Generate Full Storyline":
    st.header("📖 Generate Full Storyline")
    lore_input = st.text_area("Paste the Lore here:")
    plot_twist_input = st.text_area("Paste the Plot Twists here:")
    character_dev_input = st.text_area("Paste the Character Development here:")

    if st.button("Generate Full Story") and 'generated_story' not in st.session_state:
        full_story_input = f"Lore: {lore_input}\nPlot Twists: {plot_twist_input}\nCharacters: {character_dev_input}\nCreate a complete story."
        response = create_rag_chain().invoke({"input": full_story_input, "context": "", "chat_history": session_history.messages})
        st.session_state.generated_story = response
        st.write("### Generated Full Story:")
        st.write(response)

    # Save Story Option
    if "generated_story" in st.session_state and st.button("💾 Download Story"):
        file_path = "/tmp/generated_story.txt"  # Save to a temporary location
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(st.session_state.generated_story)

        # Provide download button
        st.download_button(
            label="Download Story as TXT",
            data=open(file_path, "rb").read(),
            file_name="generated_story.txt",
            mime="text/plain"
        )


# Display Chat History
st.sidebar.subheader("Session Chat History")
st.sidebar.write(session_history.messages)



# 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
