mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

name_final = mobile_data.get('data')[2].get('name')
price = mobile_data.get('data')[2].get('price')
made= mobile_data.get('data')[2].get('made')

exchange_rate = mobile_data.get('exchnage_rate')
exchange_bdt = (exchange_rate*103)
# mobile data varaition are success

sentence = f'The {name_final} is made by {made}. The Price is {price}. Which is almost equal to {exchange_bdt} BDT' 
print(sentence)




