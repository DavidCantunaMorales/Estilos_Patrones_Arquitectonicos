from modelo import RepositorioLibros
from vista import VistaBiblioteca
from controlador import ControladorBiblioteca

# Crear componentes
repositorio = RepositorioLibros()
vista = VistaBiblioteca()
controlador = ControladorBiblioteca(repositorio, vista)

def menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Agregar libro")
    print("2. Buscar libro por título")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar todos los libros")
    print("6. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = menu()
        
        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            controlador.agregar_libro(titulo, autor)

        elif opcion == "2":
            titulo = input("Ingrese el título a buscar: ")
            controlador.buscar_libros(titulo)

        elif opcion == "3":
            try:
                id_libro = int(input("Ingrese el ID del libro a prestar: "))
                controlador.prestar_libro(id_libro)
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "4":
            try:
                id_libro = int(input("Ingrese el ID del libro a devolver: "))
                controlador.devolver_libro(id_libro)
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "5":
            print("\nLista de libros:")
            controlador.buscar_libros("")

        elif opcion == "6":
            print("¡Gracias por usar la Biblioteca!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
