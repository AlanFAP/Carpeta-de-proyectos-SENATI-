from tkinter import *

sis=Tk()
sis.config(bd=15)
sis.geometry("700x550")
sis["bg"]="#95a5a6"

dni =StringVar()
ape =StringVar()
nom =StringVar()
dir=StringVar()
tel=StringVar()
total =StringVar()

Label(sis, text="DNI").place(x=22, y=70)
Entry(sis, justify=CENTER, textvariable=dni).place(x=22, y=100)
Label(sis, text="Apellido" ).place(x=22, y=130)
Entry(sis, justify=CENTER, textvariable=ape).place(x=22, y=160)
Label(sis, text="Nombres").place(x=22, y=190)
Entry(sis, justify=CENTER, textvariable=nom).place(x=22, y=220)
Label(sis, text="Direccion").place(x=22, y=250)
Entry(sis, justify=CENTER, textvariable=dir, width="40").place(x=22, y=280)
Label(sis, text="Telefono").place(x=300, y=250)
Entry(sis, justify=CENTER, textvariable=tel).place(x=300, y=280)

Label(sis, text="Codigo").place(x=22, y=340)
Label(sis, text="Descripcion").place(x=102, y=340)
Label(sis, text="Uniadad").place(x=202, y=340)
Label(sis, text="Cantidad").place(x=302, y=340)
Label(sis, text="Precio").place(x=402, y=340)
Label(sis, text="Subtotal").place(x=502, y=340)
cod1 =StringVar()
cod2 =StringVar()
cod3 =StringVar()
cant1 =StringVar()
cant2 =StringVar()
cant3 =StringVar()
Entry(sis, justify=CENTER, textvariable=cod1, width="10").place(x=22, y=370)
Entry(sis, justify=CENTER, textvariable=cod2, width="10").place(x=22, y=400)
Entry(sis, justify=CENTER, textvariable=cod3, width="10").place(x=22, y=430)
Entry(sis, justify=CENTER, textvariable=cant1, width="10").place(x=302, y=370)
Entry(sis, justify=CENTER, textvariable=cant2, width="10").place(x=302, y=400)
Entry(sis, justify=CENTER, textvariable=cant3, width="10").place(x=302, y=430)

Label(sis, text="Total").place(x=452, y=470)
Entry(sis, justify=CENTER, textvariable=cant3, width="10").place(x=502, y=470)

Button(sis, text="Calculo").place(x=302, y=470)
sis.mainloop()