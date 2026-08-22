"""
Streamlit UI for the Multi-Agent Research System.

Run with:
    streamlit run app.py

This file expects to sit alongside agents.py, pipeline.py, tools.py and .env
in the same folder (MULTI_AGENT_SYSTEM).
"""

import streamlit as st
from datetime import datetime

from agents import (
    built_reader_agent,
    built_search_agent,
    writer_chain,
    critics_chain,
)

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------
st.set_page_config(
    page_title="Research Agent System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------------------------------
# Custom CSS — dark theme, professional look
# --------------------------------------------------------------------------
st.markdown(
    """
    <style>
    :root {
        --bg-primary: #0e1117;
        --bg-secondary: #161a23;
        --bg-card: #1a1f2b;
        --accent: #6c5ce7;
        --accent-soft: #a29bfe;
        --text-primary: #e8e9ed;
        --text-muted: #9aa0ac;
        --border: #2a2f3a;
        --success: #2ecc71;
        --warning: #f1c40f;
    }

    .stApp {
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }

    section[data-testid="stSidebar"] {
        background-color: var(--bg-secondary);
        border-right: 1px solid var(--border);
    }

    h1, h2, h3, h4 {
        color: var(--text-primary) !important;
        font-family: 'Segoe UI', sans-serif;
        letter-spacing: 0.3px;
    }

    .hero {
        padding: 1.6rem 2rem;
        border-radius: 14px;
        background: linear-gradient(135deg, #1a1f2b 0%, #201a33 100%);
        border: 1px solid var(--border);
        margin-bottom: 1.5rem;
    }
    .hero h1 {
        margin: 0;
        font-size: 2rem;
        background: linear-gradient(90deg, #a29bfe, #6c5ce7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p {
        color: var(--text-muted);
        margin-top: 0.4rem;
        font-size: 0.95rem;
    }

    .card {
        background-color: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.3rem 1.5rem;
        margin-bottom: 1rem;
    }

    .badge {
        display: inline-block;
        padding: 0.15rem 0.6rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        background: rgba(108, 92, 231, 0.15);
        color: var(--accent-soft);
        border: 1px solid rgba(108, 92, 231, 0.35);
        margin-bottom: 0.6rem;
    }

    .stButton > button {
        background: linear-gradient(90deg, #6c5ce7, #8172f0);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.55rem 1.4rem;
        font-weight: 600;
        transition: 0.2s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #7c6bf0, #9384f5);
        box-shadow: 0 0 14px rgba(108, 92, 231, 0.45);
    }

    .stTextInput > div > div > input,
    .stTextArea textarea {
        background-color: var(--bg-card);
        color: var(--text-primary);
        border: 1px solid var(--border);
        border-radius: 8px;
    }

    div[data-testid="stStatusWidget"] {
        background-color: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 10px;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### 🧠 Research Agent System")
    st.markdown(
        "A multi-agent pipeline that **searches**, **reads**, **writes**, "
        "and **critiques** a research report on any topic."
    )
    st.markdown("---")
    st.markdown("**Pipeline stages**")
    st.markdown(
        "1. 🔍 Search Agent\n"
        "2. 📖 Reader Agent\n"
        "3. ✍️ Writer\n"
        "4. 🧐 Critic"
    )
    st.markdown("---")
    st.caption(f"Session started: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# --------------------------------------------------------------------------
# Hero header
# --------------------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <h1>Multi-Agent Research System</h1>
        <p>Enter a topic and let the search, reader, writer and critic agents
        collaborate to produce a reviewed research report.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Session state
# --------------------------------------------------------------------------
if "result" not in st.session_state:
    st.session_state.result = None

# --------------------------------------------------------------------------
# Input row
# --------------------------------------------------------------------------
col1, col2 = st.columns([4, 1])
with col1:
    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Impact of quantum computing on cryptography",
        label_visibility="collapsed",
    )
with col2:
    run_clicked = st.button("🚀 Run Research", use_container_width=True)

# --------------------------------------------------------------------------
# Pipeline execution with live step-by-step UI
# --------------------------------------------------------------------------
if run_clicked:
    if not topic or not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        state = {}

        with st.status("Step 1 — Search agent gathering sources...", expanded=True) as status:
            search_agent = built_search_agent()
            search_result = search_agent.invoke(
                {
                    "messages": [
                        (
                            "user",
                            f"Find recent, reliable, and relevant information about: {topic}",
                        )
                    ]
                }
            )
            state["search_result"] = search_result["messages"][-1].content
            status.update(label="Step 1 — Search complete ✅", state="complete")

        with st.status("Step 2 — Reader agent analyzing & scraping sources...", expanded=True) as status:
            reader_agent = built_reader_agent()
            reader_result = reader_agent.invoke(
                {
                    "messages": [
                        (
                            "user",
                            f"""Analyze the search results below for the topic: {topic}.

Select the most relevant URLs and scrape them for deeper research.

Search Results:
{state["search_result"]}""",
                        )
                    ]
                }
            )
            state["research"] = reader_result["messages"][-1].content
            status.update(label="Step 2 — Research complete ✅", state="complete")

        with st.status("Step 3 — Writer drafting the report...", expanded=True) as status:
            state["report"] = writer_chain.invoke(
                {"topic": topic, "research": state["research"]}
            )
            status.update(label="Step 3 — Draft complete ✅", state="complete")

        with st.status("Step 4 — Critic reviewing the report...", expanded=True) as status:
            state["critics"] = critics_chain.invoke(
                {"topic": topic, "report": state["report"]}
            )
            status.update(label="Step 4 — Review complete ✅", state="complete")

        state["topic"] = topic
        st.session_state.result = state
        st.success("Pipeline finished successfully.")

# --------------------------------------------------------------------------
# Results display
# --------------------------------------------------------------------------
if st.session_state.result:
    result = st.session_state.result

    st.markdown("---")
    st.markdown(f"## Results for: *{result['topic']}*")

    tab_report, tab_critic, tab_research, tab_search = st.tabs(
        ["📄 Final Report", "🧐 Critic Review", "📖 Research Notes", "🔍 Search Results"]
    )

    with tab_report:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<span class="badge">FINAL REPORT</span>', unsafe_allow_html=True)
        st.markdown(result["report"])
        st.markdown("</div>", unsafe_allow_html=True)
        st.download_button(
            "⬇️ Download report (.md)",
            data=str(result["report"]),
            file_name=f"report_{result['topic'][:30].replace(' ', '_')}.md",
            mime="text/markdown",
        )

    with tab_critic:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<span class="badge">CRITIC REVIEW</span>', unsafe_allow_html=True)
        st.markdown(result["critics"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_research:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<span class="badge">READER OUTPUT</span>', unsafe_allow_html=True)
        st.markdown(result["research"])
        st.markdown("</div>", unsafe_allow_html=True)

    with tab_search:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<span class="badge">SEARCH OUTPUT</span>', unsafe_allow_html=True)
        st.markdown(result["search_result"])
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("Enter a topic above and click **Run Research** to start the pipeline.")
