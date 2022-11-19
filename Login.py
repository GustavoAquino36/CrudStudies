from getpass import *
import os

def mainMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
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

def loga():
    user = input('Login: ')
    senha = getpass('Senha: ')
    logou = False
    data = open('txt data base path here', 'r')
    for log in data:
        nome, password = log.split(' - ')
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
        data.write(f'\n{user} - {senha}')
    finally:
        return mainMenu()