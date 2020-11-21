from tkinter import *                       
import tkinter as tkk
from tkinter import ttk
from PIL import ImageTk,Image           #esta importacion no spermite manipular y usar imagenes 
from tkinter import messagebox as mb    #Nos permite usar mensajes 
import sqlite3                          #NPermite conectarnos a la base de datos
from sqlite3 import Error

ventanal=tkk.Tk()
ventanal.title("_Bienvenido_")           #Titulo de la ventana principal
ventanal.geometry("250x450+150+220")     #Dimenciones de la ventana
    
color='dark sea green'                      #Definimos el color de la ventana
ventanal['bg']=color                  

Label(ventanal,bg=color,text="Inicio de sesion",font=("Arial Black",16)).pack()        #Ponemos titulo a la ventana de inicio

#Abrimos la imagen para la venta de inicio de sesion
imagen=Image.open("logo_size.jpg")                         #Abrimos la imagen 'Logo.png'
imagen=imagen.resize((180,180),Image.ANTIALIAS)       #Modificamos las dimenciones para que sea compatible al tamaño de la ventana
photoImg=ImageTk.PhotoImage(imagen)                   #Nombramos la variable que manipula la imagen
panel=tkk.Label(ventanal,image=photoImg).pack()        #Mostramos la imagen

#Abrimos imagen para la ventana registro
#Abrimos la imagen 'icono.jpg'
img_reg=Image.open("icono.jpg")
#Redimensionamos la imagen
img_reg=img_reg.resize((180,180),Image.ANTIALIAS)
#Le damos nombre a nuestra imagen redimensionada (photo_reg)
photo_reg=ImageTk.PhotoImage(img_reg)                

#Datos que mostrara la ventana
Label(ventanal,text="Usuario : ",bg=color,font=("Arial Black",10)).pack()    #Mostramos el dato a pedir
caja1=Entry(ventanal,font=("Arial",10))                                      #Creamos la caja de respuesta
caja1.pack()                                                                
Label(ventanal,text="Contraseña : ",bg=color,font=("Arial Black",10)).pack() #Mostramos el dato a pedir
caja2=Entry(ventanal,show="*")                                               #Creamos la caja de respuesta
caja2.pack()                                                                
#Nos conectamos a la base de datos
db=sqlite3.connect('Inventario.db')
#creamos un cursor
c=db.cursor()                                                               

