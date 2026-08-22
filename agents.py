import os

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_url

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

if not api_key:
    raise ValueError("MISTRAL_API_KEY is missing from Streamlit Secrets")

llm = ChatMistralAI(
    model="mistral-small-latest",
    api_key=api_key
)

def built_search_agent():
    return create_agent(
        model=llm,
        tools=[web_search]
    )


def built_reader_agent():
    return create_agent(
        model=llm,
        tools=[scrape_url]
    )


# Writer Chain
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer. "
        "Write clear, accurate, well-structured, and detailed research reports. "
        "Use the provided research information to create a professional report."
    ),
    (
        "human",
        """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

The report should contain only these sections:

1. Introduction
2. Key Findings (Provide exactly 3 well-explained key findings.)
3. Conclusion
4. Sources

Do not add any other sections."""
    )
])

writer_chain = writer_prompt | llm | StrOutputParser()


# Critics Chain
critics_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research report critic. "
        "Evaluate the report objectively and concisely."
    ),
    (
        "human",
        """Critically review the research report below.

Topic: {topic}

Research Report:
{report}

Respond ONLY in this format:

Score: X/10

Strength:
- Mention the main strengths of the report.

Improvement Areas:
- Mention the most important areas that need improvement.

Verdict:
- Give a one-line final verdict."""
    )
])

critics_chain = critics_prompt | llm | StrOutputParser()
