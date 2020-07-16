import time
import requests
from worm_up import results, name_of_file
import json
import os

api_link = 'https://www.yad2.co.il/api/item/'
ready_to_use_url = []
for item in results:
    ready_to_use_url.append(api_link + item)

print("Starting new file!")
with open(name_of_file, 'a') as data_file:
    data_file.write('{"responses":[')

print("Writing data...")
for item in ready_to_use_url:
    time.sleep(3)
    response = requests.get(item)
    print("Connection Status: ", response.status_code)
    try:
        response.json()
    except json.decoder.JSONDecodeError:
        print("this is not a JSON format")

    data = response.json()
    with open(name_of_file, "a") as write_file:
        json.dump(response.json(), write_file)
        write_file.write(',')

print('Finishing the file!')
with open(name_of_file, 'a') as datafile:
    datafile.seek(0, os.SEEK_END) # Move to last
    datafile.seek(datafile.tell() - 1, os.SEEK_SET) # back One character
    datafile.truncate() # Delete the last comma ","
    datafile.write(']}')
