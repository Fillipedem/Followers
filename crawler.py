"""
Crawler
"""
import tweepy
import time


class TwitterCrawler:

    waiting_time = 60

    def __init__(self, start_user, depth=2, file='search.txt'):

        self.__api = self.__authenticate()

        self.start = self.__get_user_id(start_user)
        self.depth = depth
        self.file = file

    def __get_user_id(self, start_user):
        user = self.__api.get_user(start_user)

        return user.id

    def __authenticate(self):
        """
        :return tweepy api object:
        """
        ###
        auth = tweepy.OAuthHandler('preencher', 'preencher')
        auth.set_access_token('preencher',
                              'preencher')

        return tweepy.API(auth)

    def __get_friends(self, user_id):
        """
        :param user - user id on twitter:
        :return list of users ids:
        """

        ids = []
        for page in tweepy.Cursor(self.__api.friends_ids, user_id=user_id).pages(1):
            ids.extend(page)

            time.sleep(self.waiting_time)

        return ids

    def __write(self, user, friends_list):

        with open(self.file, 'a') as f:

            f.write(str(user))

            for friend in friends_list:
                f.write(";" + str(friend))

            f.write('\n')

    def __bfs(self):

        level = {}
        frontier = [self.start]
        count = 0

        while frontier and count <= self.depth:

            new_frontier = []

            print("Tamanho atual da fronteira: ", len(frontier))
            print("Profudindade da pesquisa: ", count)
            print("Nós visitados: ", len(level))
            # para cada no na fronteira
            for u in frontier:
                print("No Visitado: ", u)
                # Checando se já visitamos
                if u not in level:
                    level[u] = []

                    # checando a lista de adjacencia do vertice u
                    for v in self.__get_friends(u):
                        level[u].append(v)
                        new_frontier.append(v)

                    # escrenvedo no arquivo
                    self.__write(u, level[u])

            frontier = new_frontier
            count += 1

        return level

    def search(self):
        """
        Realiza busca em largura
        :return lista de adjacencia:
        """
        return self.__bfs()



