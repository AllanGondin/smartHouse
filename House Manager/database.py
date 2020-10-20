import mysql.connector
import functions

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "24903196",
    database = "gerenciador",
    port = "3306"
)

servo = db.cursor()

def Select_hashid(lista):  #faz select no database

    servo.execute("SELECT `cod_id` FROM disp_infos")
    result = servo.fetchall()
    for row in result:
        lista.append(row[0])  #O resultado do select vem em várias linhas e colunas. Aqui pego só a 1ª coluna de cada linha
    else:
        print("\nOs dispositivos foram carregados! \n")
        return lista

def Select_comodo(hashid):
    servo.execute(f"SELECT `comodo` FROM disp_infos WHERE `cod_id` = '{hashid}'")
    result = servo.fetchone()
    for row in result:

        return row

def Update_status(hashid, status, comodo):
    nome = functions.separa_nome(hashid)
    servo.execute(f"UPDATE {comodo} SET `status_dispositivo` = '{status}'  WHERE `cod_id` = '{hashid}'")
    db.commit()
    print(f"O status do dispositivo {nome} foi alterado para {status}!")
    
    
 