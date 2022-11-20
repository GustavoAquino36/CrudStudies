from getpass import *
import csv
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def csvfile():
    with open('C:/Users/Gustavo/Desktop/Estudo/crudEstudo/CrudStudies/logInfo.csv', 'r') as userscsv:
        linhas = csv.reader(userscsv, delimiter = ',')
        data = []
        for log in linhas:
            data.append(log)
    for i in data:
        print(i)
    
def userinfo():
    with open('C:/Users/Gustavo/Desktop/Estudo/crudEstudo/CrudStudies/userInfo.csv', 'r') as usersinfo:
        linhas = csv.reader(usersinfo, delimiter=',')
        data = {}
        for log in linhas:
            data[log[0]] = log[1:]
        print(data)

def mainMenu():
    clear()
    global escolha
    escolha = input('''
========== CRUD Menu ==========

[1] Registrar novo login
[2] b
[3] c
[4] d
[0] Fechar programa\n ''')

def cursor():
    if escolha == '1':
        return registra()

def loga(): # Log will be important later on
    user = input('Login: ')
    senha = getpass('Senha: ')
    logou = False
    data = open('txt data base path here', 'r')
    for log in data:
        nome, password = log.split(',')
        password = password.strip()
        if nome == user and password == senha:
            logou = True
    if logou:
        mainMenu()
    else:
        print('banido')

def registra():
    try:
        user = input('User a ser registrado: ')
        senha = getpass('Senha a ser registrada: ')
        data = open('txt data base path here', 'a')
        data.write(f'\n{user},{senha}')
    finally:
        return mainMenu()

userinfo() # learning about csv as the codes goes, still simple usage, improving...

