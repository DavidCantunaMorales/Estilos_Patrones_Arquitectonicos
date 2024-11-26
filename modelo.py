import os

class Libro:
    def __init__(self, id, titulo, autor, disponible=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def to_line(self):
        return f"{self.id},{self.titulo},{self.autor},{self.disponible}\n"

    @staticmethod
    def from_line(line):
        id, titulo, autor, disponible = line.strip().split(",")
        return Libro(int(id), titulo, autor, disponible == "True")


class RepositorioLibros:
    def __init__(self, archivo="libros.txt"):
        self.archivo = archivo
        self.libros = self.cargar_libros()

    def cargar_libros(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r") as file:
            return [Libro.from_line(line) for line in file.readlines()]

    def guardar_libros(self):
        with open(self.archivo, "w") as file:
            file.writelines(libro.to_line() for libro in self.libros)

    def agregar_libro(self, libro):
        self.libros.append(libro)
        self.guardar_libros()

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]

    def marcar_como_prestado(self, id_libro):
        for libro in self.libros:
            if libro.id == id_libro and libro.disponible:
                libro.disponible = False
                self.guardar_libros()
                return True
        return False

    def devolver_libro(self, id_libro):
        for libro in self.libros:
            if libro.id == id_libro and not libro.disponible:
                libro.disponible = True
                self.guardar_libros()
                return True
        return False
