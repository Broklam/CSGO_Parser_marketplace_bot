import json

from fake_useragent import UserAgent
import requests
import certifi

user_agent = UserAgent()


def get_3d(smth, id):
    url1 = f'https://cs.money/skin_info?appId=730&id={id}&isBot=true&isStore=true&botInventory=true'
    response = requests.get(
        url=url1, headers={'user-agent': f'{user_agent.random}'})
    data = response.json()
    dd = data.get(smth)

    return dd


def data_collect():
    offset = 0
    batch_size = 60
    result = []
    count = 0

    while True:
        for item in range(offset, offset + batch_size, 60):
            url = f'https://inventories.cs.money/5.0/load_bots_inventory/730?buyBonus=30&isStore=true&limit=60' \
                  f'&maxPrice=3000.5892538833715&minPrice=150&o' \
                  f'ffset={offset}&sort=botFirst&withStack=true '
            response = requests.get(
                url=url, headers={'user-agent': f'{user_agent.random}'})
            offset += batch_size
            data = response.json()
            item = data.get('items')

            try:
                for i in item:
                    if i.get('overprice') is not None and i.get('overprice') < -10:
                        item_full_name = i.get('fullName')
                        item_price = i.get('price')
                        item_over_price = i.get('overprice')
                        item_def_price = get_3d("defaultPrice", i.get('id'))
                        item_disc = get_3d("discount", i.get('id'))
                        item_float = get_3d("float", i.get('id'))
                        item_old_price = get_3d("oldPrice",i.get('id'))


                        # item_img_link = i.get('steamImg')
                        item_3d = get_3d("3d", i.get('id'))
                        result.append(
                            {
                                'full_name': item_full_name,
                                '3d': item_3d,
                                'overprice': item_over_price,
                                'discount': item_disc,
                                'default price': item_def_price,
                                'item_price': item_price,
                                # 'URL IMAGE': item_img_link
                                'float': item_float,
                                'oldPrice': item_old_price,
                            })
                    elif TypeError:
                        break
                count += 1
                print(f'Page #{count}')
            except ValueError:
                pass
            except TypeError:
                pass
        print(url)
        if item is None:
            break
        #if count == 14:
            #break

    with open('result.json', 'w') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)

    print(len(result))


def main():
    data_collect()


if __name__ == '__main__':
    main()
