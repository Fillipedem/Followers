from crawler import TwitterCrawler


crawler = TwitterCrawler("Fillipedem", 2)
s = crawler.search()

for key in s:
    print(key, len(s[key]))
