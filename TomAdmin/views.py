from django.shortcuts import render
from django.views.generic import TemplateView

from TomAdmin.functions import get_bills_info

class Index(TemplateView):
    index_template = 'AdminIndex.html'

    def get(self, request):
        bills = get_bills_info()
        data = {"bills": bills}

        return render(request, self.index_template, data)