#Creamos la funcion para verificar datos
def login():
    #Obtenemos el datos
    usuario=caja1.get()                                     
    contr=caja2.get()                                       
    c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',(usuario,contr))
    #comprobamos los datos capturados
    if c.fetchall():
        mb.showinfo(title="Login Correcto",message="Iniciando sesion")        #Mostramos el mensaje de 'Login Correcto'
        c.close()
        ventanal.destroy()


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        #Creamos una funcion que mostrara los mensajes correspondientes a los botones 
        def mesagge():
            answer = mb.showerror("Clientes", "Esta opcion no esta disponible ;)")

        def mensage():
            answer = mb.showerror("Venta", "Esta opcion no esta disponible :)")
   
        def mensaje():
            answer = mb.askyesno("Salir", "Cerrar Aplicacion\nConfirmar")
            if(answer):
                #Esta linea destruye la ventana de verificarse la accion.
                ventana.destroy()
                
        #creamos la clase menu
        class Menu:
            def Ingresar_db(self):
                conexion=sqlite3.connect("Inventario.db")
                return conexion
            
            def __init__(self,ventana):
                self.ventana = ventana
                #Definimos un titulo de la ventana
                self.ventana.title("Menu de opciones")
                #Definimos dimenciones de la ventana
                self.ventana.geometry("1150x650+00+0")      
                self.ventana.resizable(False,False)
                #Definimos un titulo para la ventana principal
                title=Label(self.ventana,text=" Stocks Control ", bd=10,relief=RAISED, font=("Arial", 40,"bold"),bg="powderblue", fg="white")
                title.pack(side=TOP)
                #Creamos un boton de salida y asignamos dimenciones y color
                Exit_btn=Button(ventana,text="Salir", width=7, bg="snow3", font=("Arial",17,"bold"),command=mensaje)
                Exit_btn.place(x=1020, y=40)
                #Creamo sboton de ventas
                Venta_btn=Button(ventana,text="Venta", width=6, bg="snow3", font=("Arial",17,"bold"),command=mensage)
                Venta_btn.place(x=922, y=40)
                #Creamos boton cliente y asignamos tipo y color de letra
                Cliente_btn=Button(ventana,text="Clientes", width=7, bg="snow3", font=("Arial",17,"bold"),command=mesagge)
                Cliente_btn.place(x=809, y=40)

                #Definimos las variables
                self.codigo_var=StringVar()
                self.nombre_var=StringVar()
                self.precio_var=StringVar()
                self.categoria_var=StringVar()
                self.existencias_var=StringVar()
        
                #definimos las condiciones de busqueda texto y valor numerico
                self.buscar_por=StringVar()
                self.buscar_txt=StringVar()
        
                #creamos el frame donde mostraremos los datos requeridos, asiganmos color y dimenciones 
                Manage_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="Medium aquamarine")
                #Asignamos posiscion y dimenciones
                Manage_Frame.place(x=20,y=90,width=420,height=480)
        
                #Definimos el titulo del frame y asignamos un color de fondo y tamañao de letra
                m_title=Label(Manage_Frame,text= " Menú de opciones " , bg="khaki1",font=("Arial",22,"bold"))
                #Asignamos posiscion y dimenciones
                m_title.grid(row=0,columnspan=2,pady=20)
        
                #Mostramos los datos que se desean registrar, asignamos color, y tamaño de letra.
                lbl_roll=Label(Manage_Frame,text="Codigo:", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_roll.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        
                #Definimos la caja de respuesta para el dato pedido 
                txt_Roll=Entry(Manage_Frame, textvariable=self.codigo_var , font=("Arial",14,"bold"), bd=5, relief=GROOVE)
                #Asignamos posiscion y dimenciones
                txt_Roll.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        
                #Mostramos los datos que se desean registrar, asignamos color, y tamaño de letra.
                lbl_name=Label(Manage_Frame,text="Producto:", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        
                #Definimos la caja de respuesta para el dato pedido 
                txt_name=Entry(Manage_Frame, textvariable=self.nombre_var, font=("Arial",14,"bold"), bd=5, relief=GROOVE)
                #Asignamos posiscion y dimenciones
                txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
                #Mostramos los datos que se desean registrar, asignamos color, y tamaño de letra.
                lbl_precio=Label(Manage_Frame,text="Precio.", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_precio.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        
                #Definimos la caja de respuesta para el dato pedido 
                txt_precio=Entry(Manage_Frame, textvariable=self.precio_var, font=("Arial",14,"bold"), bd=5, relief=GROOVE)
                #Asignamos posiscion y dimenciones
                txt_precio.grid(row=3,column=1,pady=10,padx=10,sticky="w")
        
                #Mostramos los datos que se desean registrar, asignamos color, y tamaño de letra.
                lbl_categoria=Label(Manage_Frame,text="Categoria", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_categoria.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        
                #Creamos el combobox y asignamos las opciones a seleccionar
                combo_categoria=ttk.Combobox(Manage_Frame,textvariable=self.categoria_var , width=9, font=("Arial",14,"bold"),state='readonly')
                #Asiganamos valores dentro del combobox que mostrara las siguientes opciones
                combo_categoria['values']=(" ","Lacteos","Papeleria","Abarrotes","Enlatados","Salud","Otro")
                #Asignamos posiscion y dimenciones
                combo_categoria.grid(row=4, column=1,padx=20,pady=10)
        
                #Mostramos los datos que se desean registrar, asignamos color, y tamaño de letra.
                lbl_existencias=Label(Manage_Frame,text="Existencias:", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_existencias.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        
                #Definimos la caja de respuesta para el dato pedido 
                txt_existencias=Entry(Manage_Frame,textvariable=self.existencias_var, font=("Arial",14,"bold"), bd=5, relief=GROOVE)
                #Asignamos posiscion y dimenciones
                txt_existencias.grid(row=5,column=1,pady=10,padx=10,sticky="w")
        
                #Creamos un segundo frame donde pondremos los botones 
                btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE, bg="pale turquoise")
                #Asignamos posiscion y dimenciones
                btn_Frame.place(x=15,y=400,width=320)
        
                #Creamos el boton agregar, asignamos dimenciones y posicion
                Add_btn=Button(btn_Frame,text="Agregar", width=7, command=self.agregar_registro)
                #Asignamos posiscion y dimenciones
                Add_btn.grid(row=0, column=0, padx=10, pady=10)
        
                #Creamos el boton actualizar, asignamos dimenciones y posicion
                Update_btn=Button(btn_Frame, text="Actualizar", width=7, command=self.update_data)
                #Asignamos posiscion y dimenciones
                Update_btn.grid(row=0, column=1, padx=10, pady=10)
        
                #Creamos el boton borrar, asignamos dimenciones y posicion
                Delete_btn=Button(btn_Frame,text="Eliminar", width=7, command=self.delete_data)
                #Asignamos posiscion y dimenciones
                Delete_btn.grid(row=0, column=2, padx=10, pady=10)
        
                #Creamos el boton limpiar, asignamos dimenciones y posicion: este boton nos permitira limpiar las cajas de datos.
                Clear_btn=Button(btn_Frame,text="Limpiar", width=7, command=self.clear)
                #Asignamos posiscion y dimenciones
                Clear_btn.grid(row=0, column=3, padx=10, pady=10)

                #Creamos el Frame que contendra los botones de busqueda, asiganamos color
                Detail_Frame=Frame(self.ventana,bd=4,relief=RIDGE, bg="Medium aquamarine")
                #Asignamos posiscion y dimenciones
                Detail_Frame.place(x=420,y=90,width=710,height=480)
        
                #creamos el boton de buscar, nos permitira ver los datos y asignamos colore
                lbl_search=Label(Detail_Frame,text="Buscar por:", bg="Medium aquamarine", fg="snow", font=("Arial",14,"bold"))
                #Asignamos posiscion y dimenciones
                lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
                #Asignamos opciones al combobox de busqueda
                combo_search=ttk.Combobox(Detail_Frame,textvariable=self.buscar_por, width=10, font=("Arial",15,"bold"),state='readonly')
                #Asigamos valores dentro del combobox de busqueda que mostrara lo siguiente como opciones 
                combo_search['values']=("Codigo","Nombre","Precio")
                #Asignamos posiscion y dimenciones
                combo_search.grid(row=0, column=2,padx=20,pady=10)
        
                #Creamos un cuadro de busqueda para visualizar los datos
                txt_search=Entry(Detail_Frame,textvariable=self.buscar_txt, width=20, font=("Arial",11,"bold"), bd=5, relief=GROOVE)
                #Asignamos posiscion y dimenciones
                txt_search.grid(row=0,column=3,pady=10,padx=20,sticky="w")
        
                #Creamos el boton de busqueda que buscara lo obtenido del cuadro de busqueda anterior
                search_btn=Button(Detail_Frame,text="Buscar", width=6,command=self.buscar_data)
                #Asignamos posiscion y dimenciones
                search_btn.grid(row=0, column=4, padx=10, pady=10)
        
                #Creamos un boton que mostrara todos los datos de la tabla
                showall_btn=Button(Detail_Frame, text="Mostrar Todo", font=("Arial", 8) ,width=10,command=self.fetch_data)
                #Asignamos posiscion y dimenciones
                showall_btn.grid(row=0, column=5, padx=10, pady=10)
        
                #Mostramos una tabla donde se mostraran los registros
                Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE, bg="crimson")
                #Asignamos posiscion y dimenciones
                Table_Frame.place(x=10,y=70,width=660,height=400)
        
                #Es un desplazador que no sayudara a mostrar los registros que la tabla no visiualice
                scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
                #Asignamos posiscion y dimenciones
                scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
                #Mostramos el nombre de los datos en la tabla de los registros
                self.Menu_table=ttk.Treeview(Table_Frame,columns=("codigo","nombre", "precio", "categoria", "existencias"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
                
                #Definimos los botones para desplazar de izquierda a derecha dentro del Frame.
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT, fill=Y)
                
                #Conectamos los scrolls con los encabezados
                scroll_x.config(command=self.Menu_table.xview)
                scroll_y.config(command=self.Menu_table.yview)
        
                #Definimos las variables y las mostramos como encabezado en la tabla.
                self.Menu_table.heading("codigo", text="Codigo")
                self.Menu_table.heading("nombre", text="Nombre")
                self.Menu_table.heading("precio", text="Precio")
                self.Menu_table.heading("categoria", text="Categoria")
                self.Menu_table.heading("existencias", text="Existencias")
    
                # show, nos permite mostrar los ancabezados definidos anteriormente
                self.Menu_table['show']= 'headings'
        
                #Mostramos los encabezados en la tabla de registro
                self.Menu_table.column("codigo", width=90)
                self.Menu_table.column("nombre", width=90)
                self.Menu_table.column("precio", width=90)
                self.Menu_table.column("categoria", width=90)
                self.Menu_table.column("existencias", width=90)

                self.Menu_table.pack(fill=BOTH,expand=1)

                self.Menu_table.bind("<ButtonRelease-1>", self.get_cursor)

                self.fetch_data()
        
                #Creamos la funcion para agregar nuevo sregistros
            def agregar_registro(self):
                if usuario == "SuperAdmin":
            #La condicion nos permite verificar si el registro fue completado si no, mostrara un mensaje de error
                    if self.codigo_var.get()=="" or self.nombre_var.get()=="" or self.precio_var.get()=="" or self.categoria_var.get()=="" or self.existencias_var.get()=="":
                        mb.showerror("Error", "Registo incompleto")
                    else:
                        #Nos conectamos a la base de datos
                        con=sqlite3.connect("Inventario.db")
                        #Creamos el cursor
                        cur = con.cursor()
                        #Asignamos los valores registrados a la tabla
                        cur.execute("insert into producto values(?,?,?,?,?)",(
                            # Y recogemos los valores asignados a las variables
                            self.codigo_var.get(),
                            self.nombre_var.get(),
                            self.precio_var.get(),
                            self.categoria_var.get(),
                            self.existencias_var.get()
                            ))
                   
                        #El metodo commit nos permite guardar los cambios 
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        #Cerramos la conexion
                        con.close()
                        #Mostramos mensaje de exito
                        mb.showinfo("Exito", "El registro fue exitoso")
                else:
                    mb.showwarning("Operacion invalida","No cuenta con autorización")
                    
                    
                    #Creamos la funcion de obtencion de datos
            def fetch_data(self):
                    #Creamos la conexion a la base de datos 
                con=sqlite3.connect("Inventario.db")
                    #Creamos un cursor
                cur = con.cursor()
                    #Ejecutamos la sentencia, con la que deseamos ver los datos de la tabla
                cur.execute("select * from producto")
                    #Mostramos los datos en la tabla de widget
                rows= cur.fetchall()
                if len(rows)!=0:
                    self.Menu_table.delete(*self.Menu_table.get_children())
                    for row in rows:
                        self.Menu_table.insert('',END,values=row)
                        ##El metodo commit nos permite guardar los cambios 
                    con.commit()
                #Cerramos conexion
                con.close()
        
                #Creamos la funcion para limpiar, pondra en blanco las cajas de datos
            def clear(self):
                #Asignamos espacios vacios a las cajas de respuesta para limpiar el espacio
                self.codigo_var.set("")
                self.nombre_var.set("")
                self.precio_var.set("")
                self.categoria_var.set("")
                self.existencias_var.set("")
            #En esta funcion obtenemos los datos registrados seleccionandolos y automaticamente se mostraran en la caja de respuesta 
            def get_cursor(self,ev):
                cursor_row=self.Menu_table.focus()
                contents=self.Menu_table.item(cursor_row)
        
                row=contents['values']

                #Treamos los valores obtenidos del cursor y los mostramos en los cuadros de respuesta
                self.codigo_var.set(row[0])
                self.nombre_var.set(row[1])
                self.precio_var.set(row[2])
                self.categoria_var.set(row[3])
                self.existencias_var.set(row[4])

                #creamos la funcion de actualizar
            def update_data(self):
                if usuario == "SuperAdmin" :
                #Revisamos los datos, de no ser seleccionado ninguno mostrara un mensaje de error
                    if self.codigo_var.get()=="" or self.nombre_var.get()=="" or self.precio_var.get()=="" or self.categoria_var.get()=="" or self.existencias_var.get()=="":
                        mb.showerror("Error", "Seleccione un registro")
                    else:
                        con=sqlite3.connect("Inventario.db")
                        cur = con.cursor()
                        #Recogemos los datos y nuevos datos para su registro
                        cur.execute("update producto set nombre=?,precio=?,categoria=?,existencias=? where codigo=?",(
                        #recogemos los nuevos valores asignados a las variables
                        self.nombre_var.get(),
                        self.precio_var.get(),
                        self.categoria_var.get(),
                        self.existencias_var.get(),
                        self.codigo_var.get()
                        ))
                        #El metodo commit nos permite guardar los cambios 
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        #Mostramos mensaje de exito
                        mb.showinfo("Actualizado", "Se modifico con exito")
                        #Cerramos la secion
                        con.close()
                else:
                    mb.showwarning("Operacion invalida","No cuenta con autorización")
           
                #Esta funcion borrara los registros de la base de datos    
            def delete_data(self):
                if usuario == "SuperAdmin":
                #Definimos que los espacios de codigo 
                    if self.codigo_var.get()=="":
                        mb.showerror("Error", "Seleccione el registro")
                    else:
                        datos=(self.codigo_var, )
                        #Establkecemos conexion a la base de datos
                        con=sqlite3.connect("Inventario.db")
                        #Creamos el cursor 
                        cur=con.cursor()
                        #Asignamos la operacion de borrado con la condicion where.
                        cur.execute("delete from producto where codigo= ?",self.codigo_var.get())
                        con.commit()
                        self.fetch_data()
                        self.clear()
                        #mostramos mensaje de error
                        mb.showinfo("Eliminado", "Producto elimando")
                        #cerramos conexion ala base de datos
                        con.close()
                else:
                    mb.showwarning("Operacion invalida","No cuenta con autorización")
            
            #Definimos una funcion de opcion de busqueda
            def buscar_data(self):
                #Creamos conexion con la base de datos
                con=sqlite3.connect("Inventario.db")
                #Creamos un cursor
                cur=con.cursor()
                #Definimos la opcin de busqueda 
                cur.execute("select * from producto where "+str(self.buscar_por.get())+" LIKE '%"+str(self.buscar_txt.get())+"%'")
                rows=cur.fetchall()
                #mostramos los registros en la tabla widget
                if len(rows)!=0:
                    self.Menu_table.delete(*self.Menu_table.get_children())
                    for row in rows:
                        self.Menu_table.insert('',END,values=row)
                    ##El metodo commit nos permite guardar los cambios 
                    con.commit()
                #Cerramos la conexion a la base de datos
                con.close()
                
        ventana =tkk.Tk()
        ob=Menu(ventana)
        ventana.mainloop()
                
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        
    
    else:
        mb.showerror(title="Login incorrecto",message="Usuario o contraseña incorrecto")    #Mostramos mensaje de error'Login incorrecto'
        

def nuevaVentana():                            #Creamos una funcion y nueva ventana para el registro de usuarios
    newVentana=tkk.Toplevel(ventanal)           
    newVentana.title("Registro de Usuario")    #Definimos titulo de la ventana
    newVentana.geometry("390x290+650+250")     #Definimos dimenciones
    newVentana['bg']=color                     
    
    labelExample=tkk.Label(newVentana,text="Nuevo Usuario ",bg=color,font=("Arial Black",12)).pack(side="top")  #Ingresamos titulo 
    panel_reg=tkk.Label(newVentana,image=photo_reg).pack(side="left")               #Mostramos la posicion de la imagen 'left' (Izquierda)

    Label(newVentana,text="Nombre : ",bg=color,font=("Arial Black",9)).pack()      #Mostramos el dato a pedir
    caja3=Entry(newVentana)                                                         ##Creamos la caja de respuesta para el nombre
    caja3.pack()
    Label(newVentana,text="Apellidos : ",bg=color,font=("Arial Black",9)).pack()   #Mostramos el dato a pedir
    caja4=Entry(newVentana)                                                         ##Creamos la caja de respuesta para apellidos
    caja4.pack()
    Label(newVentana,text="Usuario : ",bg=color,font=("Arial Black",9)).pack()     #Mostramos el dato a pedir
    caja5=Entry(newVentana)                                              
    caja5.pack()
    Label(newVentana,text="Contraseña : ",bg=color,font=("Arial Black",9)).pack()  #Mostramos el dato a pedir
    #En esta linea definimos que los valores de la caja de respuesta muestren ** en la contraseña
    caja6=Entry(newVentana,show="*")                                                
    caja6.pack()
    #Mostrar el siguiente recuadro de instruccion
    Label(newVentana,text="Verifique Contraseña : ",bg=color,font=("Arial Black",9)).pack()    #Mostramos el dato a pedir 
    #En esta linea definimos que los valores de la caja de respuesta muestren ** en la contraseña 
    caja7=Entry(newVentana,show="*")                                                            
    caja7.pack()
    
#Creamos una funcion para registrar los datos a la bd
 
    def registro():
        #Obtenemos los valores de las cajas de respuesta
        Nombre=caja3.get()          
        Apellido=caja4.get()        
        Usr_reg=caja5.get()         
        Contra_reg=caja6.get()      
        Contra_reg_2=caja7.get()
        
        if(Contra_reg==Contra_reg_2):       #Verificamos las contraseñas
                                            #Insertamos los datos en el registro
            c.execute("INSERT INTO usuarios values(\'"+Nombre+"\',\'"+Apellido+"\',\'"+Usr_reg+"\',\'"+Contra_reg+"')")
            db.commit()         
            mb.showinfo(title="Registro Correcto",message="Hola, "+Nombre+" "+Apellido+" \nSu registro fue exitoso.")
            newVentana.destroy()            #Destrumos la ventana
        else:
            mb.showerror(title="Contraseña Incorrecta",message="Error \nLas contraseñas no coinciden.") #Mostramos una alerta
        
    #Se guardan los datos del nuevo registro
    buttons=tkk.Button(newVentana,text="Registrar",command=registro,bg='bisque2',font=("Arial Rounded MT Bold",10)).pack(side="bottom")
    
Label(ventanal,text=" ",bg=color,font=("Arial",10)).pack()      
Button(text=" ENTRAR ",command=login,bg='bisque2',font=("Arial Rounded MT Bold",10)).pack()   #Boton de entrar
Label(ventanal,text=" ",bg=color,font=("Arial Black",10)).pack()
Label(ventanal,text=" ",bg=color,font=("Arial Black",10)).pack()                             
#Llamaos la nueva ventana 
boton1=Button(ventanal,text="Crear una cuenta",bg='bisque2' ,command=nuevaVentana,font=("Arial Rounded MT Bold",10)).pack()

ventanal.mainloop()

