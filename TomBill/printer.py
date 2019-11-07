import win32ui

from TomBill.document import Document

def type_document(date, name, products, subtotal, total):
    doc = Document()
    doc.write_title("Babol Soda")
    doc.write_title("Laura Salgado Gómez")
    doc.write_title("1053793226")
    doc.write_title("Régimen simplificado")
    doc.new_line()
    doc.write_info("Fecha: %s" % date.strftime('%d/%m/%Y'))
    doc.write_info("Hora: %s" % date.strftime('%I:%M:%S'))
    doc.write_info("cliente: %s" % name)
    doc.new_line()

    for type_product in products:
        for product in type_product:
            doc.write_purchase(product)

    doc.new_line()
    doc.write_total("subtotal", "%d" % subtotal)
    doc.write_total("total", "%d" % total)
    return doc

def print_document(document):
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC()
    dc.StartDoc("Test.txt")
    dc.StartPage()

    document.print_document(dc)

    dc.EndPage()
    dc.EndDoc()
