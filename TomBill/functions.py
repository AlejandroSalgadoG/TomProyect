from datetime import datetime

from TomBill.products import *
from TomBill.models import Bill, Product

def register_bill(data):
    bill = Bill(date=datetime.now())
    bill.save()

    total  = register_products(data, sodas, bill)
    total += register_products(data, bakery, bill)
    total += register_products(data, coffe, bill)

    bill.total = total
    bill.save()

def register_products(data, elements, bill):
    subtotal = 0
    for id_name, name, price in elements:
        quantity = int( data[id_name] )
        if(quantity > 0):
            product = Product(name=name, price=price, quantity=quantity, bill=bill)
            product.save()
            subtotal += price * quantity 
    return subtotal
