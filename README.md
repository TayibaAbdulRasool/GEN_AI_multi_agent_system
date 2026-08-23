# Multi-Agent Research System

A research automation system built with multiple AI agents. Each agent is responsible for a specific stage of the research process, from finding information to reviewing the final report.

## Overview

The system uses four agents:

1. **Search Agent** – Searches the web and collects relevant information.
2. **Reader Agent** – Reads and analyzes the collected research.
3. **Writer Agent** – Generates a structured research report.
4. **Critic Agent** – Reviews the report and identifies areas that need improvement.

### Workflow

```text
Research Topic
      |
      v
Search Agent
      |
      v
Reader Agent
      |
      v
Writer Agent
      |
      v
Critic Agent
      |
      v
Final Research Report
```

## Technologies

* Python
* LangChain
* Mistral AI
* Tavily
* Streamlit
* BeautifulSoup
* Requests
* python-dotenv

## Project Structure

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

## Setup

Clone the repository:

```bash
git clone https://github.com/your-username/multi-agent-research-system.git
cd multi-agent-research-system
```

Create and activate a virtual environment:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Do not upload the `.env` file to GitHub.

## Run

If using Streamlit:

```bash
streamlit run app.py
```

## Example

The user provides a topic such as:

```text
Impact of Generative AI on Software Development
```

The system searches for relevant information, analyzes the sources, generates a report, and then reviews the report using the Critic Agent.

## Future Improvements

* Improve source evaluation
* Add citation generation
* Add PDF report export
* Add research history
* Add more specialized agents
* Deploy the application

## Author

**Tayiba Abdul Rasool**

Software Engineering Student
