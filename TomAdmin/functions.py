from TomBill.models import Bill, Product

def get_bills_info():
    return [[bill, bill.product_set.all()] for bill in Bill.objects.all()]
