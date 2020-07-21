class HTML:
    def __init__(self, output=None):
        self.output = output
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.output:
            with open(self.output, "w") as file:
                file.write(str(self))
        else:
            print(self)

    def __add__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        if self.children:
            internal = ""
            for child in self.children:
                internal += str(child)
            return "<html>\n{internal}\n</html>".format(internal=internal)
