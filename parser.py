import json

from fake_useragent import UserAgent
import requests
import certifi

user_agent = UserAgent(verify_ssl=False)


def data_collect():
    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=30&hasTradeLock=true&isStore=true&limit=60&maxPrice=10000&minPrice=100&offset={item }&sort=botFirst&tradeLockDays=1&tradeLockDays=2&tradeLockDays=3&tradeLockDays=4&tradeLockDays=5&tradeLockDays=6&tradeLockDays=7&tradeLockDays=0&withStack=true'
            response = requests.get(
                url=url, headers={'user-agent': f'{user_agent.random}'})
            offset += batch_size
            data = response.json()
            item = data.get('items')

            for i in item:
                if i.get('overprice') is not None and i.get('overprice') < -10:
                    item_full_name = i.get('fullname')
                    item_3d = i.get('3d')
                    item_price = i.get('price')
                    item_over_price = i.get('overprice')

                    result.append(
                        {
                            'full_name': item_full_name,
                            '3d': item_3d,
                            'overprice': item_over_price,
                            'item_price': item_price
                        })
        count += 1
        print(f'Page #{count}')
        #print(url)
        if len(item) < 60:
            break
        if count >10:
            break

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))


def main():
    data_collect()


if __name__ == '__main__':
    main()
