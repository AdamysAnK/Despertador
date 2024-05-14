import datetime as dt
from customtkinter import *


# def despertar():
#     alarme = ('09:01:00')#so colocar um input nisso ou chockbox e ja era


        
def pegar_info():
    global cont,alarmes
    # pegar horas
    pegar_hora = box_hora.get()
    pegar_min = box_min.get()
    pegar_seg = box_seg.get()
    
    # pegar dias
    pegar_1=seg.get()
    pegar_2=ter.get()
    pegar_3=quar.get()
    pegar_4=quin.get()
    pegar_5=sex.get()
    pegar_6=sab.get()
    pegar_7=dom.get()
    
    
    dias_para_despertar = []#vou fazer um for, vai guardar o dia que é pra despertar

    if pegar_1 != 0: 
        dias_para_despertar.append(pegar_1)
    if pegar_2 != 0:
        dias_para_despertar.append(pegar_2)
    if pegar_3 != 0:
        dias_para_despertar.append(pegar_3)
    if pegar_4 != 0:
        dias_para_despertar.append(pegar_4)
    if pegar_5 != 0:
        dias_para_despertar.append(pegar_5)
    if pegar_6 != 0:
        dias_para_despertar.append(pegar_6)
    if pegar_7 != 0:
        dias_para_despertar.append(pegar_7)
    alarme_inteiro=[] #onde fica armazenado o alarme inteiro 
                # o dia: a hora : e segundos.
    for dia in dias_para_despertar:


         var_alarme_inteiro = f"""{dia} {pegar_hora}:{pegar_min}:{pegar_seg}"""#tentar fazer um variavel que muda automaticamente
         alarme_inteiro.append(var_alarme_inteiro)
    
    cont=1
    
    
    
    janela_add_clock.destroy()
    


def ver_hora():
    global agora_string,agora,dia
    agora = dt.datetime.now()
    dia_atual = agora.strftime("%w")
    if dia_atual == '0':
        dia = "Domingo"      
    if dia_atual == '6':
        dia = "Sábado"  
    if dia_atual == '5':
        dia = "Sexta"
    if dia_atual == '4':
        dia = "Quinta"
    if dia_atual == '3':
        dia = "Quarta"
    if dia_atual == '2':
        dia = "Terça"
    if dia_atual == '1':
        dia = "Segunda"
        
    agora_string = agora.strftime(f"""{dia} %H:%M:%S""")
    
   

    label_hora = CTkLabel(janela, text=agora_string,font=('Arial',10))
    label_hora.place(x=3, y=10)
    
    
    label_hora.after(100,ver_hora)



cont=1
# funçao abrir nova janela
def nova_janela():
    global janela_add_clock,cont,box_hora,box_min,seg,box_seg,ter,quar,quin,sex,sab,dom
    if cont==1:
        cont+=1

        janela_add_clock = CTk()
        
        janela_add_clock.title("")
        
        # janela_add_clock.iconphoto(False,"imagens.png","png")
        
        janela_add_clock.geometry('420x300')
        
        janela_add_clock.resizable(width=FALSE,height=False)
        # horas
        label_hora = CTkLabel(janela_add_clock, text="Hora",font=("Arial",20))
        label_hora.place(x=10, y=20)
        
        hora = tuple(str(i).zfill(2) for i in range(24))
        box_hora = CTkComboBox(janela_add_clock,values=hora,width=60,height=30)
        box_hora.place(x=10, y=50)
        
        # minutos
        minutos = tuple(str(i).zfill(2) for i in range(60))

        label_min = CTkLabel(janela_add_clock, text="Minutos",font=("Arial",20))
        label_min.place(x=170, y=20)
        
        box_min = CTkComboBox(janela_add_clock,values = minutos,width=60,height=30)
        box_min.place(x=170, y=50)
        
        # segundos
        segundos = tuple(str(i).zfill(2) for i in range(60))
        
        label_min = CTkLabel(janela_add_clock, text="Segundos",font=("Arial",20))
        label_min.place(x=320, y=20)
        
        box_seg = CTkComboBox(janela_add_clock,values = segundos,width=60,height=30)
        box_seg.place(x=320, y=50)
        
        # DIAS_________________
        seg = CTkCheckBox(janela_add_clock,text='Seg',onvalue='Segunda',offvalue=0)
        seg.place(x=10, y=90)
        
        ter = CTkCheckBox(janela_add_clock,text='Ter',onvalue='Terça',offvalue=0)
        ter.place(x=70, y=90)
        
        quar = CTkCheckBox(janela_add_clock,text='Quar',onvalue='Quarta',offvalue=0)
        quar.place(x=125, y=90)
        
        quin = CTkCheckBox(janela_add_clock,text='Quin',onvalue='Quinta',offvalue=0)
        quin.place(x=185, y=90)
        
        sex = CTkCheckBox(janela_add_clock,text='Sext',onvalue='Sexta',offvalue=0)
        sex.place(x=245, y=90)
        
        sab = CTkCheckBox(janela_add_clock,text='Sab',onvalue='Sábado',offvalue=0)
        sab.place(x=305, y=90)
        
        dom = CTkCheckBox(janela_add_clock,text='Dom',onvalue='Domingo',offvalue=0)
        dom.place(x=360, y=90)
        # Button_pegar_info
        button_pegar_info = CTkButton(janela_add_clock,text="Adicionar alarme",command=pegar_info)
        button_pegar_info.place(x=140, y=180)
        

        janela_add_clock.mainloop()
        


    else:
        cont=1
        janela_add_clock.destroy()
        
        
        

    

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


