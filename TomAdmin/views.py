from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from TomBill.models import Bill, Product

class Index(TemplateView):
    index_template = 'AdminIndex.html'

    def get(self, request):
        return render(request, self.index_template, {})
