from agents import build_search_agent, build_scrape_agent, writer_chain, critic_chain


def run_research_pipeline_steps(topic: str) -> dict:
    state = {}

    search_agent = build_search_agent()
    search_results = search_agent.invoke({
        'messages': [('user', f"find recent, reliable and detailed information about the topic: {topic}")]
    })
    state['search_results'] = search_results['messages'][-1].content

    scrape_agent = build_scrape_agent()
    scrape_results = scrape_agent.invoke({
        'messages': [('user',
                       f"Based on the following search results about `{topic}`,"
                       f"pick the most relevant URL and scrap it for deeper content.\n\n"
                       f"Search Results:\n{state['search_results'][:800]}")]
    })
    state['scraped_content'] = scrape_results['messages'][-1].content

    research_combined = (
        f"Search Results:\n{state['search_results']}\n\n"
        f"Scraped Content:\n{state['scraped_content']}"
    )
    state['report'] = writer_chain.invoke({
        'topic': topic,
        'research': research_combined
    })

    state['critique'] = critic_chain.invoke({
        'report': state['report']
    })

    return state