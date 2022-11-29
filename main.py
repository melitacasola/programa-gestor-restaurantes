from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ''

precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]



def click_btn(nro):
    global operador
    operador = operador + nro
    visor_calc.delete(0, END)
    visor_calc.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calc.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calc.delete(0, END)
    visor_calc.insert(0, resultado)
    operador = ''


# checkbuttons
def revisar_check():
    x = 0
    for c in cuadro_comida:
        if variable_comidas[x].get() == 1:
            cuadro_comida[x].config(state=NORMAL)
            if cuadro_comida[x].get() == '0':
                cuadro_comida[x].delete(0, END)
            cuadro_comida[x].focus()
        else:
            cuadro_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_bebida:
        if variable_bebidas[x].get() == 1:
            cuadro_bebida[x].config(state=NORMAL)
            if cuadro_bebida[x].get() == '0':
                cuadro_bebida[x].delete(0, END)

            cuadro_bebida[x].focus()
        else:
            cuadro_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadro_postres:
        if variable_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebidas.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postres.set(f'$ {round(sub_total_postres, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuestos.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: \t{num_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*56+'\n')

    texto_recibo.insert(END, 'Items\t\tCant.\t\tCosto Items\n')
    texto_recibo.insert(END, f'-'*66+'\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'$ {int(postres.get()) * precios_postres[x]}\n')
        x += 1

    texto_recibo.insert(END, f'-' * 66 + '\n')
    texto_recibo.insert(END, f' Costo de la Comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f' Costo de la Bebida: \t\t\t{var_costo_bebidas.get()}\n')
    texto_recibo.insert(END, f' Costo de la Postres: \t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 66 + '\n')
    texto_recibo.insert(END, f' Sub-total: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f' Impuestos: \t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f' Total: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 56 + '\n')
    texto_recibo.insert(END, 'GraciaSS, vuelvas prontos')



def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')



def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadro_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variable_comidas:
        v.set(0)
    for v in variable_bebidas:
        v.set(0)
    for v in variable_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')


# iniciar tkinter
aplicacion = Tk()

# tamaño ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# color de fondo y ventana
aplicacion.config(bg='cadet blue')


# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
#donde ? es uno solo el superior arriba de todo
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_tit = Label(panel_superior, text="Sistema de Facturacion", fg='white',
                     font=('Dosis', 38, 'bold'), bg='cadet blue', width=27)
etiqueta_tit.grid(row=0, column=0)

# panel izquierdo
panel_izq = Frame(aplicacion, bd=1, relief=FLAT)
panel_izq.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izq, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# panel de comidas
panel_comidas = LabelFrame(panel_izq, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izq, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izq, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# Panel derecha
panel_dcha = Frame(aplicacion, bd=1, relief=FLAT)
panel_dcha.pack(side=RIGHT)

# panel calc
panel_calc = Frame(panel_dcha, bd=1, relief=FLAT, bg='cadet blue')
panel_calc.pack()

# panel recibo
panel_recibo = Frame(panel_dcha, bd=1, relief=FLAT, bg='cadet blue')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_dcha, bd=1, relief=FLAT, bg='cadet blue')
panel_botones.pack()


# lista de productos
lista_comidas = ['empanadas', 'pollo', 'costeleta', 'pizza1', 'pizza2', 'ñoquis', 'tarta', 'asadito']
lista_bebidas = ['soda', 'gaseoasa', 'cerveza', 'cerveza2', 'vino', 'vino2', 'cafe', 'insfusiones']
lista_postres= ['budin', 'helado', 'tiramisu', 'flan', 'ensalda de frutas', 'brownie', 'medialuna', 'membrillo y queso']


# generar items comidas:
variable_comidas = []
cuadro_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    # crear checkbutton
    variable_comidas.append('')
    variable_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 12, 'bold',),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_comidas[contador],
                         command=revisar_check)


    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear los cuadros de entrada
    cuadro_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadro_comida[contador] = Entry(panel_comidas,
                                     font=('Dosis', 14, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadro_comida[contador].grid(row=contador,
                                  column=1)
    contador += 1


# generar items bebidas:
variable_bebidas = []
cuadro_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    #crear checkbutton
    variable_bebidas.append('')
    variable_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_bebidas[contador],
                         command=revisar_check)

    bebida.grid(row=contador,
                column=0,
                sticky=W)

    #cuadro de entradas
    cuadro_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadro_bebida[contador] = Entry(panel_bebidas,
                                    font=('Dosis', 14, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadro_bebida[contador].grid(row=contador,
                                 column=1)
    contador += 1


# generar items postres:
variable_postres = []
cuadro_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    #crear checkbutton
    variable_postres.append('')
    variable_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 12, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variable_postres[contador],
                         command=revisar_check)

    postre.grid(row=contador,
                column=0,
                sticky=W)

    # cuadro de entradas
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadro_postres[contador] = Entry(panel_postres,
                                    font=('Dosis', 14, 'bold'),
                                    bd=1,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                 column=1)
    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebidas = StringVar()
var_costo_postres = StringVar()
var_subtotal = StringVar()
var_impuestos = StringVar()
var_total = StringVar()


# etiquetas de costo y campos de entrada
# Comidas
etiqueta_costo_comida = Label(panel_costos,
                               text='Costo Comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=8,
                            state='readonly',
                            textvariable=var_costo_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)

# bebidas
etiqueta_costo_bebidas = Label(panel_costos,
                       text='Costo Bebidas',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_costo_bebidas.grid(row=1, column=0)
texto_costo_bebidas = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=8,
                            state='readonly',
                            textvariable=var_costo_bebidas)

texto_costo_bebidas.grid(row=1, column=1)

# postres
etiqueta_costo_postres = Label(panel_costos,
                               text='Costo Postres',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_postres.grid(row=2, column=0)
texto_costo_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=8,
                            state='readonly',
                            textvariable=var_costo_postres)

texto_costo_postres.grid(row=2, column=1)


#subtotal
etiqueta_subtotal = Label(panel_costos,
                       text='Sub-total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_subtotal)

texto_subtotal.grid(row=0, column=3)

#impuestos
etiqueta_impuestos = Label(panel_costos,
                       text='Impuestos',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_impuestos.grid(row=1, column=2, padx=41)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_impuestos)

texto_impuestos.grid(row=1, column=3)

#Total
etiqueta_total = Label(panel_costos,
                       text='Total $',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=8,
                        state='readonly',
                        textvariable=var_total)

texto_total.grid(row=2, column=3)


#botones
botones = ['total', 'recibo', 'guardar', 'resetear']
botones_creados = []

columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 12, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=9)

    botones_creados.append(boton)

    boton.grid(row=0,
               column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)


# area de recibo
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 11, 'bold'),
                    bd=1,
                    width=50,
                    height=10)
texto_recibo.grid(row=0, column=0)


#calculadora
visor_calc = Entry(panel_calc,
                   font=('Dosis', 16, 'bold'),
                   width=32,
                   bd=1)

visor_calc.grid(row=0,
                column=0,
                columnspan=4)

botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-',
                '1', '2', '3', 'x', 'CE', 'Borrar', '0', '/']

btn_guardados = []

fila = 1
columna = 0

for boton in botones_calc:
    boton = Button(panel_calc,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg= 'azure4',
                   bd=1,
                   width=7)
    btn_guardados.append(boton)
    #ubicar botones
    boton.grid(row=fila, column=columna)

    if columna == 3:
        fila += 1
    columna += 1

    if columna == 4:
        columna = 0

btn_guardados[0].config(command=lambda : click_btn('7'))
btn_guardados[1].config(command=lambda : click_btn('8'))
btn_guardados[2].config(command=lambda : click_btn('9'))
btn_guardados[3].config(command=lambda : click_btn('+'))
btn_guardados[4].config(command=lambda : click_btn('4'))
btn_guardados[5].config(command=lambda : click_btn('5'))
btn_guardados[6].config(command=lambda : click_btn('6'))
btn_guardados[7].config(command=lambda : click_btn('-'))
btn_guardados[8].config(command=lambda : click_btn('1'))
btn_guardados[9].config(command=lambda : click_btn('2'))
btn_guardados[10].config(command=lambda : click_btn('3'))
btn_guardados[11].config(command=lambda : click_btn('*'))
btn_guardados[14].config(command=lambda : click_btn('0'))
btn_guardados[15].config(command=lambda : click_btn('/'))
btn_guardados[13].config(command=borrar)
btn_guardados[12].config(command=obtener_resultado)



#evitar que pantalla se cierre:
aplicacion.mainloop()