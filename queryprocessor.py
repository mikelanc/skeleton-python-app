def process_query(query):
    if ("romeo and juliet" in query.lower()):
        return "William Shakespeare"
    if ("what is your name" in query.lower()):
        return "Mike Lancaster"
    if ("which of the following numbers is the largest" in query.lower()):
        #print max(query.split(":")[1].split(","))
        #print map(int,query.split(":")[1].split(","))
        return max(map(int,query.split(":")[1].split(",")))
    if ("plus" in query.lower()):
        return sum([int(s) for s in query.split() if s.isdigit()])
    if ("which year was Theresa May first elected" in query.lower()):
        return "2016"
    if ("james bond" in query.lower()):
        return "Sean Connery"
    if ("eiffel" in query.lower()):
        return "Paris"
    return ""
