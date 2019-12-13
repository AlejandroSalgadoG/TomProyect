from TomBill.models import Section, Product

d_soda = Section(name="Sodas Dobles")
soda = Section(name="Sodas")
addition = Section(name="Adiciones")
bakery = Section(name="Panaderia")
coffe = Section(name="Cafe")

d_soda.save()
soda.save()
addition.save()
bakery.save()
coffe.save()

Product(section=d_soda, html="Kiwwi_menta",                    short="Kiwwi-menta", name="Kiwwi-menta",                    price=7000).save() 
Product(section=d_soda, html="Amarena_menta",                  short="Ama menta",   name="Amarena menta",                  price=7000).save()
Product(section=d_soda, html="Maracuya_coco",                  short="Mara coco",   name="Maracuya coco",                  price=7000).save()
Product(section=d_soda, html="Frutos_rojos_limon_habanero",    short="Fruto rojos", name="Frutos rojos limon habanero",    price=7000).save()
Product(section=d_soda, html="Sandia_pepino",                  short="Sandia pep",  name="Sandia pepino",                  price=7000).save()
Product(section=d_soda, html="Lychee_coco",                    short="Lychee coco", name="Lychee coco",                    price=7000).save()
Product(section=d_soda, html="Limon_habanero_y_mango",         short="Limo haban",  name="Limon habanero y mango",         price=7000).save()
Product(section=d_soda, html="Mango_durazno",                  short="Mango dur",   name="Mango-durazno",                  price=7000).save()
Product(section=d_soda, html="Sandia_limon_habanero",          short="Sand limi",   name="Sandia limon habanero",          price=7000).save()
Product(section=d_soda, html="Limonada_de_coco",               short="Limo coco",   name="Limonada de coco",               price=7000).save()
Product(section=d_soda, html="Manzana_verde_y_limon_habanero", short="Manzan lim",  name="Manzana verde y limon habanero", price=7000).save()
Product(section=d_soda, html="Personalizada",                  short="Personal",    name="Personalizada",                  price=7000).save() 

Product(section=soda, html="Durazno",       short="Durazno",    name="Durazno",       price=6500).save()
Product(section=soda, html="Pepino",        short="Pepino",     name="Pepino",        price=6500).save()
Product(section=soda, html="Manzana verde", short="Manzana",    name="Manzana verde", price=6500).save()
Product(section=soda, html="Coco",          short="Coco",       name="Coco",          price=6500).save()
Product(section=soda, html="Mango",         short="Mango",      name="Mango",         price=6500).save()
Product(section=soda, html="Fresa",         short="Fresa",      name="Fresa",         price=6500).save()
Product(section=soda, html="Sandia",        short="Sandia",     name="Sandia",        price=6500).save()
Product(section=soda, html="Mora_azul",     short="Mora azul",  name="Mora azul",     price=6500).save()
Product(section=soda, html="Menta",         short="Menta",      name="Menta",         price=6500).save()
Product(section=soda, html="Lychee",        short="Lychee",     name="Lychee",        price=6500).save()
Product(section=soda, html="Lyme_habanero", short="Lyme haban", name="Lyme habanero", price=6500).save()
Product(section=soda, html="Maracuya",      short="Maracuya",   name="Maracuya",      price=6500).save()
Product(section=soda, html="Amarena",       short="Amarena",    name="Amarena",       price=6500).save()
Product(section=soda, html="Kiwwi",         short="Kiwwi",      name="Kiwwi",         price=6500).save()
Product(section=soda, html="Tradicional",   short="Tradicion",  name="Tradicional",   price=5000).save()

Product(section=addition, html="Adicion_lychee",           short="Ad Lychee",     name="Adicion lychee",           price=800).save()
Product(section=addition, html="Adicion_durazno",          short="Ad Durazno",    name="Adicion durazno",          price=800).save()
Product(section=addition, html="Adicion_mix_frutos_rojos", short="Ad Mix frutos", name="Adicion mix frutos rojos", price=800).save()
Product(section=addition, html="Adicion_mango",            short="Ad Mango",      name="Adicion mango",            price=500).save()
Product(section=addition, html="Adicion_fresa",            short="Ad Fresa",      name="Adicion fresa",            price=500).save()
Product(section=addition, html="Adicion_maracuya",         short="Ad Maracuya",   name="Adicion maracuya",         price=500).save()
Product(section=addition, html="Adicion_coco",             short="Ad Coco",       name="Adicion coco",             price=500).save()
Product(section=addition, html="Adicion_cereza",           short="Ad Cereza",     name="Adicion cereza",           price=500).save()
Product(section=addition, html="Adicion_explosion",        short="Ad Explosion",  name="Adicion explosion",        price=800).save()
Product(section=addition, html="Adicion_jelly_arcoiris",   short="Ad Jelly",      name="Adicion jelly arcoiris",   price=800).save()

Product(section=bakery, html="Palito_de_queso",                     short="P queso",   name="Palito de queso",                     price=3000).save()
Product(section=bakery, html="Pastel_de_pollo",                     short="P Pollo",   name="Pastel de pollo",                     price=4500).save()
Product(section=bakery, html="Pastel_carne_y_cebolla_caramelizada", short="P Carne",   name="Pastel carne y cebolla caramelizada", price=4500).save()
Product(section=bakery, html="Pastel_de_espinaca_y_champinones",    short="P espin",   name="Pastel de espinaca y champinones",    price=4500).save()
Product(section=bakery, html="Croissant_de_chocolate",              short="C choco",   name="Croissant de chocolate",              price=4500).save()
Product(section=bakery, html="Croissant_de queso",                  short="C queso",   name="Croissant de queso",                  price=4000).save()
Product(section=bakery, html="Muffin_de_banano",                    short="M banano",  name="Muffin de banano",                    price=3000).save()
Product(section=bakery, html="Muffin_de_queso",                     short="M queso",   name="Muffin de queso",                     price=4500).save()
Product(section=bakery, html="Muffin_de_manzana_y_nuez",            short="M manzana", name="Muffin de manzana y nuez",            price=4000).save()

Product(section=coffe, html="Americano",          short="Americ",      name="Americano",          price=2500).save()
Product(section=coffe, html="Expresso",           short="Expres",      name="Expresso",           price=3500).save()
Product(section=coffe, html="Mochaccino",         short="Moch",        name="Mochaccino",         price=5000).save()
Product(section=coffe, html="Capuchino",          short="Capuc",       name="Capuchino",          price=5000).save()
Product(section=coffe, html="Chocolate",          short="Choco",       name="Chocolate",          price=3500).save()
Product(section=coffe, html="chocolate_en_leche", short="Choco leche", name="chocolate en leche", price=4500).save()
Product(section=coffe, html="Aromatica_en_leche", short="Aro leche",   name="Aromatica en leche", price=4000).save()
Product(section=coffe, html="Aromatica_en_agua",  short="Aro agua",    name="Aromatica en agua",  price=3000).save()
