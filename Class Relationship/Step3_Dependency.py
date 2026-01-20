# doc->Document("Hello Dependency"), printer have never saved document 
# the lifecycle of document is irrelevant with printer
class Document:
    def __init__(self, content):
        self.content = content
    
    def get_content(self):
        return self.content
    
    def __repr__(self):
        return f"Document(content={self.content})"

class Printer:
    def print_document(self, document:Document):
        print("Printing:", document.get_content())

doc = Document("Hello Dependency")
printer = Printer()
printer.print_document(doc)

del printer
print(doc)