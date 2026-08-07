class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.au = autor
        self.num = num_paginas

    def metodo(self):
        if self.num <= 100:
            print(f"Livro pequeno!{self.titulo}")
        else:
            print(f"Livro grande!{self.titulo}")


Percy_Jackson = Livro("Percy Jackson", "BlaBla", 100)
Harry_Potter = Livro("Harry Potter", "Bla", 101)

Percy_Jackson.metodo()
Harry_Potter.metodo()

