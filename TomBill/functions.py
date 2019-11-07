import pandas as pd

from TomBill.models import Bill, Product

def register_bill(date, name, products):
    bill = Bill(date=date, name=name)
    bill.save()

    d_sodas_prod, sodas_prod, bakery_prod, coffe_prod, additions_prod = products

    subtotal  = register_products(d_sodas_prod, bill)
    subtotal += register_products(sodas_prod, bill)
    subtotal += register_products(bakery_prod, bill)
    subtotal += register_products(coffe_prod, bill)
    subtotal += register_products(additions_prod, bill)

    bill.subtotal = subtotal
    bill.total = subtotal*1.1
    bill.save()

    return subtotal, total

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
