from getpass import *
import csv
import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mainMenu():
    clear()
    global escolha
    escolha = input('''
========== CRUD Menu ==========

[1] Registrar novo login
[2] Consulta de usuario
[3] c
[4] Deletar usuarios
[0] Fechar programa\n ''')
    cursor()

def cursor():
    if escolha == '1':
        return register()
    elif escolha == '2':
        return userinfo()
    elif escolha == '4':
        return deleteUser()
    elif escolha == '0':
        sys.exit

def register():
    clear()
    try:
        user = input('User a ser registrado: ')
        senha = getpass('Senha a ser registrada: ')
        data = open('logInfo.csv', 'a')
        data.write(f'\n{user},{senha}')
    finally:
        return mainMenu()

def userinfo():
    global user, userDetail
    clear()
    user = input('Qual user Quer puxar as informacoes? (email e linkedin)\n').casefold()
    readUsers = open('userInfo.csv', 'r')
    linhas = csv.reader(readUsers, delimiter=',')
    userDetail = {}
    for log in linhas:
        userDetail[log[0]] = log[1:]
    showUserInfo()

def showUserInfo():
    try:
        clear()
        info = print(f'User: {user} \nEmail: {userDetail[user][0]} \nLinkedin: {userDetail[user][1]}')
        backToMenu = input(f'[0] Para retornar ao menu inicial\n ')
        while not backToMenu == '0':
            showUserInfo()
        else:
            mainMenu()
    except KeyError:
        noUserError = input(f'User {user} nao encontrado, Gostaria de Registra-lo?\n')
        if noUserError.casefold() in ['sim','yes','y','s','quero']:
            register()
        else:
            mainMenu()

def loginfo():
    userscsv = open('logInfo.csv', 'r')
    linhas = csv.reader(userscsv, delimiter=',')
    users = []
    for log in linhas:
        users.append(log)
    for i in users:
        print(i)

def deleteUser():
    clear()
    updatedlist = []
    with open("logInfo.csv", newline="") as csvfile:
      reader = csv.reader(csvfile)
      user = input("Nome do User a ser removido:\n")
      for row in reader:
          if not row[0] == user:
              updatedlist.append(row)
      print('User Removido com sucesso!')
      updatefile(updatedlist)

def updatefile(updatedlist):
    with open("logInfo.csv", "w", newline="") as csvfile:
        Writer = csv.writer(csvfile, lineterminator='')
        Writer.writerows(updatedlist)
    backToMenu = input('[0] para voltar ao menu\n')
    if backToMenu == '0':
        mainMenu()
    else:
        clear()
        updatefile(updatedlist)

mainMenu()