from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView

from django.views.decorators.csrf import csrf_exempt

class Index(TemplateView):
    index_template = 'Index.html'

    sodas = [ ("kiwwi_menta", "Kiwwi-menta", 6500),
              ("limonada_coco", "Limonada de coco", 6500),
              ("menta_marac", "Menta-maracuyá", 6500),
              ("sandia_hierb", "Sandia-hierbabuena", 6500),
              ("mango_duraz", "Mango-durazno", 6500),
              ("sandia_pepin", "Sandia-pepino", 6500),
              ("mango_lyme", "Mango-lyme habanero", 6500),
              ("lychee_menta", "Lychee-menta", 6500),
              ("durazno", "Durazno", 6000),
              ("pepino", "Pepino", 6000),
              ("manzana_verde", "Manzana verde", 6000),
              ("coco", "Coco", 6000),
              ("mango", "Mango", 6000),
              ("fresa", "Fresa", 6000),
              ("sandia", "Sandia", 6000),
              ("mora_azul", "Mora azul", 6000),
              ("menta", "Menta", 6000),
              ("lychee", "Lychee", 6000),
              ("lyme_haban", "Lyme habanero", 6000),
              ("maracuya", "Maracuyá", 6000),
              ("amarena", "Amarena", 6000),
              ("kiwwi", "Kiwwi", 6000) ]

    additions = [ ("lychee", "Lychee", 800),
                  ("durazno", "Durazno", 800),
                  ("mix_fruto", "Mix frutos rojos", 800),
                  ("mango", "Mango", 500),
                  ("fresa", "Fresa", 500),
                  ("maracuya", "Maracuya", 500),
                  ("coco", "Coco", 500),
                  ("cereza", "Cereza", 500),
                  ("explosion", "explosion", 800),
                  ("jelly_arco", "jelly arcoiris", 800) ]

    bakery = [ ("pastel_pollo", "Pastel de pollo", 3800),
               ("pastel_carne", "Pastel carne", 3800),
               ("croissant_queso", "Croissant queso", 3000),
               ("croissant_peppe", "Croissant pepperoni mozzarella y oregano", 3800),
               ("croissant_pesto", "Croissant pesto y cebolla caramelizada", 4000),
               ("rollo_espin", "Rollo de Espinaca", 3600),
               ("palito_queso", "Palito 3 quesos", 3800),
               ("palito_super", "Palito super perro", 4600),
               ("rollo_canel", "Rollo de canela", 3000),
               ("rollo_nutel", "Rollo de nutella", 3000) ]

    coffe = [ ("capuchino", "capuchino", 60000),
              ("expresso", "expresso", 100000),
              ("cafe_ameri", "café americano", 200000),
              ("mocaccino", "mocaccino", 1234578),
              ("chocolate", "chocolate", 400000),
              ("chocolate_leche", "chocolate en leche", 500000) ]


    def get(self, request):
        data = {"sodas": self.sodas, "bakery": self.bakery, "coffe": self.coffe}
        return render(request, self.index_template, data)

@csrf_exempt
def save_bill(request):
    print(request.POST)
    return redirect('/bill/')
