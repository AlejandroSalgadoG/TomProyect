from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import TemplateView

from TomAdmin.functions import get_bills_info

class Index(TemplateView):
    index_template = 'AdminIndex.html'

    def get(self, request):
        date_from, date_to = None, None

        if "date_from" in request.GET and request.GET["date_from"] != "":
            date_from = datetime.strptime(request.GET["date_from"], "%Y-%m-%d")


        if "date_to" in request.GET and request.GET["date_to"] != "":
            date_to = datetime.strptime(request.GET["date_to"], "%Y-%m-%d")

        bills = get_bills_info(date_from, date_to)
        data = {"bills": bills}

        return render(request, self.index_template, data)
