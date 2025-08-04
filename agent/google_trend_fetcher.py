from pytrends.request import TrendReq

def get_google_trending_topic():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["technology"])
    trends = pytrends.related_queries()
    related = trends.get("technology", {}).get("top", {})
    if related and "query" in related.columns:
        return related["query"].iloc[0]
    return "Emerging technology"
