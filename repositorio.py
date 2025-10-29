class Repositorio:
    """Simula persistência em memória"""
    def __init__(self):
        self._clientes = []
        self._prestadores = []
        self._pedidos = []


    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)


    def adicionar_prestador(self, prestador):
        self._prestadores.append(prestador)


    def adicionar_pedido(self, pedido):
        self._pedidos.append(pedido)


    def listar_pedidos(self):
        return self._pedidos


    def listar_prestadores(self):
        return self._prestadores
