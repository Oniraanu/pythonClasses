from functools import reduce

twitter = [
    {"name": "Bakre Olubunmi", "username": "@olubunmee__", "age": 27,
     "tweets": ["Hello world!", "Messi is the undisputed GOAT", "I should get a vasectomy soon", "god doesn't exist"],
     "status": "verified"},
    {"name": "Love Orobola", "username": "@orobola5", "age": 26,
     "tweets": ["Hi, i'm new here", "I love Jesus", "My oh my"], "status": "not verified"},
    {"name": "Jonathan Martins", "username": "@dejmartins", "age": 22,
     "tweets": ["Y'all should see An inconvenient truth", "Its really good"], "status": "verified"},
    {"name": "Tolani Jinadu", "username": "@teeswitch", "age": 24,
     "tweets": ["Guess who just became a front-end dev", "HTML is really underrated", "Java is trash"],
     "status": "verified"},
    {"name": "Ismail Olajide", "username": "@ismaeel", "age": 29, "tweets": ["Geospatial technology is the future"],
     "status": "not verified"},
    {"name": "Bassey Edet", "username": "@The_Law", "age": 27,
     "tweets": ["Hala Madrid!!!", "I really want to get into sports agency", "Smart contracts...Hmmm"],
     "status": "verified"},
    {"name": "John Doe", "username": "@Johndoe", "age": 25, "tweets": ["Hello, i'm John"], "status": "not verified"},
    {"name": "Justin Imo", "username": "@just_surveys", "age": 29, "tweets": ["Hola ma niggas"],
     "status": "not verified"},
    {"name": "Ansu Fati", "username": "@ansumannefati", "age": 18,
     "tweets": ["Forca Barca", "Getting the ballon d'or next season insha Allah"], "status": "verified"},
    {"name": "Harvey Spectre", "username": "@harveyy", "age": 19, "tweets": [], "status": "not verified"}
]

#  comprehension list
print([tweet["username"] for tweet in twitter if tweet["status"] == "verified"])

print([tweet["username"] for tweet in twitter if tweet["tweets"] != []])

print([tweet["username"] for tweet in twitter if tweet["status"] == "verified" and tweet["age"] < 25])

longest = reduce(lambda x, y: x if x["age"] > y["age"] else y, twitter)
print(longest)

shortest = reduce(lambda x, y: x if x["age"] < y["age"] else y, twitter)
print(shortest)

print(max(tweet["age"] for tweet in twitter))

print(min(tweet["age"] for tweet in twitter))

print(sum(tweet["age"] for tweet in twitter) / len(twitter))

print(reduce(lambda x, y: x + y, (tweet["age"] for tweet in twitter)) / len(twitter))


most_tweets = max(twitter, key=lambda tweet: len(tweet["tweets"]))
print(most_tweets)














