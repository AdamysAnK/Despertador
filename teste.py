import datetime 

while True:
    # Usaremos essa estrutura para sempre atualizar o valor da hora/minutos/segundos
    agora = datetime.datetime.now()
    agora_string = agora.strftime("%I:%M:%S")
    print(agora_string)
    break
    
    
    
print(datetime.time(1,3,5))

#podemos usar ele para quando o horario chegar ele despertar
# é possível criarmos um data e um tempo, ou criarmos uma variável que tenha tanto a data quanto a hora, usando ele

# if hora_limite == hora_atual:
#     desperter