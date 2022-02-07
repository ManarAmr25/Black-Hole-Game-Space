from database import db_manager
import os
import requests

import requests
response = requests.get("https://opentdb.com/api.php?amount=1")
print(response)
print(response.json()['results'])

