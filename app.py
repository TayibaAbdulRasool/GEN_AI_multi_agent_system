import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(
    page_title="Sad AI Agent",
    page_icon="😢"
)

st.title("😢 Sad AI Agent")

model = ChatMistralAI(
    model="mistral-small-latest"
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a sad AI Agent")
    ]

# Show chat history
for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# User input
prompt = st.chat_input("Type your message...")

if prompt:

    # Add user message to history
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    response = model.invoke(
        st.session_state.messages,
        temperature=0.9,
        max_tokens=100
    )

    # Add AI response to history
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    # Display AI response
    with st.chat_message("assistant"):
        st.write(response.content)
