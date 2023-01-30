import tkinter as tk #importamos el tkinter y lo abriviamos con as
from client.gui_app import Frame,barra_menu


def main(): #se crea una función para la ventana invocando todos los elementos
    root = tk.Tk()#convertimos la variable de Tk
    root.title('Catalogo de Peliculas')#Agregamos un titulo
    root.iconbitmap('img/cp-logo.ico')#agregamo una imagen al frame en la parte superior
    root.resizable(0,0)#los dos parametros en 0,0 hace de false para los lados esto evita modificar manualmente
    barra_menu(root)
    
    app = Frame(root=root)
         
    app.mainloop()# main cierra la ventana
    
if __name__ == '__main__':
    main()