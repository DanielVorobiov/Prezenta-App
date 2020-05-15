import datetime
import pytz
import pandas as pd
import xlrd
from openpyxl import Workbook

def timp():
  utc_now = pytz.utc.localize(datetime.datetime.utcnow())
  local_now = utc_now.astimezone(pytz.timezone("Europe/Chisinau"))
  current_time = local_now.strftime("%H:%M:%S")
  return current_time
#strftime = string format time


lista = pd.DataFrame(columns=['Nume','Ora sosirii','Ora plecarii'])


def venit():
  
  for row in range(lista.shape[0],75):
    timp()
    nume = input("A venit: ")
    if nume == "/":
      menu()
      break
    for i,index in lista.iterrows():
      unique = i
      name = index["Nume"]
      if nume ==name:
        lista.loc[unique,"Ora plecarii"] = ""
        row +=1
        venit()
    lista.loc[row] = [nume,timp(),""]
    print(lista)
    row +=1
  venit()


def plecat():
  left = input("A plecat: ")
  for i,row in lista.iterrows():
    unique = i
    name = row["Nume"]
    if left == name:
      lista.loc[unique,"Ora plecarii"] =timp()
    
    #print(str(unique) +". "+ name)
  

def menu():
  print("1. A venit cineva nou")
  print("2. A plecat cineva")
  print("3. Vezi lista")
  print("4. Ședința s-a terminat")
  pick = input("Pick one: ")
  if pick == str(1):
    venit()
  elif pick== str(2):
    plecat()
  elif pick == str(3):
    print(lista)
  else:
    print("Please pick one of above")
    menu()


menu()