from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

from TomBill.products import *
from TomBill.functions import get_products, calc_addition_price, register_bill
from TomBill.printer import type_bill, type_order, print_document

class Index(TemplateView):
    index_template = 'BillIndex.html'

    def get(self, request):
        data = {"double_sodas": double_sodas, "sodas": sodas, 
                "additions": additions, "bakery": bakery, "coffe": coffe}
        return render(request, self.index_template, data)

@csrf_exempt
def save_bill(request):
    d_sodas_prod, n_d_sodas     = get_products(request.POST, double_sodas)
    sodas_prod, n_sodas         = get_products(request.POST, sodas)
    bakery_prod, n_bakery       = get_products(request.POST, bakery)
    coffe_prod, n_coffe         = get_products(request.POST, coffe)
    additions_tmp, n_additions = get_products(request.POST, additions)
    additions_prod = calc_addition_price(additions_tmp, n_d_sodas + n_sodas)

    date = datetime.now()
    name = request.POST["client"]
    products = [d_sodas_prod, sodas_prod, bakery_prod, coffe_prod, additions_prod]
    tip = "tip" in request.POST
    cash = "cash" in request.POST

    subtotal, total = register_bill(date, name, products, tip, cash)

    bill = type_bill(date, name, products, subtotal, total)
    order = type_order(date, name, products)
    print_document(bill)
    print_document(order)

    return redirect('/bill/')
