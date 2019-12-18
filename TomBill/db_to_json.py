import json
from TomBill.models import Bill

bills = {}

for number, bill in enumerate(Bill.objects.all()):
    bills[number] = { "date": bill.date.strftime("%Y-%m-%-%d"),
                      "name": bill.name,
                      "cash": bill.cash,
                      "subtotal": bill.subtotal,
                      "total": bill.total,
                      "products": [] }

    for product in bill.product_set.all():
        bills[number]["products"].append({ "name": product.name, 
                                           "price": product.price,
                                           "quantity": product.quantity })

with open("TomBill\database.json", 'w') as database_file:
    json.dump(bills, database_file)
