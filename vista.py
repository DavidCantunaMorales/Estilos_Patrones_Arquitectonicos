class VistaBiblioteca:
    def mostrar_libros(self, libros):
        if not libros:
            print("No se encontraron libros.")
        else:
            for libro in libros:
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"{libro.id}. {libro.titulo} - {libro.autor} ({estado})")

    def mensaje(self, texto):
        print(texto)
