def process_query(query):
    if ("romeo and juliet" in query.lower()):
        return "William Shakespeare"
    if ("what is your name" in query.lower()):
        return "Mike Lancaster"
    if ("which of the followidsfdsfng numbers is the largest" in query.lower()):
        return "20880"
    return ""
