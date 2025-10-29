class Servico:
    """Classe representando um serviço disponível"""
    def __init__(self, nome, preco_base):
        self._nome = nome
        self._preco_base = preco_base


    @property
    def nome(self):
        return self._nome


    @property
    def preco_base(self):
        return self._preco_base


    def calcular_preco(self, horas):
        """Pode ser sobrescrito para diferentes cálculos de preço"""
        return self._preco_base * horas




class ServicoEspecial(Servico):
    """Polimorfismo: cálculo de preço especial com taxa adicional"""
    def calcular_preco(self, horas):
        taxa_extra = 1.2
        return self._preco_base * horas * taxa_extra