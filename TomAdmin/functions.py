from django.utils.timezone import now

from TomBill.models import Bill, Purchase, Section, Product

def get_bills_info(date_from, date_to):
    bills = []
    total, cash, tips = 0, 0, 0

    if date_from is None:
        date_from = now()

    if date_to is None:
        date_to = now()

    db_bills = Bill.objects.filter(date__gte=date_from, date__lte=date_to)

    for bill in db_bills:
        total += bill.total
        tips += bill.total - bill.subtotal

        if bill.cash:
            cash += bill.total

        bills.append([bill, bill.purchase_set.all()])

    return bills, len(bills), total, cash, tips

def update_products(request):
    html_ids = [key for key in request.POST if not key.startswith("short") and not key.startswith("price")]

    for html_id in html_ids:
        print(html_id)
        ids = html_id.split("_")
        html_section, html_product = ids[0], "_".join(ids[1:])
        product = Product.objects.get(html=html_product)
        product.name = request.POST[html_id]
        product.html = product.name.replace(" ", "_").replace("-", "_")
        product.short = request.POST["short_" + html_product]
        product.price = request.POST["price_" + html_product]
        product.section = Section.objects.get(html=html_section)
        product.save()

    return
