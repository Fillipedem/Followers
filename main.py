"""
Crawler
"""
import tweepy
import time


# Graph
graph = {}
frontier = []
file_graph = 'graphs\search.txt'
ids_to_screen = {}

# Tweepy API Auth
print("Autenticado")
auth = tweepy.OAuthHandler('preencher', 'preencher')
auth.set_access_token('preencher',
                        'preencher')

api = tweepy.API(auth, wait_on_rate_limit=True)

# Search Followers from start user
print("Buscando Followers")
user = api.get_user('carequinha10')

frontier.append(user.id)

for friends in tweepy.Cursor(api.followers_ids, user_id=user.id).pages():

    frontier.extend(friends)
    #for f in friends:
    #    frontier.append(f.screen_name)

print(len(frontier))

# Search Following
print("Buscando Following")
for user in frontier:
    # log
    print("Get user: " + str(user))

    # adding node
    graph[user] = []

    try:
        # search followings on frontier
        for page in tweepy.Cursor(api.friends_ids, user_id=user).pages(2):

            graph[user].extend(page)
    except tweepy.error.TweepError:
        print("Usuário: " + str(user) + " Não Autorizado!!")

    # escrevendo
    with open(file_graph, 'a') as f:

        f.write(str(user))

        for friend in graph[user]:
            f.write(";" + str(friend))

        f.write('\n')

    time.sleep(15)



