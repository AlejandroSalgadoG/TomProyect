line_size = 350
line_width = 35
letter_size = 15

class Line:
    def __init__(self, number):
        self.number = number
        self.content = [None]*line_size
        self.actions = []

    def left(self, text):
        if self.is_available(0, len(text)*letter_size):
            self.assign_text(0, text)
            return True
        return False

    def right(self, text):
        space = len(text)*letter_size
        if self.is_available(line_size - space, space):
            self.assign_text(line_size - space, text)
            return True
        return False

    def middle(self, text): 
        space = len(text)*letter_size
        empty = [i for i in range(line_size) if self.content[i] is None]
        n_empty = len(empty)

        if n_empty < space:
            return False

        relative_start = int( (n_empty-space) / 2 )

        if self.is_available(empty[0] + relative_start, space):
            self.assign_text(empty[0] + relative_start, text)
            return True
        return False

    def is_available(self, start, space):
        if start+space > line_size:
            return False

        if all(x is None for x in self.content[start:start+space]):
            return True
        else:
            return False

    def assign_text(self, start, text):
        self.actions.append((start, self.number*line_width, text))
        for letter in text:
            for i in range(start,start+letter_size):
                self.content[i] = letter 
            start += letter_size

    def write_line(self, dc):
        for px, py, text in self.actions:
            dc.TextOut(px, py, text)

class Document:
    def __init__(self):
        self.lines = []
        self.n_line = 0

    def write_title(self, text):
        line = Line(self.n_line)
        line.middle(text)
        self.lines.append(line)
        self.new_line()

    def write_info(self, text):
        line = Line(self.n_line)
        line.left(text)
        self.lines.append(line)
        self.new_line()

    def write_purchase(self, purchase):
        product, quantity, price = purchase
        line = Line(self.n_line)
        line.left(product)
        line.right("%d" % price)
        line.middle("%d" % quantity)
        self.lines.append(line)
        self.new_line()

    def write_total(self, name, price):
        line = Line(self.n_line)
        line.left(name)
        line.right(price)
        self.lines.append(line)
        self.new_line()

    def write_order(self, purchase):
        product, quantity, price = purchase
        line = Line(self.n_line)
        line.left(product)
        line.right("%d" % quantity)
        self.lines.append(line)
        self.new_line()

    def new_line(self):
        self.n_line += 1
        
    def print_document(self, dc):
        for line in self.lines:
            line.write_line(dc)
