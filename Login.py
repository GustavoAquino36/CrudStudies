from pwinput import pwinput

def entrar():
    global cursor
    print('Olá, Bem vindo ao teste de Login')
    cursor = input('Gostaria de Entrar ou se registrar?\n')

def sistema():
    global user, senha
    if cursor.casefold() in ['entrar', 'logar', 'acessar', 'login', 'log']:
        user = input('Qual seu user?\n')
        senha = pwinput(prompt = 'Qual senha?\n', mask = '*')
        loga(user, senha)
    else:
        user = input('user que gostaria de registrar:\n')
        senha = pwinput(prompt = 'senha para o user:\n', mask = '*')
        registra(user, senha)

def loga(user, senha):
    logou = False
    data = open('C:/Users/Gustavo/Desktop/Estudo/crudEstudo/CrudStudies/logInfo.txt', 'r')
    for log in data:
        nome, password = log.split(' - ')
        password = password.strip()
        if nome == user and password == senha:
            logou = True
    if logou:
        menuShow()
    else:
        print('banido')

def registra(user, senha):
    data = open('C:/Users/Gustavo/Desktop/Estudo/crudEstudo/CrudStudies/logInfo.txt', 'a')
    data.write(f'\n{user} - {senha}')

def menuShow():
    global escolha
    escolha = input('''
========== CRUD Menu ==========

[1] Registrar novo login
[2] Consulta de Logs
[3] c
[4] d
[0] x\n ''')


def addLog():
     if escolha == '1':
        newname = input('User a ser registrado:\n')
        newsenha = input('Senha a ser registrado:\n')
        registra(newname, newsenha)

def showlog():
    if escolha == '2':
        data = open('C:/Users/Gustavo/Desktop/Estudo/crudEstudo/CrudStudies/logInfo.txt', 'r')
        for log in data:
            print(log)