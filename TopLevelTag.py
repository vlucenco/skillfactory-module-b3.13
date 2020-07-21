class TopLevelTag:
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __add__(self, other):
        self.children.append(other)
        return self

    def __str__(self):
        if self.children:
            internal = ""
            for child in self.children:
                internal += "\t" + str(child) + "\n"
            return "\n<{tag}>\n{internal}</{tag}>\n".format(tag=self.tag, internal=internal)
        else:
            return "<{tag}></{tag}>\n".format(tag=self.tag)
