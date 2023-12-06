import os
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

class AdaptadorImagenes: #Creamos la clase
    def __init__(self, root): #Inicializamos los atributos
        #Configuramos la ventana principal
        self.root = root
        self.root.title("Image Adapter")

        #Cracion de etiqueta para mostrar imagen
        self.image_label = Label(root)
        self.image_label.pack(padx=20, pady=20)

        #boton para cargar imagen
        self.load_button = Button(root, text="Cargar Imagen", command=self.cargar_imagen)
        self.load_button.pack(pady=10)

        #Boto para redimensionar y guardar imagen en donde vos quieras 
        self.resize_button = Button(root, text="Redimensionar y Guardar", command=self.redimencionar_guardar_imagen)
        self.resize_button.pack(pady=10)

        #variables para almacenar la ruta de la imagen cargada 
        self.image_path = None
        self.image = None

    def cargar_imagen(self):
        #Usamos el metodo para cargar una imagen desde el sistema de archivos esto permite convertirla en lo siguiente
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            #Almacena la ruta de la imagen cargada y cargar la imagen usando Pillow desde pyt
            self.image_path = file_path
            self.image = Image.open(file_path)
            self.mostrar_imagen()

    def redimencionar_guardar_imagen(self): 
        #Este metodo es  para redimensionar y guardar la imagen
        if self.image:
            w = self.image.width
            h = self.image.height
            
            #new_width = 300
            #new_height = int(self.image.height * (new_width / self.image.width))
            new_width = int(w/10)
            new_height = int(h/10)

            #Redimensionar la imagen usando el modo LANCZOS por que no sirve ANIMALIAS NO SE POR QUE
            resized_image = self.image.resize((new_width, new_height), Image.LANCZOS )

            #Aca es para guardar el archivo en la ubicacion que el usuario desee
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                       filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])

            if save_path:
                #Guardar la imagen redimensionada en la ubicación especificada por el mismisimo usuario
                resized_image.save(save_path)
                print(f"Imagen redimensionada y guardada en: {save_path}")

    def mostrar_imagen(self):
        #Metodo para mostrar la imagen cargada en la etiqueta
        if self.image_path:
            image = Image.open(self.image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(image=photo)
            self.image_label.image = photo

#Ejecucion del programa...
if __name__ == "__main__":
    root = Tk()
    app = AdaptadorImagenes(root)
    root.mainloop()
