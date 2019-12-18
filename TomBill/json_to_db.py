import json
from TomBill.models import Bill, Purchase, Product

with open("TomBill\database.json") as database_file:
    data = json.load(database_file)

    for key in data:
        json_bill = data[key]
        date = json_bill["date"]
        name = json_bill["name"]
        cash = json_bill["cash"]
        subtotal = json_bill["subtotal"]
        total = json_bill["total"]

        bill = Bill(date=date, name=name, cash=cash, subtotal=subtotal, total=total)
        bill.save()

        for json_product in json_bill["products"]:
            quantity = json_product["quantity"]
            product = Product.objects.get(name=json_product["name"])
            free = json_product["price"] == 0

            Purchase(quantity=quantity, free=free, product=product, bill=bill).save()
