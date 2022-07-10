import json

import requests
from fake_useragent import UserAgent
user_agent = UserAgent(verify_ssl=False)
response = requests.get(
url = 'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=30&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=1&offset=4980&sort=botFirst&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&withStack=true',
headers={'user-agent': f'{user_agent.random}'}
)

with open('result.json', 'w') as file:
    json.dump(response.json(),file,indent=4,ensure_ascii=False)