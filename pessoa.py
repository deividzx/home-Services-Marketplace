from abc import ABC, abstractmethod


class Pessoa(ABC):
    """Classe abstrata representando uma pessoa no sistema"""
    def __init__(self, nome, email, telefone):
        self._nome = nome
        self._email = email
        self._telefone = telefone


    # Encapsulamento: uso de getters e setters
    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome


    @abstractmethod
    def exibir_informacoes(self):
        pass




class Cliente(Pessoa):
    """Cliente que solicita serviços"""
    def __init__(self, nome, email, telefone, endereco):
        super().__init__(nome, email, telefone)
        self._endereco = endereco


    def exibir_informacoes(self):
        return f"Cliente: {self._nome}, Endereço: {self._endereco}"




class Prestador(Pessoa):
    """Prestador que oferece serviços"""
    def __init__(self, nome, email, telefone, especialidade, avaliacao=0):
        super().__init__(nome, email, telefone)
        self._especialidade = especialidade
        self._avaliacao = avaliacao


    def exibir_informacoes(self):
        return f"Prestador: {self._nome} ({self._especialidade}) - Avaliação: {self._avaliacao}/5"
