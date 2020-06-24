def process_query(query):
    if ("romeo and juliet" in query.lower()):
        return "William Shakespeare"
    if ("what is your name" in query.lower()):
        return "Mike Lancaster"
    if ("which of the following numbers is the largest" in query.lower()):
        return query.split(":").max()
    if ("plus" in query.lower()):
        return [int(s) for s in query.split() if s.isdigit()].sum()
    return ""
