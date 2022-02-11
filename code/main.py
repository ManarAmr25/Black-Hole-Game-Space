from database import db_manager
import os
import requests
from queue import PriorityQueue

import requests
response = requests.get("https://opentdb.com/api.php?amount=1")
print(response)
print(response.json()['results'])

p = PriorityQueue()
for x in range(4):
    p.put((0, x))

print(p.qsize())
print(p.get())
print(p.qsize())
print(p.get())
print(p.qsize())
print(p.get())
print(p.qsize())

