from tkinter import *
import datetime as dt
from customtkinter import *





janela = CTk()

janela.config(bg= "#363636")

janela.geometry("800x500")

janela.resizable(width=FALSE,height=False)

janela.title("")


# Label cronometro
label_crono = CTkLabel(janela, text="Despertador",font=("Arial bold",50),bg_color="#363636")
label_crono.place(x=300, y=10)

def ver_hora():
    agora = dt.datetime.now()
    agora_string = agora.strftime("%I:%M:%S")    
    label_hora = CTkLabel(janela, text=agora_string)
    label_hora.place(x=15, y=10)

    label_hora.after(100,ver_hora)
    
ver_hora()

# Labels
label_lado=CTkLabel(janela, text='',height=700,width=80)
label_lado.grid(row=0,column=0)


# Coloca as funções aqui apolo
botao_adicionar_alarme = CTkButton(janela, text="+",width=20,height=20,font=("Arial",20))
botao_adicionar_alarme.place(x=28, y=400)

botao_remover_alarme = CTkButton(janela, text="-",width=27,height=27,font=("Arial",20))
botao_remover_alarme.place(x=28, y=440)







janela.mainloop()
