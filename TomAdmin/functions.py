from django.utils.timezone import now

from TomAdmin.models import Expense, Inventory
from TomBill.models import Bill, Purchase, Section, Product

def get_bills_info(date_from, date_to):
    bills = []
    total, cash, tips = 0, 0, 0

    db_bills = Bill.objects.filter(date__gte=date_from, date__lte=date_to)

    for bill in db_bills:
        total += bill.total
        tips += bill.total - bill.subtotal

        if bill.cash:
            cash += bill.total

        bills.append([bill, bill.purchase_set.all()])

    return bills, len(bills), total, cash, tips

def get_section_and_product(html_id):
    ids = html_id.split("_")
    return ids[0], "_".join(ids[1:])

def update_products(data):
    products = Product.objects.all()
    html_ids = [key for key in data if not key.startswith("short") and not key.startswith("price")]
         
    for product in products:
        founded = False
        for html_id in html_ids:
            html_section, html_product = get_section_and_product(html_id)
            if product.html == html_product:
                update_product(product, html_id, data)
                html_ids.remove(html_id)
                founded = True

    for html_id in html_ids:
        update_product(Product(), html_id, data)

def update_product(product, html_id, data):
    html_section, html_product = get_section_and_product(html_id)
    product.name = data[html_id]
    product.html = product.name.replace(" ", "_").replace("-", "_")
    product.short = data["short_" + html_product]
    product.price = data["price_" + html_product]
    product.section = Section.objects.get(html=html_section)
    product.save()

def get_expenses_info(date_from, date_to):
    expenses = []
    total, cash = 0, 0

    db_expenses = Expense.objects.filter(date__gte=date_from, date__lte=date_to)

    for expense in db_expenses:
        total += expense.price

        if expense.cash:
            cash += expense.price

        expenses.append(expense)

    return expenses, len(expenses), total, cash

def update_inventory(element, name, data):
    element.name = data[name]
    element.quantity = data["quantity_" + name]
    element.save()

def update_inventories(data):
    elements = Inventory.objects.all()
    names = [key for key in data if not key.startswith("quantity")]
         
    for element in elements:
        founded = False
        for name in names:
            if element.name == name:
                update_inventory(element, name, data)
                names.remove(name)
                founded = True

    for name in names:
        update_inventory(Inventory(), name, data)
