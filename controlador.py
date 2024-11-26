from modelo import Libro, RepositorioLibros
from vista import VistaBiblioteca

class ControladorBiblioteca:
    def __init__(self, repositorio, vista):
        self.repositorio = repositorio
        self.vista = vista

    def agregar_libro(self, titulo, autor):
        nuevo_libro = Libro(id=len(self.repositorio.libros) + 1, titulo=titulo, autor=autor)
        self.repositorio.agregar_libro(nuevo_libro)
        self.vista.mensaje(f"Libro '{titulo}' agregado exitosamente.")

    def buscar_libros(self, titulo):
        libros = self.repositorio.buscar_por_titulo(titulo)
        self.vista.mostrar_libros(libros)

    def prestar_libro(self, id_libro):
        if self.repositorio.marcar_como_prestado(id_libro):
            self.vista.mensaje("El libro fue prestado exitosamente.")
        else:
            self.vista.mensaje("No se pudo prestar el libro. Verifique el ID o el estado del libro.")

    def devolver_libro(self, id_libro):
        if self.repositorio.devolver_libro(id_libro):
            self.vista.mensaje("El libro fue devuelto exitosamente.")
        else:
            self.vista.mensaje("No se pudo devolver el libro. Verifique el ID o el estado del libro.")
