from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import TemplateView

from TomAdmin.functions import get_bills_info

class Index(TemplateView):
    template = 'AdminIndex.html'

    def get(self, request):
        return render(request, self.template, {})

class Accounting(TemplateView):
    template = 'Accounting.html'

    def get(self, request):
        date_from, date_to = None, None

        if "date_from" in request.GET and request.GET["date_from"] != "":
            date_from = datetime.strptime(request.GET["date_from"], "%Y-%m-%d")

        if "date_to" in request.GET and request.GET["date_to"] != "":
            date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")

        bills, n_bills, total, cash, tips, = get_bills_info(date_from, date_to)

        data = {"n_bills": n_bills,
                "total": total,
                "cash": cash,
                "tips": tips}

        return render(request, self.template, data)

    def post(self, request):
        return render(request, self.template, {})

class Records(TemplateView):
    template = 'Records.html'

    def get(self, request):
        date_from, date_to = None, None

        if "date_from" in request.GET and request.GET["date_from"] != "":
            date_from = datetime.strptime(request.GET["date_from"], "%Y-%m-%d")


        if "date_to" in request.GET and request.GET["date_to"] != "":
            date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")

        bills, _, _, _, _ = get_bills_info(date_from, date_to)

        return render(request, self.template, {"bills": bills})

class Products(TemplateView):
    template = 'Products.html'

    def get(self, request):
        return render(request, self.template, {})

class Inventary(TemplateView):
    template = 'Inventary.html'

    def get(self, request):
        return render(request, self.template, {})
