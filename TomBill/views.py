from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

from TomBill.products import *
from TomBill.functions import register_bill

class Index(TemplateView):
    index_template = 'Index.html'

    def get(self, request):
        data = {"sodas": sodas, "bakery": bakery, "coffe": coffe}
        return render(request, self.index_template, data)

@csrf_exempt
def save_bill(request):
    register_bill(request.POST)
    return redirect('/bill/')
