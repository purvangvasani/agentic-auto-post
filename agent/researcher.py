from ddgs import DDGS

def research_topic():
    with DDGS() as ddgs:
        results = list(ddgs.text("latest trends in AI", max_results=3))
        if results:
            return results[0]['title'] + ": " + results[0]['body']
    return "AI in business"