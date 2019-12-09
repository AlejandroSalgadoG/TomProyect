from django.utils.timezone import now

from TomBill.models import Bill, Purchase

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
