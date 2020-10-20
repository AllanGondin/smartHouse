import os 
import re
import database

#FUNÇÃO PRINCIPAL EXECUTA PING
def Execute_ping(hashid):

    status = ""

    print("\nEXECUTANDO PING, AGUARDE...\n")

    for hid in hashid:    #passa cada elemento da hasdhid para a variavel hid

        nome = separa_nome(hid) #extrai nome do Hashid
        ip = separa_ip(hid) #extrai ip do Hashid
        comodo = database.Select_comodo(hid) #retorna a tabela especifica do dispositivo
        
        resposta = os.popen(f"ping {ip}").read()  #printa e armazena o resultado do subprocesso dentro da variavel resposta  
                                                      #o f permite que você forme uma string com texto e um elemento do python
        if "Recebidos = 4" in resposta:
            status = "Ativo"
            print(f"\nO Dispositivo {nome} está Ativo\n")
            database.Update_status(hid, status, comodo)   #atualiza no banco o status para ativo

        else: 
            status = "Inativo" 
            print(f"\nO Dispositivo {nome} está Inativo\n")
            database.Update_status(hid, status, comodo)    #atualiza no banco o status para inativo

#FUNÇÃO SEPARA IP DO HASH ID
def separa_ip(entrada):
    saida = re.search(r"(?<=\#).*", entrada).group()  #regex

    return saida

#FUNÇÃO EXTRAI NOME DO HASH ID
def separa_nome(entrada):
    saida= re.search(r".*(?=\#)", entrada).group()  #regex

    return saida
     
    
        
                
