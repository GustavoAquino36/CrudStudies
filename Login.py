from pwinput import pwinput

def entrar():
    global cursor
    print('Olá, Bem vindo ao teste de Login')
    cursor = input('Gostaria de Entrar ou se registrar?\n')

def sistema(cursor):
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
    data = open('data base txt path here', 'r')
    for log in data:
        nome, password = log.split(' - ')
        password = password.strip()
        if nome == user and password == senha:
            logou = True
    if logou:
        print('logado')
    else:
        print('banido')

def registra(user, senha):
    data = open('data base txt path here', 'a')
    data.write(f'\n{user} - {senha}')

entrar()
sistema(cursor)