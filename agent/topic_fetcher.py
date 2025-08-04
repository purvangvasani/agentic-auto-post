from ddgs import DDGS

def get_trending_topic(query="tech trends", region="US"):
    with DDGS() as ddgs:
        results = ddgs.text(query)
        if not results:
            return "AI in business"
        return results[0]['title']



# from ddgs import DDGS
# from datetime import datetime, timedelta
# import re

# def get_trending_topic(query="yesterday's top technology and business trends", region="wt-wt"):
    """
    Dynamically fetch yesterday's top trending topic in technology and business.
    
    Args:
        query (str): Search query to find trending topics (default: "yesterday's top technology and business trends").
        region (str): Region code for search (default: "wt-wt" for worldwide).
    
    Returns:
        str: Title or description of the top trending topic, or a fallback message if none found.
    """
    # Calculate yesterday's date
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    # Refine query to focus on yesterday's trends
    refined_query = f"{query} {yesterday} site:*.com | site:*.org | site:*.edu -inurl:(login | signup)"

    try:
        with DDGS() as ddgs:
            # Fetch search results (use safesearch='off' to avoid filtering, set region to worldwide)
            results = ddgs.text(query=refined_query, safesearch='off', region=region, max_results=1)
            # Convert results to list and ensure it’s iterable
            results = list(results) if results else []
            
            if not results:
                print(f"No results found for query: {refined_query}")
                return "No trending topics found for yesterday. Fallback: AI in business."
            print(len(results))
            # Filter results for relevance and recency
            for result in results:
                title = result.get('title', '')
                print("Title:",title)
                body = result.get('body', '')
                print("Body:",body)
                url = result.get('href', '')
                print("URL:",url)
                
                # Check if result is relevant to technology/business and mentions "trend"
                if any(keyword in title.lower() or keyword in body.lower() for keyword in ['trend', 'trending', 'technology', 'business', 'tech', 'innovation', 'market', 'AI', 'artificial intelligence', 'stock market', 'crypto', 'cryptocurrency', 'USA', 'US', 'America', 'gold']):
                    print("Found relevant result:", title)
                    # Prioritize results from trusted sources or those mentioning yesterday
                    trusted_domains = ['reuters.com', 'mckinsey.com', 'explodingtopics.com', 'wired.com', 'bbc.com', 'cnbc.com', 'techspot.com']
                    if any(domain in url for domain in trusted_domains) or yesterday in title or yesterday in body:
                        # Clean title to extract meaningful topic
                        topic = re.sub(r' -.*$', '', title)  # Remove source suffix (e.g., " - Reuters")
                        topic = re.sub(r'^.*: ', '', topic)  # Remove prefix like "Tech News: "
                        return topic.strip() or "AI in business"  # Return cleaned topic or fallback
            
                    topic = re.sub(r' -.*$', '', title)  # Remove source suffix (e.g., " - Reuters")
                    topic = re.sub(r'^.*: ', '', topic)  # Remove prefix like "Tech News: "
                    return topic.strip() or "AI in business"  # Return cleaned topic or fallback
            # If no relevant result is found, return fallback
            print(f"No relevant results found for query: {refined_query}")
            return "No trending topics found for yesterday. Fallback: AI in business."
            
    except Exception as e:
        print(f"Error fetching trends: {str(e)}")
        return "Error occurred. Fallback: AI in business."