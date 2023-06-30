from video import Video
from nodo import Nodo

class Playlist:
    def __init__(self):
        self.head = None

    def agregar_video(self, titulo, autor, duracion):
        nuevo_video = Video(titulo, autor, duracion)
        nuevo_nodo = Nodo(nuevo_video)

        if not self.head:
            self.head = nuevo_nodo
            self.head.siguiente = self.head
        else:
            nodo_actual = self.head
            while nodo_actual.siguiente != self.head:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.head

    def mostrar_playlist(self):
        if not self.head:
            print("La lista de videos está vacia")
            return
        nodo_actual = self.head
        while True:
            print("Título:", nodo_actual.video.titulo)
            print("Autor:", nodo_actual.video.autor)
            print("Duración:", nodo_actual.video.duracion)
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.head:
                break

    def buscar_video(self, titulo):
        if not self.head:
            return None
        nodo_actual = self.head
        while True:
            if nodo_actual.video.titulo == titulo:
                return nodo_actual.video
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.head:
                break
        return None

    def eliminar_video(self, titulo):
        if not self.head:
            return
        nodo_actual = self.head
        nodo_anterior = None
        while True:
            if nodo_actual.video.titulo == titulo:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                else:
                    while nodo_actual.siguiente != self.head:
                        nodo_actual = nodo_actual.siguiente
                    nodo_actual.next = self.head.siguiente
                    self.head = self.head.siguiente
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.head:
                break

    def esta_vacia(self):
        return self.head is None

    def menu(self):
        while True:
            print("-------- menu --------")
            print("1. Agregar video")
            print("2. Mostrar playlist")
            print("3. Buscar video")
            print("4. Eliminar video")
            print("5. Salir")
            print("\n")
            
            opcion = input("Ingrese el número de la opción que desea realizar: ")

            if opcion == "1":
                titulo = input("Ingrese el título del video: ")
                autor = input("Ingrese el autor del video: ")
                duracion = input("Ingrese la duración del video: ")
                self.agregar_video(titulo, autor, duracion)
                print("Video agregado exitosamente.")

            elif opcion == "2":
                print("\n")
                self.mostrar_playlist()
                print("\n")

            elif opcion == "3":
                titulo = input("Ingrese el título del video que desea buscar: ")
                video = self.buscar_video(titulo)
                if video:
                    print("Video encontrado:")
                    print("Título:", video.titulo)
                    print("Autor:", video.autor)
                    print("Duración:", video.duracion)
                    print("\n")
                else:
                    print("El video no se encontró en la playlist.")

            elif opcion == "4":
                titulo = input("Ingrese el título del video que desea eliminar: ")
                self.eliminar_video(titulo)
                print("Video eliminado")

            elif opcion == "5":
                print("Usted salio del programa")
                break

            else:
                print("Opción inválida.")

playlist = Playlist()
playlist.menu()
