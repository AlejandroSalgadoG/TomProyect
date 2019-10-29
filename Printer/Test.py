import win32ui
from datetime import datetime

class Printer:
    def __init__(self):
        self.line = 0
        self.px = 15
        self.py = 35
        self.total_p = 350

    def print_bill(self, client, products):
        dc = win32ui.CreateDC()
        dc.CreatePrinterDC()
        dc.StartDoc("Test.txt")

        dc.StartPage()

        self.write_centered(dc, "BabolSoda")
        self.write_centered(dc, "Laura Salgado Gómez")
        self.write_centered(dc, "1053793226")
        self.write_centered(dc, "Régimen simplificado")

        self.newline()

        date = datetime.now().strftime('%d/%m/%Y')
        hour = datetime.now().strftime('%I:%M:%S')

        self.write_left(dc, "Fecha: %s" % date)
        self.write_left(dc, "Hora: %s" % hour)
        self.write_left(dc, "Cliente: %s" % client)

        self.newline()

        self.write_left(dc, "Café", newline=False)
        self.write_centered(dc, "1", newline=False)
        self.write_right(dc, "3000")

        self.newline()

        self.write_left(dc, "Subtotal", newline=False)
        self.write_right(dc, "3000")

        self.write_left(dc, "Total", newline=False)
        self.write_right(dc, "3300")

        dc.EndPage()

        dc.EndDoc()

    def count_letters(self, msg):
        return len(msg) - msg.count("i")

    def write_centered(self, dc, msg, newline=True):
        n_letters = self.count_letters(msg)
        x_centered = int(self.total_p/2) - int(n_letters/2)*self.px
        dc.TextOut(x_centered, self.line*self.py ,msg)
        if newline:
            self.newline()

    def write_left(self, dc, msg, newline=True):
        dc.TextOut(0, self.line*self.py, msg)
        if newline:
            self.newline()

    def write_right(self, dc, msg):
        n_letters = self.count_letters(msg)
        x_right = self.total_p - n_letters*self.px
        dc.TextOut(x_right , self.line*self.py, msg)
        self.newline()

    def newline(self):
        self.line += 1

printer = Printer()
printer.print_bill("Alejandro", [])
