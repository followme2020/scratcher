import re
import requests
import bs4
from bs4 import BeautifulSoup
import time

name_of_file = 'data_file.json' #for each page of search, new json file will be added
pages_to_scan = input(int("Please enter amount of pages needed (each page creates new file)"))
res = requests.get('https://www.yad2.co.il/realestate/forsale?city=7900')
soup = bs4.BeautifulSoup(res.text, 'lxml')
blocks = soup.select('.feeditem.table')
pattern = r'item-id=\"......\"'
matches = re.finditer(pattern, str(blocks), re.MULTILINE)
results = []
for matchNum, match in enumerate(matches, start=1):
    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))
    results.append(match.group()[9:-1])


print(results)
time.sleep(2)
