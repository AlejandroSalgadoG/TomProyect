from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.utils.timezone import now

from django.views.decorators.csrf import csrf_exempt

from TomBill.functions import get_db_products
from TomBill.functions import get_products, calc_addition_price, register_bill
from TomBill.printer import type_bill, type_order, print_document

class Index(TemplateView):
    index_template = 'BillIndex.html'

    def get(self, request):
        double_sodas, sodas, additions, bakery, coffe = get_db_products()

        data = {"double_sodas": double_sodas, "sodas": sodas, 
                "additions": additions, "bakery": bakery, "coffe": coffe}

        return render(request, self.index_template, data)

@csrf_exempt
def save_bill(request):
    d_sodas = get_products(request.POST, section_name="Sodas Dobles")
    additions = get_products(request.POST, section_name="Adiciones")
    sodas = get_products(request.POST, section_name="Sodas")
    coffe = get_products(request.POST, section_name="Cafe")
    bakery = get_products(request.POST, section_name="Panaderia")
    additions_prod = calc_addition_price(additions, d_sodas, sodas)

    date = now()
    name = request.POST["client"]
    tip = "tip" in request.POST
    cash = "cash" in request.POST
    products = [d_sodas, sodas, coffe, bakery]

    bill = register_bill(date, name, products, additions_prod, tip, cash)

    #print_document( type_bill(bill) )
    #print_document( type_order(bill) )

    return redirect('/bill/')
