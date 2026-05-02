from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showwarning

import produto
from carrinho import Carrinho
from mercado import Mercado


def criar_interface(mercado,carrinho):
    window = Tk()
    window.title("Senna's Market")
    icon = PhotoImage(file="carrinhoicon.png")
    window.iconphoto(True,icon)
    text = Text(window)
    text.pack()
    entry = Entry(window)
    entry_id = Entry(window)
    # entry_id.bind("<FocusIn>", limpar_texto)
    Label(window, text="ID do produto:").pack()
    entry_id.config(font=("Arial", 10, "bold"))
    entry_id.pack()
    entry_id.insert(0,"")
    entry_qtd = Entry(window)
    # entry_qtd.bind("<FocusIn>", limpar_texto)
    entry_qtd.config(font=("Arial", 10, "bold"))
    Label(window, text="Quantidade do produto:").pack()
    entry_qtd.insert(0,"")
    entry_qtd.pack()
    botao_mostrar_carrinho = Button(window, text="Mostrar carrinho", command=lambda: checar_carrinho(carrinho,text))
    botao_mostrar_carrinho.pack(side=LEFT)
    botao_mostrar_carrinho.config(width=24)
    botao_mostrar_carrinho.config(height=1)
    botao_mostrar_carrinho.config(padx=10, pady=10)
    botao_mostrar_carrinho.config(bg="gray")
    botao_mostrar_carrinho.config(font=("Arial", 10, "bold"))
    botao_mostrar_carrinho.config(fg="black")
    botao_adicionar = Button(window, text="Adicionar ao carrinho", command=lambda:add_produto(carrinho, entry_id, entry_qtd, text))
    botao_adicionar.pack(side=LEFT)
    botao_adicionar.config(fg="black")
    botao_adicionar.config(bg="gray")
    botao_adicionar.config(font=("Arial", 10, "bold"))
    botao_adicionar.config(width=24,height=1)
    botao_adicionar.config(padx=10, pady=10)
    botao_compra = Button(window,text="Concluir Compra", command=lambda: click())
    botao_compra.config(fg="black")
    botao_compra.config(bg="gray")
    botao_compra.config(width=24,height=1)
    botao_compra.config(padx=10, pady=10)
    botao_compra.config(font=("Arial", 10, "bold"))
    botao_compra.pack(side=LEFT)
    botao_estoque = Button(window, text="Mostrar estoque", command=lambda: checar_produtos(mercado, text))
    botao_estoque.config(font=("Arial", 10, "bold"))
    botao_estoque.config(bg="gray")
    botao_estoque.config(width=24)
    botao_estoque.config(height=1)
    botao_estoque.config(padx=10, pady=10)
    botao_estoque.pack(side=LEFT)

    window.mainloop()







def checar_carrinho(carrinho, text):
    text.delete("1.0", END)
    text.insert(END, str(carrinho))

def click():
     if messagebox.askokcancel(title="Concluir a compra",message="Você deseja concluir a compra?"):
         messagebox.showinfo(title="Compra concluída!", message="Muito obrigado por comprar conosco, volte sempre!")
         exit()

     else:
         messagebox.showwarning(title="Compra cancelada!", message="Você cancelou a compra!")






def checar_produtos(mercado, text):
    text.delete("1.0", END)
    for produtos in mercado.produtos.values():
        text.insert(END, str(produtos)+"\n")

def add_produto(carrinho, entry_id, entry_qtd, text):

    if entry_id.get() == "" or entry_qtd.get() == "":
         return showwarning(title="Erro ao adicionar",message="Por favor, digite um código e quantidade do produto.")
    else:

        try:
            int(entry_id.get())
            int(entry_qtd.get())
        except ValueError:
            showwarning(title="Erro ao adicionar",message="Por favor, digite apenas números inteiros.")
        else:
            id = entry_id.get()
            qtd = entry_qtd.get()
            id = int(id)
            qtd = int(qtd)
            text.delete("1.0", END)
            carrinho.comprar_produto(id, qtd)
            text.insert(END, str(carrinho))

# def remover_produto(carrinho,)