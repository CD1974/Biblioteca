class Autor:
    def __init__(self, nombre, apellidos):
        self.Nombre = nombre
        self.Apellidos = apellidos
    def MostrarAutor(self):
        print("Autor:", self.Nombre, " ", self.Apellidos)

class Libro:
    def __init__(self, titulo, isbn):
        self.Titulo = titulo
        self.ISBN = isbn
    def AñadirAutor(self, autor):
        self.Autor = autor
    def MostrarLibros(self):
        print("-----Libro-----")
        print("Titulo: ", self.Titulo)
        print("ISBN: ", self.ISBN)
        self.Autor.MostrarAutor()
        print("-----------")
    def ObtenerTitulo(self):
        return self.Titulo;

class Biblioteca:
    def __init__(self):
        self.ListaLibros = []
    def NumeroLibros(self):
        return len(self.ListaLibros)
    def AñadirLibro(self, libro):
        self.ListaLibros = self.ListaLibros + [libro]
    def MostrarBiblioteca(self):
        print("##################################")
        for item in self.ListaLibros:
            item.MostrarLibros()
        print("##################################")
    def BorrarLibro(self, titulo):
        encontrado = False
        posicionaborrar = -1
        for item in self.ListaLibros:
            posicionaborrar += 1
            if item.ObtenerTitulo() == titulo:
                encontrado = True
                break
        if encontrado:
            del self.ListaLibros[posicionaborrar]
            print("¡Libro borrado correctamente!")
        else:
            print("¡Libro no encontrado!")

def MostrarMenu():
    print(""" Menu
1) Añadir Libro a la biblioteca
2) Mostrar biblioteca
3) Borrar libro
4) ¿Numero de libros?
5) Salir """)

def AñadirLibroABiblioteca(biblioteca):
    titulo = input("Introduzca el titulo del libro: ")
    isbn = input("Introduzca el ISBN del libro: ")
    autonombre = input("Introduzca el nombre del autor: ")
    autoapellidos = input("Introduzca el apellido del autor: ")
    autor = Autor(autonombre,autoapellidos)
    libro = Libro(titulo, isbn)
    libro.AñadirAutor(autor)
    biblioteca.AñadirLibro(libro)
    return biblioteca
def MostarBiblioteca(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibro(biblioteca):
    titulo= input("Introduzca el titulo a borrar: ")
    biblioteca.BorrarLibro(titulo)

def NumeroLibros(biblioteca):
    print("El número de libros en la biblioteca es: ", biblioteca.NumeroLibros())

fin = False
biblioteca = Biblioteca()

while not fin:
    MostrarMenu()
    opcion = int(input("Seleccione opción: "))
    if(opcion == 1):
        biblioteca = AñadirLibroABiblioteca(biblioteca)
    elif(opcion == 2):
        MostarBiblioteca(biblioteca)
    elif(opcion == 3):
        BorrarLibro(biblioteca)
    elif(opcion == 4):
        NumeroLibros(biblioteca)
    elif(opcion == 5):
        fin = True

print("¡Adios!")
