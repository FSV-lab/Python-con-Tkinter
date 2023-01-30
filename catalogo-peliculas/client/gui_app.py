import tkinter as tk #importamos el tkinter en este Script
from tkinter import ttk,messagebox #importamos ttk para utlizar la tabla
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar,editar,eliminar

def barra_menu(root): #creamos una función llamada barra_menu y dentro empaquetamos la funcion root
    barra_menu = tk.Menu(root) #creamos una variable barra_menu utilizamos tky creamos un objeto Menu() empaquetamos a root
    root.config(menu=barra_menu, width=300, height=300) #con root agregamosla configuración en los parametro creamos la variable menu y anexamos el menu a esta con sus dimensiones

    menu_inicio = tk.Menu(barra_menu,tearoff = 0)#barra_menu estará dentro de variable menu que a su vez nombraremos una nueva variable que contendrá con menu_inicio y tearoff elimina la linea sobrante
    barra_menu.add_cascade(label ='Inicio', menu = menu_inicio)#El menu_inicio en variable menu y este elemento funcional estará en la etiqueta inicio en formar de cascada en barra_menu

    menu_inicio.add_command(label ='Crear Registro en DB',command= crear_tabla)#la primera etiqueta crear es adherida para desplegar
    menu_inicio.add_command(label ='Eliminar Registro en DB',command= borrar_tabla)#la segunda etiqueta Eliminar es adherida para desplegar
    menu_inicio.add_command(label ='Salir',command = root.destroy)#la tercera etiqueta Salir es adherida para desplegar command le da función ala etiqueta salir 

    barra_menu.add_cascade(label='Consultas')#eliminamos la variable menu
    barra_menu.add_cascade(label='Configuración')#simplemente se adhiren las demas items
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame): #la clase Frame contendrá el frame de este script
    def __init__ (self,root = None):#Esta función __init__ 
        super().__init__(root,width=480,height=320)#Por herencia cuando se inicie el script tendrá las dimensiones
        self.root = root 
        self.pack()
        #self.config(bg='green')
        self.id_pelicula = None
        self.campos_pelicula()
        self.desabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):
        #labels de cada campo
        self.label_nombre = tk.Label(self,text ='Nombre:')
        self.label_nombre.config(font =('Arial',12,'bold'))
        self.label_nombre.grid(row = 0,column = 0,padx=10,pady=10)

        self.label_duracion = tk.Label(self,text ='Duración:')
        self.label_duracion.config(font =('Arial',12,'bold'))
        self.label_duracion.grid(row = 1,column = 0,padx=10,pady=10)

        self.label_genero = tk.Label(self,text ='Genero:')
        self.label_genero.config(font =('Arial',12,'bold'))
        self.label_genero.grid(row = 2,column = 0,padx=10,pady=10)
      
        #Entrys de Cada Campo
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50,font =('Arial',12,))
        self.entry_nombre.grid(row = 0 ,column = 1,padx=10,pady=10,columnspan=2) 
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable = self.mi_duracion)
        self.entry_duracion.config(width=50,font =('Arial',12,))
        self.entry_duracion.grid(row = 1 ,column = 1,padx=10,pady=10,columnspan=2)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self,textvariable = self.mi_genero)
        self.entry_genero.config(width=50,font =('Arial',12,))
        self.entry_genero.grid(row = 2 ,column = 1,padx=10,pady=10,columnspan=2)

        #Botones
        self.boton_nuevo = tk.Button(self,text='Nuevo',command=self.habilitar_campos)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),fg ='#DAD5D6',bg='#158645',
                                cursor ='hand2',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3,column=0,padx=10,pady=10)

        self.boton_guardar = tk.Button(self,text='Guardar',command =self.guardar_datos)
        self.boton_guardar.config(width=20,font=('Arial',12,'bold'),fg ='#DAD5D6',bg='blue',
                                cursor ='hand2',activebackground='#3586DF')
        self.boton_guardar.grid(row=3,column=1,padx=10,pady=10)

        self.boton_cancelar = tk.Button(self,text="Cancelar",command=self.desabilitar_campos)
        self.boton_cancelar.config(width=20,font=('Arial',12,'bold'),fg ='#DAD5D6',bg='red',
                                cursor ='hand2',activebackground='#E15370')
        self.boton_cancelar.grid(row=3,column=2,padx=10,pady=10)

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
    
    def guardar_datos(self):
        
        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get(),
        )
        
        if self.id_pelicula == None:
            guardar(pelicula)
        else:
            editar(pelicula,self.id_pelicula)
            
        
        self.tabla_peliculas()
        
        #desabilita campos
        self.desabilitar_campos()

    def tabla_peliculas(self):
        #Recuperar la lista de peliculas
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        self.tabla = ttk.Treeview(self,
        column =('Nombre','Duración','Genero'))
        self.tabla.grid(row = 4,column = 0,columnspan = 4,sticky='nse')
        
        #Scrollbar para latabla si excede 10 filas
        self.scroll = ttk.Scrollbar(self,orient='vertical',command=self.tabla.yview)
        self.scroll.grid(row=4,column = 4,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='NOMBRE')
        self.tabla.heading('#2',text='DURACION')
        self.tabla.heading('#3',text='GENERO')

        #Insertar datos en la tabla
        #Iterar la lista de peliculas
        for p in self.lista_peliculas:   
            self.tabla.insert('',0,text=p[0],
            values = (p[1],p[2],p[3]))

        #Boton Editar
        self.boton_Editar = tk.Button(self,text='Editar',command= self.editar_datos)
        self.boton_Editar.config(width=20,font=('Arial',12,'bold'),fg ='#DAD5D6',bg='#158645',
                                cursor ='hand2',activebackground='#35BD6F')
        self.boton_Editar.grid(row=5,column=0,padx=10,pady=10)
        
        #Boton de Eliminar 
        self.boton_Eliminar = tk.Button(self,text="Eliminar",command=self.eliminar_datos)
        self.boton_Eliminar.config(width=20,font=('Arial',12,'bold'),fg ='#DAD5D6',bg='red',
                                cursor ='hand2',activebackground='#E15370')
        self.boton_Eliminar.grid(row=5,column=1,padx=10,pady=10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula =self.tabla.item(self.tabla.selection())['values'][0]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0,self.nombre_pelicula)
            self.entry_duracion.insert(0,self.duracion_pelicula)
            self.entry_genero.insert(0,self.genero_pelicula)
            
        except:    
            titulo = 'Edición de datos'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo,mensaje)
            
    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            eliminar(self.id_pelicula)
            self.tabla_peliculas()
        except:
            titulo = 'Eliminar un registro'
            mensaje = 'No ha seleccionado ningún registro'
            messagebox.showerror(titulo,mensaje)
        