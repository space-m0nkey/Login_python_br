from keyauth import api
import sys
import time
import platform
import os
import hashlib
from time import sleep
from datetime import datetime

def limpar_tela():
    if platform.system() == 'Windows':
        os.system('cls & title Exemplo Python')  
    elif platform.system() == 'Linux':
        os.system('clear') 
        sys.stdout.write("\x1b]0;Exemplo Python\x07") 
    elif platform.system() == 'Darwin':
        os.system("clear && printf '\e[3J'") 
        os.system('''echo - n - e "\033]0;Exemplo Python\007"''')

print("Inicializando...")
sleep(3)

def calcular_checksum():
    md5_hash = hashlib.md5()
    arquivo = open(''.join(sys.argv), "rb")
    md5_hash.update(arquivo.read())
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
    name="reverse",
    ownerid="h4GlGtPhNA",
    secret="fa3158db3ec9df08dbe8ad4dc4d2f68b93b654a55e2013236cbdd455dc05799f",
    version="1.0",
    hash_to_check=calcular_checksum()
)

def resposta():
    try:
        os.system('cls') 
        print("""1. Login
2. Registrar
3. Atualizar
4. Somente Chave de Licença
        """)
        escolha = input("Selecione a Opção: ")
        if escolha == "1":
            usuario = input('Fornecer nome de usuário: ')
            senha = input('Fornecer senha: ')
            keyauthapp.login(usuario, senha)
        elif escolha == "2":
            usuario = input('Fornecer nome de usuário: ')
            senha = input('Fornecer senha: ')
            licenca = input('Fornecer Licença: ')
            keyauthapp.register(usuario, senha, licenca)
        elif escolha == "3":
            usuario = input('Fornecer nome de usuário: ')
            licenca = input('Fornecer Licença: ')
            keyauthapp.upgrade(usuario, licenca)
        elif escolha == "4":
            chave = input('Digite sua licença: ')
            keyauthapp.license(chave)
        else:
            print("\nOpção inválida")
            sleep(1)
            limpar_tela()
            resposta()
    except KeyboardInterrupt:
        os._exit(1)

resposta()

print("\nDados do usuário: ")
print("Nome de usuário: " + keyauthapp.user_data.username)
print("Endereço IP: " + keyauthapp.user_data.ip)
print("Hardware-ID: " + keyauthapp.user_data.hwid)

subs = keyauthapp.user_data.subscriptions  
for i in range(len(subs)):
    sub = subs[i]["subscription"]  
    expiry = datetime.utcfromtimestamp(int(subs[i]["expiry"])).strftime(
        '%Y-%m-%d %H:%M:%S')  
    tempo_restante = subs[i]["timeleft"]  

    print(f"[{i + 1} / {len(subs)}] | Assinatura: {sub} - Expira em: {expiry} - Tempo Restante: {tempo_restante}")

print("Criado em: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.createdate)).strftime('%Y-%m-%d %H:%M:%S'))
print("Último login em: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.lastlogin)).strftime('%Y-%m-%d %H:%M:%S'))
print("Expira em: " + datetime.utcfromtimestamp(int(keyauthapp.user_data.expires)).strftime('%Y-%m-%d %H:%M:%S'))
print("\niniciando...")
sleep(5)
os.system('cls')

os.system('pause')
