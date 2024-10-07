import firebase_admin
from firebase_admin import credentials, db, firestore

cred = firebase_admin.credentials.Certificate("chave_firebase.json")#
firebase_admin.initialize_app(cred,{
             'databaseURL': "https://mensagem-encryptografada-default-rtdb.firebaseio.com/"
})

ref = db.reference("/")
# Números primos para calcular as chaves:
p = 61
q = 53

# Calculo de Euler:
Euler_n = (p -1)*(q -1) # 3120


# Recebe "n" de acordo com multiplicação dos números primos:
n = p * q # 3233

# Usado na chave pública:
e = 17  # Número coprimo de 3120

# Inverso modular de 17 e 3120
d = 2753


# Listas usadas no script:
lista_mensagem = [] # Lista na qual ficaram salvas as mensagens
lista_convertida = [] # Nesta lista ficam as letras convertidas em números
lista_Criptografada = [] # Nesta lista ficam os número criptografados
lista_descriptografada = []# Esta lista armazena os dados da mensagem em decimal
lista_convertida_des = []# Esta lista armazena os dados convertido em texto
lista_mensagem_recebida_cript = []# dados criptografados retornado do banco de dados


# Funções do projeto:
def converte_dados(): # Transforma a letra para decimal:
  for sublista in lista_mensagem:
    for i in sublista:
        decimal = ord(i)
        lista_convertida.append(decimal)

def criptografa(): # Criptografa a mensagem através do seguinte cálculo:
  for m in lista_convertida:
    c = m**e % n
    lista_Criptografada.append(c)

def descriptografia(): # Descriptografa a mensagem através do seguinte cálculo:
  for crpt in lista_mensagem_recebida_cript[0]:
    des = crpt**d % n
    lista_descriptografada.append(des)

def converte_texto(): # Transformará os números antes convertidos em decimais para seus valores reais:  l
  for txt in lista_descriptografada:
    texto = chr(txt)
    lista_convertida_des.append(texto)
  texto_descriptografado = ''.join(lista_convertida_des)
  return texto_descriptografado


 #Salva os dados escritos no banco de dados

def SalvaNoDb(): # Salva os dados escritos no banco de dados
     nome_mensagem = input(" Digite para quem quer enviar: ")
     ref.update({
         #         key : value
         nome_mensagem : lista_Criptografada
     })


def recupera_dados():# recupera_dados torna a mensagem escrita de acordo com a maneira na qual foi salva : db():
    nome_mensagem = input(" Digite seu nome para ver mensagens recebidas: ")
    ref_recupera = db.reference(f"{nome_mensagem}")
    mensagem_recuperada = ref_recupera.get()
    lista_mensagem_recebida_cript.append(mensagem_recuperada)
    descriptografia()
    texto_tela = converte_texto()
    print(f" Mensagem descriptografada: {texto_tela}")
    input(" Digite OK para continuar: ")


 # Deleta do Banco de Dados a informação solicitada pelo usuário. 

def deletedb(): # deleta os dados no banco de dados
  ''' Deleta os dados de dentro do banco de dados de acordo com a mensagem \n
      Ana Melo<3 '''
  mensagem_deletar = input(" Digite a mensagem que deseja apagar: ")
  ref = db.reference(f"/{mensagem_deletar}")
  ref.delete()
  print(" Dados removidos com sucesso.")
  input(" Digite OK para continuar: ")


def envia_mesagem(): # Pergunta ao usuário quantas mensagem ele deseja digitar.
    lista_mensagem.clear()
    numero_mensagens = int(input(" Quantas mensagens deseja criptografar? "))
    print(lista_mensagem)
    contador = 0
    while contador != numero_mensagens:
      mensagem = input(" Digite uma mensagem para criptrografar: ")
      lista_mensagem.append(list(f'{mensagem}'))
      lista_mensagem.append("  ")
      contador += 1
      print(f" Mensagem {contador} salvada!")
      print(" A mensagem: ", mensagem ,"foi salva")

    if numero_mensagens == contador:
      converte_dados()
      criptografa()
      print(f" Lista criptografada: {lista_Criptografada}")
      SalvaNoDb()

def mostra_chaves(): # Aqui é mostrado as chaves públicas e privadas
  chave_publica = ( n, e)
  chave_privada = ( n, d)
  print(f" Sua chave Pública é: {chave_publica} \n Sua chave Privada é: {chave_privada}")
  input(" Digite OK para continuar: ")

  
def painel(): # Painel na qual fará as perguntas do que o usuário deseja fazer:
  comando = input(
    "\n Bem-vindo a aplicação!!<3 \n Oque deseja fazer? \n  1 - Criptografar a mensagem \n  2 - Descriptografar uma mensagem\n  3 - Ver chave pública da criptografia\n  4 - Apagar mensagens \n  5 - Sair da aplicação. \n Digite um dos valores 1, 2, 3, 4 ou 5 : \n "
    )

  return int(comando)

while True: # Aqui está as Defs(funções) usadas no painel.55
 comando = painel()
 if comando == 1:
   envia_mesagem()
 elif comando == 2:
  recupera_dados()
 elif comando == 3:
    mostra_chaves()
 elif comando == 4:
  deletedb() 
 else:
    ref = db.reference("/") # Define o local onde será operado no banco de dados(raiz)
    print(" Aplicação encerrada")
    break 