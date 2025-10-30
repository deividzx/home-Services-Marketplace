import tkinter as tk
from tkinter import ttk, messagebox
from pessoa import Cliente, Prestador
from servico import Servico, ServicoEspecial
from pedido import Pedido
from repositorio import Repositorio




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("iFood de Serviços Domésticos 🏠")
        self.geometry("750x600")
        self.resizable(False, False)


        # Repositório e dados
        self.repositorio = Repositorio()
        self.clientes = []
        self.prestadores = []
        self.servicos = {
            1: Servico("Limpeza Residencial", 50),
            2: Servico("Lavagem de Roupas", 40),
            3: ServicoEspecial("Reparo Elétrico", 80),
            4: ServicoEspecial("Conserto Hidráulico", 70),
        }


        # Notebook (abas)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(fill="both", expand=True)


        self.frame_clientes = ttk.Frame(self.tabs)
        self.frame_prestadores = ttk.Frame(self.tabs)
        self.frame_pedidos = ttk.Frame(self.tabs)
        self.frame_servicos = ttk.Frame(self.tabs)


        self.tabs.add(self.frame_clientes, text="👤 Clientes")
        self.tabs.add(self.frame_prestadores, text="🔧 Prestadores")
        self.tabs.add(self.frame_servicos, text="🧾 Serviços")
        self.tabs.add(self.frame_pedidos, text="📦 Pedidos")


        # Criar as telas
        self.tela_clientes()
        self.tela_prestadores()
        self.tela_servicos()
        self.tela_pedidos()


    # ==============================
    # 🧍 CADASTRO DE CLIENTES
    # ==============================
    def tela_clientes(self):
        tk.Label(self.frame_clientes, text="Cadastro de Cliente", font=("Arial", 16, "bold")).pack(pady=10)


        form = ttk.Frame(self.frame_clientes)
        form.pack(pady=10)


        labels = ["Nome", "Email", "Telefone", "Endereço"]
        self.entry_cliente = {}
        for i, campo in enumerate(labels):
            ttk.Label(form, text=campo + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            e = ttk.Entry(form, width=40)
            e.grid(row=i, column=1)
            self.entry_cliente[campo] = e


        ttk.Button(self.frame_clientes, text="Cadastrar Cliente", command=self.cadastrar_cliente).pack(pady=10)


        self.lista_clientes = tk.Listbox(self.frame_clientes, width=60, height=10)
        self.lista_clientes.pack(pady=10)


    def cadastrar_cliente(self):
        nome = self.entry_cliente["Nome"].get()
        email = self.entry_cliente["Email"].get()
        telefone = self.entry_cliente["Telefone"].get()
        endereco = self.entry_cliente["Endereço"].get()


        if not nome or not email:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return


        cliente = Cliente(nome, email, telefone, endereco)
        self.clientes.append(cliente)
        self.repositorio.adicionar_cliente(cliente)
        self.lista_clientes.insert(tk.END, f"{cliente.nome} - {endereco}")
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")


        for e in self.entry_cliente.values():
            e.delete(0, tk.END)


    # ==============================
    # 🛠️ CADASTRO DE PRESTADORES
    # ==============================
    def tela_prestadores(self):
        tk.Label(self.frame_prestadores, text="Cadastro de Prestador", font=("Arial", 16, "bold")).pack(pady=10)


        form = ttk.Frame(self.frame_prestadores)
        form.pack(pady=10)


        labels = ["Nome", "Email", "Telefone", "Especialidade"]
        self.entry_prestador = {}
        for i, campo in enumerate(labels):
            ttk.Label(form, text=campo + ":").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            e = ttk.Entry(form, width=40)
            e.grid(row=i, column=1)
            self.entry_prestador[campo] = e


        ttk.Button(self.frame_prestadores, text="Cadastrar Prestador", command=self.cadastrar_prestador).pack(pady=10)


        self.lista_prestadores = tk.Listbox(self.frame_prestadores, width=60, height=10)
        self.lista_prestadores.pack(pady=10)


    def cadastrar_prestador(self):
        nome = self.entry_prestador["Nome"].get()
        email = self.entry_prestador["Email"].get()
        telefone = self.entry_prestador["Telefone"].get()
        especialidade = self.entry_prestador["Especialidade"].get()


        if not nome or not especialidade:
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return


        prestador = Prestador(nome, email, telefone, especialidade)
        self.prestadores.append(prestador)
        self.repositorio.adicionar_prestador(prestador)
        self.lista_prestadores.insert(tk.END, f"{prestador.nome} - {prestador._especialidade}")
        messagebox.showinfo("Sucesso", "Prestador cadastrado com sucesso!")


        for e in self.entry_prestador.values():
            e.delete(0, tk.END)


    # ==============================
    # 🧹 SERVIÇOS DISPONÍVEIS
    # ==============================
    def tela_servicos(self):
        tk.Label(self.frame_servicos, text="Serviços Disponíveis", font=("Arial", 16, "bold")).pack(pady=10)


        self.lista_servicos = tk.Listbox(self.frame_servicos, width=60, height=10)
        self.lista_servicos.pack(pady=10)


        for codigo, servico in self.servicos.items():
            self.lista_servicos.insert(tk.END, f"{codigo}. {servico.nome} - R$ {servico.preco_base}/h")


    # ==============================
    # 📦 PEDIDOS
    # ==============================
    def tela_pedidos(self):
        tk.Label(self.frame_pedidos, text="Gerenciar Pedidos", font=("Arial", 16, "bold")).pack(pady=10)


        form = ttk.Frame(self.frame_pedidos)
        form.pack(pady=10)


        ttk.Label(form, text="Cliente:").grid(row=0, column=0, sticky="e")
        self.cb_cliente = ttk.Combobox(form, width=35, state="readonly")
        self.cb_cliente.grid(row=0, column=1)


        ttk.Label(form, text="Prestador:").grid(row=1, column=0, sticky="e")
        self.cb_prestador = ttk.Combobox(form, width=35, state="readonly")
        self.cb_prestador.grid(row=1, column=1)


        ttk.Label(form, text="Serviço:").grid(row=2, column=0, sticky="e")
        self.cb_servico = ttk.Combobox(form, width=35, state="readonly",
                                       values=[f"{s.nome} - R${s.preco_base}/h" for s in self.servicos.values()])
        self.cb_servico.grid(row=2, column=1)


        ttk.Label(form, text="Horas estimadas:").grid(row=3, column=0, sticky="e")
        self.entry_horas = ttk.Entry(form, width=10)
        self.entry_horas.grid(row=3, column=1, sticky="w")


        ttk.Button(self.frame_pedidos, text="Criar Pedido", command=self.criar_pedido).pack(pady=5)


        self.lista_pedidos = tk.Listbox(self.frame_pedidos, width=80, height=15)
        self.lista_pedidos.pack(pady=10)


        ttk.Button(self.frame_pedidos, text="Atualizar Status", command=self.atualizar_status).pack(pady=5)


    def atualizar_comboboxes(self):
        self.cb_cliente["values"] = [c.nome for c in self.clientes]
        self.cb_prestador["values"] = [p.nome for p in self.prestadores]


    def criar_pedido(self):
        self.atualizar_comboboxes()
        if not self.cb_cliente.get() or not self.cb_prestador.get() or not self.cb_servico.get():
            messagebox.showwarning("Atenção", "Preencha todos os campos!")
            return


        try:
            horas = float(self.entry_horas.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido de horas.")
            return


        cliente = next(c for c in self.clientes if c.nome == self.cb_cliente.get())
        prestador = next(p for p in self.prestadores if p.nome == self.cb_prestador.get())
        servico_nome = self.cb_servico.get().split(" - ")[0]
        servico = next(s for s in self.servicos.values() if s.nome == servico_nome)


        pedido = Pedido(cliente, prestador, servico, horas)
        self.repositorio.adicionar_pedido(pedido)
        self.lista_pedidos.insert(tk.END, pedido.exibir_resumo())


        messagebox.showinfo("Sucesso", "Pedido criado com sucesso!")


    def atualizar_status(self):
        idx = self.lista_pedidos.curselection()
        if not idx:
            messagebox.showwarning("Atenção", "Selecione um pedido para atualizar.")
            return


        novo_status = tk.simpledialog.askstring("Atualizar Status", "Novo status (Ex: 'Em andamento', 'Concluído'):")
        if not novo_status:
            return


        pedido = self.repositorio.listar_pedidos()[idx[0]]
        pedido.atualizar_status(novo_status)
        self.lista_pedidos.delete(idx)
        self.lista_pedidos.insert(idx, pedido.exibir_resumo())
        messagebox.showinfo("Sucesso", "Status atualizado com sucesso!")




if __name__ == "__main__":
    app = App()
    app.mainloop()


