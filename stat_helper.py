import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime
from db.repositories.products_repository import products_repository
from db.repositories.old_prices_repository import old_prices_repository

folder_path = 'outputs/'
markets = ['ekomarket', 'silpo', 'atb', 'marketopt', 'metro']

def get_name_of_product(name):
    product = products_repository.find_one({'name': name})
    return f"{product['name']} {product['type']}"

def get_prices_of_products(name, market):
    products = products_repository.find({'name': name, 'market': market})
    products_prices = []
    for product in products:
        products_prices.append(product['price'])
    return products_prices

def get_average_plot(prices, title, name):
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
    get_average_plot(prices, title, name)

    min_market = markets[prices.index(min(prices))]
    max_market = markets[prices.index(max(prices))]
    print(f'Market {min_market} has the lowest prices on {name_of_product}. And {max_market} has the highest prices on {name_of_product}.')

def get_linear_regression(name, market, date=0, isPredict=False):
    products = products_repository.find({'name': name, 'market': market})
    old_prices = []
    dates = []
    prices = []

    for p in products:
        old_prices += old_prices_repository.find({'product_id': p['_id']})
        dates.append(p['date'])
        prices.append(p['price'])

    for op in old_prices:
        dates.append(op['date'])
        prices.append(op['price'])

    dates_to_number_values = list(map(lambda x: datetime.toordinal(datetime.strptime(x, '%Y-%m-%d')), dates))

    #
    slope, intercept, r, p, std_err = stats.linregress(dates_to_number_values, prices)
    def lin_regr(x):
        return slope * x + intercept
    model = list(map(lin_regr, dates_to_number_values))
    #

    if isPredict:
        answer = lin_regr(datetime.toordinal(datetime.strptime(date, '%Y-%m-%d')))
        print(f'Price on {date} will be {round(answer, 2)}.')

    fig = plt.figure()
    plt.ylabel('Price, uah')
    plt.xlabel('Date')
    plt.title(f'LR for {name} in {market}')
    plt.scatter(dates_to_number_values, prices)
    plt.plot(dates_to_number_values, model)
    fig.savefig(folder_path + f'LR_{name}_{market}.png')