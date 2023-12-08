
import copy

# Classe Document - Classe a ser clonada
class Document:
    def __init__(self, content):
        self.content = content

    def clone(self):
        # Usando a biblioteca copy para criar uma cópia profunda do objeto
        return copy.deepcopy(self)

# Cliente
if __name__ == "__main__":
    # Cria um documento original
    original_document = Document("Conteúdo original do documento.")

    # Clona o documento original
    cloned_document = original_document.clone()

    # Modifica o conteúdo do documento clonado
    cloned_document.content += " Conteúdo adicionado no documento clonado."

    # Exibe os conteúdos dos dois documentos
    print("Documento Original:", original_document.content)
    print("Documento Clonado:", cloned_document.content)
