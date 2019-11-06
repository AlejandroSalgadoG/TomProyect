import pandas as pd
from datetime import datetime

from TomBill.products import *
from TomBill.models import Bill, Product

def register_bill(data):
    bill = Bill(date=datetime.now(), name=data["client"])
    bill.save()

    d_sodas_products   = get_products(data, double_sodas)
    sodas_products     = get_products(data, sodas)
    bakery_products    = get_products(data, bakery)
    coffe_products     = get_products(data, coffe)
    additions_products = get_products(data, additions)

    additions_products = calc_addition_price(additions_products)

    total  = register_products(d_sodas_products, bill)
    total += register_products(sodas_products, bill)
    total += register_products(bakery_products, bill)
    total += register_products(coffe_products, bill)
    total += register_products(additions_products, bill)

    bill.total = total
    bill.save()

def get_products(data, elements):
    products = []
    for id_name, name, price in elements:
        quantity = int( data[id_name] )
        if(quantity > 0):
            products.append([name, quantity, price])
    return products

def calc_addition_price(additions_products):
    additions = pd.DataFrame(additions_products, columns=["name", "quantity", "price"])

    split_additions = additions.loc[additions.index.repeat(additions['quantity'])].reset_index(drop=True)
    split_additions["quantity"] = 1

    if len(split_additions.index) <= 2:
        split_additions["price"] = 0
    else:
        split_additions.sort_values(by="price")
        last_two_idx = split_additions.iloc[[-1,-2]].index
        split_additions.at[last_two_idx,"price"] = 0

    additions = split_additions.groupby(by="name", as_index=False).sum()
    return additions.values

def register_products(products, bill):
    subtotal = 0

    if len(products) == 0:
        return subtotal

    for name, quantity, price in products:
        product = Product(name=name, price=price, quantity=quantity, bill=bill)
        product.save()
        subtotal += price * quantity 
    return subtotal
