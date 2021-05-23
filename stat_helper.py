import numpy as np
import matplotlib.pyplot as plt
from db.repository import ProductsRepository

PR = ProductsRepository()

folder_path = 'outputs/'
markets = ['ekomarket', 'silpo', 'atb', 'marketopt', 'metro']

def get_name_of_product(name):
    product = PR.find_one({'name': name})
    return f"{product['name']} {product['type']}"

def get_prices_of_products(name, market):
    products = PR.find({'name': name, 'market': market})
    products_prices = []
    for product in products:
        products_prices.append(product['price'])
    return products_prices

def get_plot(prices, title, name):
    fig = plt.figure()
    plt.xlabel('Market')
    plt.ylabel('UAH')
    plt.title(title)
    plt.bar(markets, prices)
    fig.savefig(folder_path + name)

def describe_products(product):
    name_of_product = get_name_of_product(product)

    ekomarket = get_prices_of_products(product, 'ekomarket')
    av_price_ekomarket = np.mean(ekomarket)
    silpo = get_prices_of_products(product, 'silpo')
    av_price_silpo = np.mean(silpo)
    atb = get_prices_of_products(product, 'atb')
    av_price_atb = np.mean(atb)
    marketopt = get_prices_of_products(product, 'marketopt')
    av_price_marketopt = np.mean(marketopt)
    metro = get_prices_of_products(product, 'metro')
    av_price_metro = np.mean(metro)

    prices = [av_price_ekomarket, av_price_silpo, av_price_atb, av_price_marketopt, av_price_metro]
    title = f'Average prices - {name_of_product}'
    name = f'av_prices_{name_of_product}.png'
    get_plot(prices, title, name)

    min_market = markets[prices.index(min(prices))]
    max_market = markets[prices.index(max(prices))]
    print(f'Market {min_market} has the lowest prices on {name_of_product}. And {max_market} has the highest prices on {name_of_product}.')