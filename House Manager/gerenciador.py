import os
import database
import functions


hashid = []  #lista vazia para receber os hash id do banco

hashid = database.Select_hashid(hashid)
print(f"Dispositivos:{hashid}")
print("----------------------------------------------------")
functions.Execute_ping(hashid)






     