import json
import tkinter as tk
from tkinter import ttk

import requests


class Container:
    def __init__(self, parent):
        self.myParent = parent
        self.container = tk.Frame(parent)
        self.container.pack()

        self.titulo = ttk.Label(self.container, text="Consultar por Endereço")
        self.titulo.config(font=("Arial", 14, "normal", "normal"))

        self.lb_uf = ttk.Label(self.container, text="ESTADO:")
        self.lb_uf.config(font=("Arial", 12, "normal", "normal"))
        self.uf = ttk.Entry(self.container)
        self.uf.config(font=("Arial", 14, "bold", "bold"), width=4)

        self.lb_municipio = ttk.Label(self.container, text="MUNICIPIO:")
        self.lb_municipio.config(font=("Arial", 12, "normal", "normal"))
        self.municipio = ttk.Entry(self.container)
        self.municipio.config(font=("Arial", 14, "bold", "bold"), width=30)

        self.lb_logradouro = ttk.Label(self.container, text="LOGRADOURO:")
        self.lb_logradouro.config(font=("Arial", 12, "normal", "normal"))
        self.logradouro = ttk.Entry(self.container)
        self.logradouro.config(font=("Arial", 14, "bold", "bold"), width=30)

        self.consultar_button = tk.Button(
            self.container, text="Consultar", command=self.consultar
        )
        self.consultar_button.configure(
            font=("Verdana", 16, "normal", "normal"), foreground="blue"
        )

        self.resultado_label = ttk.Label(self.container, text="")
        self.resultado_label.config(
            font=("Comic Sans ms", 16, "normal", "normal"), foreground="green"
        )

        self.titulo.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.lb_uf.grid(row=1, column=0, padx=10, pady=10)
        self.uf.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        self.lb_municipio.grid(row=2, column=0, padx=10, pady=10)
        self.municipio.grid(row=2, column=1, padx=10, pady=10)
        self.lb_logradouro.grid(row=3, column=0, padx=10, pady=10)
        self.logradouro.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        self.consultar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def consultar(self):
        p1 = self.uf.get()
        p2 = self.municipio.get()
        p3 = self.logradouro.get()
        retorno = ""

        response = requests.get(
            "https://viacep.com.br/ws/" + p1 + "/" + p2 + "/" + p3 + "/json/"
        )
        enderecos = json.loads(response.text)
        if enderecos == []:
            retorno = "CEP não encontrada!"
        else:
            for cep in enderecos:
                retorno += f"""
CEP: {cep['cep']}
Logradouro: {cep['logradouro']}
---------------------------------------------------
"""
        self.resultado_label.config(text=retorno)


def main():
    raiz = tk.Tk()
    raiz.title("Consulta CEP")
    apl = Container(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()
