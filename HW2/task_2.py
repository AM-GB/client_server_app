import json


def write_order_to_json(item, quantity, price, buyer, date):

    dict_data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }

    with open('orders.json') as f:
        objs = json.load(f)

    for k in objs.keys():
        if k == 'orders':
            objs[k].append(dict_data)

    with open('orders.json', 'w') as f:
        f.write(json.dumps(objs, indent=4))


if __name__ == '__main__':

    write_order_to_json('товар', 'количество', 'цена', 'покупатель', 'дата')
