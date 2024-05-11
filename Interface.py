from tkinter import *
import datetime as dt
from customtkinter import *
# import pygame as pg
#fkfkkf
#cwncchingi
#rlr

# def despertar():
#     alarme = ('09:01:00')#so colocar um input nisso ou chockbox e ja era

#     if agora_string == alarme and ligado == True:
#         print("despertou!!")
        
    
def ver_hora():
    global agora_string
    agora = dt.datetime.now()
    agora_string = agora.strftime("%H:%M:%S")    

    label_hora = CTkLabel(janela, text=agora_string)
    label_hora.place(x=15, y=10)
    label_hora.after(100,ver_hora)

# funçao abrir nova janela
def nova_janela():
    cont=1
    if cont==1:
        janela_add_clock = CTk()
        
        janela_add_clock.geometry('400x300')
        
        janela_add_clock.resizable(width=FALSE,height=False)
        # horas
        label_hora = CTkLabel(janela_add_clock, text="Hora",font=("Arial",20))
        label_hora.place(x=10, y=20)
        
        hora = ('01','02','03','04','05','06','07','08','09','10','11','12')
        box_hora = CTkComboBox(janela_add_clock,values=hora,width=60,height=30)
        box_hora.place(x=10, y=50)
        
        # minutos
        minutos = tuple(str(i).zfill(2) for i in range(60))

        label_min = CTkLabel(janela_add_clock, text="Minutos",font=("Arial",20))
        label_min.place(x=100, y=20)
        
        box_min = CTkComboBox(janela_add_clock,values = minutos,width=60,height=30)
        box_min.place(x=100, y=50)
        
        # segundos
        segundos = tuple(str(i).zfill(2) for i in range(60))
        
        label_min = CTkLabel(janela_add_clock, text="Segundos",font=("Arial",20))
        label_min.place(x=200, y=20)
        
        box_min = CTkComboBox(janela_add_clock,values = segundos,width=60,height=30)
        box_min.place(x=210, y=50)
        
        # PM/AM
        fuso = CTkComboBox(janela_add_clock,values=('PM','AM'),width=60,height=30)
        fuso.place(x= 310, y= 50)       
    
        
        janela_add_clock.mainloop()

janela = CTk()

janela.config(bg= "#363636")

janela.geometry("800x500")

janela.resizable(width=FALSE,height=False)

janela.title("")


# Label cronometro
label_crono = CTkLabel(janela, text="Despertador",font=("Arial bold",50),bg_color="#363636")
label_crono.place(x=300, y=10)

    

# Labels
label_lado=CTkLabel(janela, text='',height=700,width=80)
label_lado.grid(row=0,column=0)





    
    

# Coloca as funções aqui apolo
botao_adicionar_alarme = CTkButton(janela, text="+",width=20,height=20,font=("Arial",20),command=nova_janela)
botao_adicionar_alarme.place(x=28, y=400)

botao_remover_alarme = CTkButton(janela, text="-",width=27,height=27,font=("Arial",20))
botao_remover_alarme.place(x=28, y=440)




ver_hora()


janela.mainloop()
