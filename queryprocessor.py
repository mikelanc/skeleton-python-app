def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    

def process_query(query):
    if ("romeo and juliet" in query.lower()):
        return "William Shakespeare"
    if ("what is your name" in query.lower()):
        return "Mike Lancaster"
    if ("which of the following numbers is the largest" in query.lower()):
        #print max(query.split(":")[1].split(","))
        #print map(int,query.split(":")[1].split(","))
        #return max(map(int,query.split(":")[1].split(",")))
        test_list = query.split(":")[1].split(",")
        test_list = list(map(int, test_list)) 
        return max(test_list)
    if ("plus" in query.lower()):
        return sum([int(s) for s in query.split() if s.isdigit()])
    if ("minus" in query.lower()):
        values = [int(s) for s in query.split() if s.isdigit()]
        return values[0] - values[1]
    if ("which year was Theresa May first elected" in query.lower()):
        return "2016"
    if ("james bond" in query.lower()):
        return "Sean Connery"
    if ("eiffel" in query.lower()):
        return "Paris"
    if ("are primes" in query.lower()):
        test_list = query.split(":")[1].split(",")
        test_list = list(map(int, test_list)) 
        newlist = []
        for i in test_list:
            if is_prime(i):
                newlist.append(i)
        return newlist
        #:%20457,%20586,%20353,%20467
    return ""
