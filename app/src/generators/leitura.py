
class Leitura:

    def __init__(self):
        self.segundo = 0
        self.minuto = 0
        self.hora = 0
        self.dia = 1
        self.mes = 1
        self.ano = 2025
    
    def incrase(self):
        self.segundo += 30
        
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
        
        if self.minuto >= 60:
            self.segundo = 0
            self.minuto = 0
            self.hora += 1
        
        if self.hora >= 24:
            self.segundo = 0
            self.minuto = 0
            self.hora = 0
            self.dia += 1
        
        if self.dia >= 28:
            self.segundo = 0
            self.minuto = 0
            self.hora = 0
            self.dia = 1
            self.mes += 1
        
        if self.mes > 12:
            self.segundo = 0
            self.minuto = 0
            self.hora = 0
            self.dia = 1
            self.mes = 1
            self.ano += 1
    
    def mount(self) -> str:
        return f"('{str(self.ano)}-{str(self.mes).zfill(2)}-{str(self.dia).zfill(2)} {str(self.hora).zfill(2)}:{str(self.minuto).zfill(2)}:{str(self.segundo).zfill(2)}')"