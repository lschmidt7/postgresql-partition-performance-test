from random import uniform

class LeituraDados:

    def __init__(self):
        pass

    def mount(self, chave, leitura_id) -> str:
        valor = uniform(0,100)
        return f"({chave},{valor},{leitura_id})"