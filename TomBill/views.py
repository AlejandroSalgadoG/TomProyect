from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

class Index(TemplateView):
    index_template = 'Index.html'

    def get(self, request):
        return render(request, self.index_template)
