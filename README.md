# Multi-Agent Research System

An AI-powered research automation system that uses multiple specialized agents to search, analyze, write, and review research content.

Instead of using a single AI model for the complete research task, the project divides the research process into **four specialized agents**, where each agent is responsible for a specific stage of the workflow.

## Live Application

**Streamlit Application:**
https://tayibaabdulrasool-multi-agent-system-app-rwnjhe.streamlit.app/

## Project Overview

The **Multi-Agent Research System** automates the process of creating a structured research report from a user-provided topic.

The system takes a research topic as input and passes it through a sequence of specialized agents:

```text
Research Topic
      ↓
Search Agent
      ↓
Reader Agent
      ↓
Writer Agent
      ↓
Critic Agent
      ↓
Final Research Report
```

Each stage has a different responsibility, making the workflow more organized than asking a single AI agent to perform the entire research process.

## How My Project Works

### 1. User Provides a Research Topic

The user enters a research topic through the Streamlit interface.

For example:

```text
Impact of Generative AI on Software Development
```

This topic becomes the starting point of the research pipeline.

### 2. Search Agent

The **Search Agent** is responsible for finding relevant information about the research topic.

It uses web search capabilities through **Tavily** to discover relevant sources.

The purpose of this agent is to collect useful information that can be passed to the next stage instead of allowing the writing agent to generate a report without external research.

### 3. Reader Agent

The **Reader Agent** processes the information collected during the search stage.

Its responsibility is to:

* Read the retrieved information
* Analyze the relevant content
* Extract useful information
* Organize the research material
* Prepare the information for report generation

This stage separates **research analysis** from **report writing**.

### 4. Writer Agent

The **Writer Agent** uses the processed research information to generate a structured research report.

It receives the output of the Reader Agent and turns the collected information into a readable report.

The Writer Agent is responsible for transforming the research material into a coherent final document.

### 5. Critic Agent

The **Critic Agent** reviews the generated report.

Instead of immediately returning the Writer Agent's output, the system adds a separate review stage.

The Critic Agent checks the generated report and identifies areas that may require improvement.

This introduces a basic **generation → evaluation** cycle into the research pipeline.

## Agent Architecture

The project contains four specialized agents:

| Agent            | Main Responsibility                                      |
| ---------------- | -------------------------------------------------------- |
| **Search Agent** | Finds relevant information from the web                  |
| **Reader Agent** | Reads and analyzes retrieved research                    |
| **Writer Agent** | Generates the structured research report                 |
| **Critic Agent** | Reviews the generated report and identifies improvements |

This architecture allows each agent to focus on one task instead of making one agent responsible for the entire workflow.

## Agent Workflow

```text
                         User
                          |
                          ↓
                  Research Topic
                          |
                          ↓
                  ┌───────────────┐
                  │ Search Agent  │
                  │   Tavily      │
                  └───────┬───────┘
                          |
                          ↓
                  ┌───────────────┐
                  │ Reader Agent  │
                  │ Research      │
                  │ Analysis      │
                  └───────┬───────┘
                          |
                          ↓
                  ┌───────────────┐
                  │ Writer Agent  │
                  │ Report        │
                  │ Generation    │
                  └───────┬───────┘
                          |
                          ↓
                  ┌───────────────┐
                  │ Critic Agent  │
                  │ Report Review │
                  └───────┬───────┘
                          |
                          ↓
                  Final Research Report
```

## Tools Used in the System

The project combines LLMs with external tools to perform the research workflow.

### Tavily

Used by the Search Agent to search the web and retrieve relevant research information.

### Web Requests & BeautifulSoup

`Requests` and `BeautifulSoup` are used for retrieving and processing web content where required by the research tools.

### Mistral AI

Mistral models provide the language-model capabilities used by the agents for research analysis, report generation, and critique.

### LangChain

LangChain is used to structure the agent-based workflow and connect the language model with the research tools.

### Streamlit

Streamlit provides the user interface for entering a research topic and displaying the generated research output.

## Project Files

```text
MULTI_AGENT_SYSTEM/
│
├── agents.py
├── pipeline.py
├── tools.py
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Project Structure Explained

### `agents.py`

Contains the definitions and instructions for the specialized AI agents.

The four main agents are:

* Search Agent
* Reader Agent
* Writer Agent
* Critic Agent

Each agent has a specific role within the research process.

### `pipeline.py`

Contains the main research workflow.

It controls how information moves between the agents:

```text
Search → Read → Write → Critique
```

This file connects the individual agent stages into one complete pipeline.

### `tools.py`

Contains the tools used by the agents to obtain and process external information.

This includes functionality related to web searching and web content retrieval.

### `app.py`

Contains the Streamlit application.

It provides the interface through which the user enters a research topic and receives the generated research output.

### `requirements.txt`

Contains the Python packages required to run the project.

### `.env`

Stores API credentials such as:

```text
MISTRAL_API_KEY
TAVILY_API_KEY
```

The `.env` file is excluded from GitHub using `.gitignore` to prevent API credentials from being exposed.

### `.gitignore`

Prevents sensitive and unnecessary files, such as environment variables and local environment files, from being committed to the repository.

## Technologies

| Technology        | Purpose                                           |
| ----------------- | ------------------------------------------------- |
| **Python**        | Core programming language                         |
| **LangChain**     | Agent and LLM workflow                            |
| **Mistral AI**    | Language model for agent reasoning and generation |
| **Tavily**        | Web search and research retrieval                 |
| **BeautifulSoup** | Web content parsing                               |
| **Requests**      | HTTP requests and web retrieval                   |
| **Streamlit**     | Interactive web interface                         |
| **python-dotenv** | Environment variable management                   |
| **Git & GitHub**  | Version control                                   |

## Example Research Flow

Suppose the user enters:

```text
Impact of Generative AI on Software Development
```

The system processes the topic as follows:

**Search Agent**

Finds relevant information and sources related to Generative AI and software development.

↓

**Reader Agent**

Analyzes the retrieved research and extracts useful information.

↓

**Writer Agent**

Uses the analyzed information to generate a structured research report.

↓

**Critic Agent**

Reviews the generated report and identifies potential weaknesses or areas for improvement.

↓

**Final Output**

The user receives the resulting research report through the Streamlit application.

## UI Interface

![Multi-Agent Research System](https://github.com/user-attachments/assets/b64e5320-0d54-4568-ba65-4a29657d0ca8)

The Streamlit interface provides a simple way to submit a research topic and interact with the multi-agent research pipeline.

## Why a Multi-Agent Approach?

The main idea behind the project is **task specialization**.

A traditional single-agent approach could ask one LLM to:

```text
Search → Read → Analyze → Write → Review
```

The project instead separates these responsibilities:

```text
Search Agent  → Research Retrieval
Reader Agent  → Research Analysis
Writer Agent  → Report Generation
Critic Agent  → Quality Review
```

This makes the workflow easier to organize, understand, and extend.

## Key Learning Outcomes

Through this project, I worked with:

* Multi-agent AI architecture
* LLM-based task specialization
* LangChain agent workflows
* Tool integration with LLMs
* Web search and information retrieval
* Research automation
* Sequential agent pipelines
* AI-generated report creation
* AI-based output critique
* Streamlit application development
* Environment variable and API-key management

## Future Improvements

* Improve source evaluation and reliability
* Add automatic citations to generated reports
* Add PDF report export
* Store previous research sessions
* Add additional specialized research agents
* Improve the Critic Agent with more detailed evaluation criteria
* Add iterative revision between the Writer and Critic agents

## Author

**Tayiba Abdul Rasool**

