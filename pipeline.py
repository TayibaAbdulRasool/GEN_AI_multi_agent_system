from agents import (
    built_reader_agent,
    built_search_agent,
    writer_chain,
    critics_chain
)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # Search agent
    print("\n" + "=" * 50)
    print("Step 1: Search agent is working......")
    print("=" * 50)

    search_agent = built_search_agent()

    search_result = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable, and relevant information about: {topic}"
            )
        ]
    })

    state["search_result"] = search_result["messages"][-1].content

    print(state["search_result"])

    # Reader agent
    print("\n" + "=" * 50)
    print("Step 2: Reader agent is working......")
    print("=" * 50)

    reader_agent = built_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""Analyze the search results below for the topic: {topic}.

Select the most relevant URLs and scrape them for deeper research.

Search Results:
{state["search_result"]}"""
            )
        ]
    })

    state["research"] = reader_result["messages"][-1].content

    print(state["research"])

    # Writer chain
    print("\n" + "=" * 50)
    print("Step 3: Writer is working......")
    print("=" * 50)

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": state["research"]
    })

    print("\nFinal Report:")
    print(state["report"])

    # Critics chain
    print("\n" + "=" * 50)
    print("Step 4: Critic is working......")
    print("=" * 50)

    state["critics"] = critics_chain.invoke({
        "topic": topic,
        "report": state["report"]
    })

    print("\nCritic Result:")
    print(state["critics"])

    return state


if __name__ == "__main__":
    topic = input("Enter research topic: ")

    result = run_research_pipeline(topic)

    print("\n" + "=" * 50)
    print("FINAL RESEARCH REPORT")
    print("=" * 50)

    print(result["report"])

    print("\n" + "=" * 50)
    print("CRITIC REVIEW")
    print("=" * 50)

    print(result["critics"])