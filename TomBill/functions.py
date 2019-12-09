import pandas as pd

from TomBill.models import Bill, Purchase, Section

def get_db_products():
    double_sodas = Section.objects.get(name="Sodas Dobles").product_set.all()
    sodas = Section.objects.get(name="Sodas").product_set.all()
    additions = Section.objects.get(name="Adiciones").product_set.all()
    bakery = Section.objects.get(name="Panaderia").product_set.all()
    coffe = Section.objects.get(name="Cafe").product_set.all()

    return double_sodas, sodas, additions, bakery, coffe

def get_products(data, section_name):
    products = []
    section = Section.objects.get(name=section_name)
    for product in section.product_set.all():
        quantity = int( data[product.html] )
        if quantity > 0:
            products.append( (product, quantity) )
    return products

def calc_addition_price(additions, d_sodas, sodas):
    n_sodas = sum( [quantity for product, quantity in d_sodas] + [quantity for product, quantity in sodas] )

    additions_data = [ (addition, quantity, addition.price) for addition, quantity in additions ]
    addition_products = pd.DataFrame(additions_data, columns=["product", "quantity", "price"])
    split_additions = addition_products.loc[addition_products.index.repeat(addition_products['quantity'])].reset_index(drop=True)
    split_additions = split_additions.sort_values(by="price")
    split_additions["quantity"] = 1

    if len(split_additions.index) <= 2*n_sodas:
        split_additions["price"] = 0
    else:
        last_idx = split_additions.head(2*n_sodas).index
        split_additions.at[last_idx,"price"] = 0

    additions = split_additions.groupby(by=["product", "price"], as_index=False, sort=False).sum()

    return additions.values

def register_bill(date, name, products, additions, tip, cash):
    bill = Bill(date=date, name=name, cash=cash)
    bill.save()

    d_sodas, sodas, coffe, bakery = products

    subtotal  = register_products(d_sodas, bill)
    subtotal += register_products(sodas, bill)
    subtotal += register_products(bakery, bill)
    subtotal += register_products(coffe, bill)
    subtotal += register_additions(additions, bill)

    bill.subtotal = subtotal
    bill.total = subtotal

    if tip:
        bill.total *= 1.1
    bill.save()

    return bill

def register_products(products, bill):
    subtotal = 0
    if len(products) == 0:
        return subtotal

    for product, quantity in products:
        purchase = Purchase(quantity=quantity, product=product, bill=bill)
        purchase.save()
        subtotal += product.price * quantity 
    return subtotal

def register_additions(additions, bill):
    subtotal = 0
    if len(additions) == 0:
        return subtotal

    for product, price, quantity in additions:
        if price == 0:
            purchase = Purchase(quantity=quantity, product=product, bill=bill, free=True)
        else:
            purchase = Purchase(quantity=quantity, product=product, bill=bill)
            subtotal += price * quantity 
        purchase.save()
    return subtotal
