import win32ui

from TomBill.document import Document

def type_bill(bill):
    doc = Document()
    doc.write_title("Babol Soda")
    doc.write_title("Laura Salgado Gómez")
    doc.write_title("1053793226")
    doc.write_title("Régimen simplificado")
    doc.new_line()
    doc.write_info("Fecha: %s" % bill.date.strftime('%d/%m/%Y'))
    doc.write_info("Hora: %s" % bill.date.strftime('%I:%M:%S'))
    doc.write_info("cliente: %s" % bill.name)
    doc.new_line()

    for purchase in bill.purchase_set.all():
        doc.write_purchase(purchase)

    doc.new_line()
    doc.write_total("subtotal", "%d" % bill.subtotal)
    doc.write_total("total", "%d" % bill.total)
    return doc

def type_order(bill):
    doc = Document()
    doc.write_info("Hora: %s" % bill.date.strftime('%I:%M:%S'))
    doc.write_info("cliente: %s" % bill.name)

    for product in bill.purchase_set.all():
        doc.write_order(product)

    return doc

def print_document(document):
    dc = win32ui.CreateDC()
    dc.CreatePrinterDC()
    dc.StartDoc("Test.txt")
    dc.StartPage()

    document.print_document(dc)

    dc.EndPage()
    dc.EndDoc()
