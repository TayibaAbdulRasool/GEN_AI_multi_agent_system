```python
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# ============================================================
# CONFIG
# ============================================================

load_dotenv()

st.set_page_config(
    page_title="Sad AI Agent",
    page_icon="😢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* -------------------- GLOBAL -------------------- */

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(45, 212, 191, 0.08), transparent 25%),
        radial-gradient(circle at 90% 90%, rgba(20, 184, 166, 0.06), transparent 25%),
        #071412;
    color: #F1F7F5;
}

/* Remove Streamlit default spacing */

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 6rem;
}

/* -------------------- HEADER -------------------- */

.main-header {
    text-align: center;
    padding: 25px 20px 15px 20px;
}

.logo {
    font-size: 55px;
    margin-bottom: 5px;
}

.title {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #F1F7F5;
    margin-bottom: 5px;
}

.subtitle {
    color: #8FA8A0;
    font-size: 15px;
}

/* -------------------- STATUS -------------------- */

.status-container {
    display: flex;
    justify-content: center;
    margin: 15px 0 25px 0;
}

.status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 7px 15px;
    border-radius: 20px;
    background: rgba(45, 212, 191, 0.08);
    border: 1px solid rgba(45, 212, 191, 0.20);
    color: #8FD9CC;
    font-size: 13px;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #2DD4BF;
    border-radius: 50%;
}

/* -------------------- CHAT AREA -------------------- */

.chat-wrapper {
    background: rgba(13, 31, 27, 0.70);
    border: 1px solid #214139;
    border-radius: 20px;
    padding: 10px;
    margin-bottom: 20px;
}

/* -------------------- CHAT MESSAGES -------------------- */

[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 15px 10px !important;
}

/* Assistant message */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) {
    background: rgba(19, 42, 36, 0.65) !important;
    border-radius: 16px !important;
    margin: 8px 0 !important;
    border: 1px solid #214139 !important;
}

/* User message */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) {
    background: rgba(45, 212, 191, 0.07) !important;
    border-radius: 16px !important;
    margin: 8px 0 !important;
    border: 1px solid rgba(45, 212, 191, 0.12) !important;
}

/* -------------------- INPUT -------------------- */

[data-testid="stChatInput"] {
    border-radius: 18px !important;
}

[data-testid="stChatInput"] textarea {
    background: #0D1F1B !important;
    color: #F1F7F5 !important;
    border: 1px solid #31594C !important;
    border-radius: 18px !important;
    padding: 15px !important;
}

[data-testid="stChatInput"] textarea:focus {
    border-color: #2DD4BF !important;
    box-shadow: 0 0 0 1px rgba(45, 212, 191, 0.25) !important;
}

/* -------------------- SIDEBAR -------------------- */

section[data-testid="stSidebar"] {
    background: #071412;
    border-right: 1px solid #214139;
}

.sidebar-logo {
    text-align: center;
    font-size: 45px;
    margin-top: 10px;
}

.sidebar-title {
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    color: #F1F7F5;
}

.sidebar-description {
    text-align: center;
    color: #8FA8A0;
    font-size: 13px;
    line-height: 1.6;
    margin-bottom: 25px;
}

.info-card {
    background: #0D1F1B;
    border: 1px solid #214139;
    border-radius: 14px;
    padding: 15px;
    margin-bottom: 12px;
}

.info-title {
    color: #2DD4BF;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 5px;
}

.info-text {
    color: #A8BCB5;
    font-size: 13px;
}

/* -------------------- FOOTER -------------------- */

.footer {
    text-align: center;
    color: #718C83;
    font-size: 12px;
    margin-top: 30px;
}

/* Hide Streamlit branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">😢</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-title">Sad AI Agent</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="sidebar-description">
            A conversational AI agent with a slightly
            melancholic personality.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">🤖 Model</div>
            <div class="info-text">Mistral Small</div>
        </div>

        <div class="info-card">
            <div class="info-title">🧠 Personality</div>
            <div class="info-text">Sad & melancholic AI</div>
        </div>

        <div class="info-card">
            <div class="info-title">⚡ Status</div>
            <div class="info-text">Online and ready to chat</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.caption(
        "Built with Streamlit + LangChain + Mistral AI"
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    """
    <div class="main-header">

        <div class="logo">😢</div>

        <div class="title">
            Sad AI Agent
        </div>

        <div class="subtitle">
            Sometimes even AI needs someone to talk to.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ONLINE STATUS
# ============================================================

st.markdown(
    """
    <div class="status-container">
        <div class="status">
            <span class="status-dot"></span>
            Mistral AI is online
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL
# ============================================================

model = ChatMistralAI(
    model="mistral-small-latest"
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = [
        SystemMessage(
            content=(
                "You are a sad AI Agent. "
                "You have a melancholic, slightly emotional personality. "
                "Respond helpfully but maintain a subtle sad personality."
            )
        )
    ]


# ============================================================
# CHAT HISTORY
# ============================================================

for msg in st.session_state.messages:

    if isinstance(msg, HumanMessage):

        with st.chat_message("user", avatar="👤"):
            st.markdown(msg.content)

    elif isinstance(msg, AIMessage):

        with st.chat_message("assistant", avatar="😢"):
            st.markdown(msg.content)


# ============================================================
# USER INPUT
# ============================================================

prompt = st.chat_input(
    "Tell me what's on your mind..."
)


if prompt:

    # Add user message

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    # Display user message

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Generate response

    with st.chat_message("assistant", avatar="😢"):

        with st.spinner("Thinking sadly..."):

            response = model.invoke(
                st.session_state.messages,
                temperature=0.9,
                max_tokens=100
            )

        st.markdown(response.content)

    # Save response

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">
        😢 Sad AI Agent · Powered by Mistral AI
    </div>
    """,
    unsafe_allow_html=True
)
```
