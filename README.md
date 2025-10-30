# 🏠 iFood de Serviços Domésticos

## 💡 Sobre o Projeto

O "iFood de Serviços Domésticos" é um sistema que simula uma plataforma de *marketplace* para conectar clientes que precisam de serviços domésticos (limpeza, reparos elétricos, hidráulicos, etc.) a prestadores de serviços especializados.

Este projeto foi desenvolvido em **Python**, aplicando os princípios da **Programação Orientada a Objetos (POO)** e utilizando a biblioteca **Flet** para fornecer uma **Interface Gráfica de Usuário (GUI)** multi-plataforma (desktop/web), substituindo o antigo menu de console.

## 📐 Arquitetura e Princípios de POO

O sistema é modular, com separação clara de responsabilidades:

### Princípios de POO Aplicados:

* **Abstração e Herança:** A classe base **`Pessoa`** define o comportamento fundamental, enquanto **`Cliente`** e **`Prestador`** herdam e especializam suas funcionalidades.
* **Polimorfismo:** A classe **`Servico`** tem o método `calcular_preco(horas)`, que é sobrescrito pela classe **`ServicoEspecial`** para adicionar uma taxa extra, demonstrando comportamentos distintos para o mesmo método.
* **Encapsulamento:** O acesso às variáveis internas das classes (`_nome`, `_status`) é controlado por *getters* e *setters* (propriedades).

### Separação de Responsabilidades (Estrutura de Arquivos):

| Arquivo | Responsabilidade | Funções/Classes Chave |
| :--- | :--- | :--- |
| **`gui_app.py`** | **Interface (GUI) e Orquestração.** Gerencia a exibição e interage com os métodos de negócio. | `main()`, `atualizar_lista_pedidos()` |
| **`pessoa.py`** | **Entidades Principais (Usuários).** Classes `Pessoa` (Abstrata), `Cliente` e `Prestador`. | `Cliente`, `Prestador` |
| **`servico.py`** | **Entidades de Serviço.** Classes `Servico` e `ServicoEspecial` (Polimorfismo). | `Servico`, `ServicoEspecial` |
| **`pedido.py`** | **Entidade de Pedido.** Lógica de cálculo de valor total e atualização de status. | `Pedido` |
| **`repositorio.py`** | **Persistência de Dados.** Simula o banco de dados armazenando objetos em listas em memória. | `Repositorio` |

## ⚙️ Funcionalidades Implementadas

O projeto implementa os principais Casos de Uso do sistema através das abas da interface:

* **1. Cadastrar Usuário:** Permite o cadastro de novos Clientes e Prestadores.
* **2. Fazer Pedido:** Seleção de Cliente, Prestador, Serviço e horas estimadas, resultando na criação de um `Pedido`.
* **3. Listar Pedidos:** Exibe todos os pedidos criados e seu status atual.
* **4. Atualizar Status:** Permite que o status de um pedido existente seja alterado (Ex: de 'Pendente' para 'Concluído').

## 🚀 Como Executar o Projeto

Siga os passos abaixo para clonar e rodar a aplicação:

### 1. Requisitos

Certifique-se de ter o **Python 3.x** instalado.

### 2. Clonar o Repositório

```bash
