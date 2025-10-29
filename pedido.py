class Pedido:
    """Classe que representa o pedido de um cliente para um prestador"""
    def __init__(self, cliente, prestador, servico, horas):
        self._cliente = cliente
        self._prestador = prestador
        self._servico = servico
        self._horas = horas
        self._status = "Pendente"


    @property
    def status(self):
        return self._status


    def calcular_valor_total(self):
        return self._servico.calcular_preco(self._horas)


    def atualizar_status(self, novo_status):
        self._status = novo_status


    def exibir_resumo(self):
        return (f"Pedido: {self._servico.nome} - Cliente: {self._cliente.nome} - "
                f"Prestador: {self._prestador.nome} - "
                f"Total: R${self.calcular_valor_total():.2f} - Status: {self._status}")