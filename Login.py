from getpass import *
import csv
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def csvfile():
    userscsv = open('logInfo.csv', 'r')
    linhas = csv.reader(userscsv, delimiter = ',')
    dataarray = []
    for log in linhas:
        dataarray.append(log)
    for i in dataarray:
        print(i)
    
def userinfo():
    global user, dataobj
    clear()
    user = input('Qual user Quer puxar as informacoes? (email e linkedin)\n').casefold()
    ruser = open('userInfo.csv', 'r')
    linhas = csv.reader(ruser, delimiter=',')
    dataobj = {}
    for log in linhas:
        dataobj[log[0]] = log[1:]
    showUserInfo()
def showUserInfo():
    try:
        clear()
        info = print(f'User: {user} \nEmail: {dataobj[user][0]} \nLinkedin: {dataobj[user][1]}')
        backToMenu = input(f'[0] Para retornar ao menu inicial\n ')
        while not backToMenu == '0':
            showUserInfo()
        else:
            mainMenu()
    except KeyError:
        noUserError = input(f'User {user} nao encontrado, Gostaria de Registra-lo?\n')
        if noUserError.casefold() in ['sim','yes','y','s','quero']:
            registra()
        else:
            mainMenu()

def mainMenu():
    clear()
    global escolha
    escolha = input('''
========== CRUD Menu ==========

[1] Registrar novo login
[2] Consulta de usuario
[3] c
[4] d
[0] Fechar programa\n ''')
    cursor()

def cursor():
    if escolha == '1':
        return registra()
    elif escolha == '2':
        return userinfo()

def registra():
    clear()
    try:
        user = input('User a ser registrado: ')
        senha = getpass('Senha a ser registrada: ')
        data = open('txt data base path here', 'a')
        data.write(f'\n{user},{senha}')
    finally:
        return mainMenu()

mainMenu()