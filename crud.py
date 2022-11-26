from getpass import *
import csv
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fecha():
    clear()
    print('Obrigado por utilizar meu CRUD, Finalizando...\nFeedbacks para github.com/Gustavoaquino36')

def mainMenu():
    clear()
    global escolha
    escolha = input('''
========== CRUD Menu ==========

[1] Registrar novo login
[2] Consulta de usuario
[3] Edite usuarios (login necessario)
[4] Deletar usuarios
[0] Fechar programa\n ''')
    cursor()

def cursor():
    if escolha == '1':
        return register()
    elif escolha == '2':
        return userinfo()
    elif escolha == '3':
        return editUser()
    elif escolha == '4':
        return deleteUser(), deleteinfo()
    elif escolha == '0':
        return fecha()
    else:
        return mainMenu()

def register():
    clear()
    try:
        user = input('User a ser registrado: ')
        senha = getpass('Senha a ser registrada: ')
        data = open('logInfo.csv', 'a')
        data.write(f'{user},{senha}\n')
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
        noUserError = input(f'User {user} nao encontrado ou sem informacoes registradas\npressione qualquer botao para voltar ao menu')
        mainMenu()

def checkinfo():
    try: 
        readUsers = open('userInfo.csv', 'r')
        linhas = csv.reader(readUsers, delimiter=',')
        info = {}
        for j in linhas:
            info[j[0]] = j[:1]
        if str(info[userlogin]) == str(f"['{userlogin}']"):
            editInfo()
    except KeyError:
        addinfo()

def editUser():
    clear()
    global userlogin
    print('Login é necessario para adicionar informacoes ao proprio user!')
    userlogin = input('User: ')
    senha = getpass('Senha: ')
    userscsv = open('logInfo.csv', 'r')
    linhas = csv.reader(userscsv, delimiter=',')
    users = []
    for log in linhas:
        users.append(log)
    logou = False
    for i in users:
        if i[0] == userlogin and i[1] == senha:
            logou = True
            if logou:
                checkinfo()
    if not logou:
        print('Usuario nao encontrado,')
        input('Pressione qualquer botão para voltar ao menu inicial.')
        mainMenu()

def editInfo():
    readUsers = open('userInfo.csv', 'r')
    linhas = csv.reader(readUsers, delimiter=',')
    userDetail = {}
    for log in linhas:
        userDetail[log[0]] = log[1:]
    clear()
    print(f'User: {userlogin} \nEmail: {userDetail[userlogin][0]} \nLinkedin: {userDetail[userlogin][1]}')
    email = input("Novo email : ")
    linkedin = input("Novo linkedin : ")
    for data in userDetail:
        if data == userlogin:
            update = True
    if update:     
        userDetail = (f'{userlogin},{email},{linkedin}')
        updatedinfo = []
    with open("userInfo.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
          if not row[0] == userlogin:
            updatedinfo.append(row)
        updateinfo(updatedinfo)
    data2 = open('userInfo.csv', 'a')
    data2.write(f'{userDetail}\n')
    input('pressione qualquer botao para voltar ao menu')
    mainMenu()

def addinfo():
    lerlog = open('logInfo.csv', 'r')
    csvlog = csv.reader(lerlog, delimiter=',')
    users = []
    for log in csvlog:
        users.append(log)
    for i in users:
        if i[0] == userlogin:
            email = input('Email a ser vinculado ao usuario logado: ')
            linkedin = input('Linkedin (/user): ')
            data = open('userInfo.csv', 'a')
            data.write(f'{i[0]},{email},{linkedin}\n')
            backToMenu = input('[0] para voltar ao menu\n')
            if backToMenu == '0':
                mainMenu()
            else:
                mainMenu()

def deleteUser():
    global duser
    clear()
    updatedlist = []
    with open("logInfo.csv", newline="") as csvfile:
      reader = csv.reader(csvfile)
      duser = input("Nome do User a ser removido:\n")
      for row in reader:
          if not row[0] == duser:
              updatedlist.append(row)
      print('User Removido com sucesso!')
      updatefile(updatedlist)

def updatefile(updatedlist):
    with open("logInfo.csv", "w", newline="") as csvfile:
        Writer = csv.writer(csvfile)
        Writer.writerows(updatedlist)
    backToMenu = input('[0] para voltar ao menu\n')
    if backToMenu == '0':
        mainMenu()
    else:
        clear()
        updatefile(updatedlist)

def deleteinfo():
    clear()
    updatedinfo = []
    with open("userInfo.csv", newline="") as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          if not row[0] == duser:
              updatedinfo.append(row)
      updateinfo(updatedinfo)

def updateinfo(updatedinfo):
    with open("userInfo.csv", "w", newline="") as csvinfo:
        Writer = csv.writer(csvinfo)
        Writer.writerows(updatedinfo)

mainMenu()
