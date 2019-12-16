from datetime import datetime
from django.utils.timezone import now

from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

from TomAdmin.models import Expense
from TomAdmin.functions import get_bills_info, update_products, get_expenses_info
from TomBill.functions import get_db_products

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

        if date_from is None:
            date_from = now()

        if date_to is None:
            date_to = now()

        bills, n_bills, total_bills, cash_bills, tips = get_bills_info(date_from, date_to)
        expenses, n_expenses, total_expenses, cash_expenses = get_expenses_info(date_from, date_to)

        data = {"n_bills": n_bills,
                "total_bills": total_bills,
                "cash_bills": cash_bills,
                "tips": tips,
                "n_expenses": n_expenses,
                "total_expenses": total_expenses,
                "cash_expenses": cash_expenses,
                "card_expenses": total_expenses - cash_expenses}

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

        if date_from is None:
            date_from = now()

        if date_to is None:
            date_to = now()

        bills, _, _, _, _ = get_bills_info(date_from, date_to)

        return render(request, self.template, {"bills": bills})

class Expenses(TemplateView):
    template = 'Expenses.html'

    def get(self, request):
        date_from, date_to = None, None

        if "date_from" in request.GET and request.GET["date_from"] != "":
            date_from = datetime.strptime(request.GET["date_from"], "%Y-%m-%d")

        if "date_to" in request.GET and request.GET["date_to"] != "":
            date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")

        if date_from is None:
            date_from = now()

        if date_to is None:
            date_to = now()

        expenses = [ (expense, expense.date.date()) for expense in Expense.objects.filter(date__gte=date_from, date__lte=date_to)]

        data = {"expenses": expenses}

        return render(request, self.template, data)

    def post(self, request):
        date = request.POST["date"]
        description = request.POST["description"]
        price = request.POST["price"]
        cash = "cash" in request.POST
        
        Expense(date=date, description=description, price=price, cash=cash).save()

        return render(request, self.template, {})

class Products(TemplateView):
    template = 'Products.html'

    def get(self, request):
        double_sodas, sodas, additions, bakery, coffe = get_db_products()

        data = {"double_sodas": double_sodas, "sodas": sodas, 
                "additions": additions, "bakery": bakery, "coffe": coffe}

        return render(request, self.template, data)

    def post(self, request):
        update_products(request)
        return self.get(request)
        
class Inventary(TemplateView):
    template = 'Inventary.html'

    def get(self, request):
        return render(request, self.template, {})
