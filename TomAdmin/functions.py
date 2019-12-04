from datetime import datetime, date

from TomBill.models import Bill, Product

def get_bills_info(date_from, date_to):
    if date_from is None:
        return []

    if date_to is None:
        date_to = datetime.now()

    bills = Bill.objects.filter(date__gte=date_from, date__lte=date_to)
    return [[bill, bill.product_set.all()] for bill in bills]
