# parametro publico;

p = 23
g = 5

# chave privada

a = 893 # excolhido pelo kaue

b = 225 # escolhido pelo Eduardo

# calcular a chave publica 

calculo_a = g**a% p # Kaue
print("Calculo do kauê: ",calculo_a, end="  ")
calculo_b = g**b% p # Eduardo 
print("Calculo do Eduardo: ", calculo_b)

# Na tranferencia Eduardo recebe 8 do kaue. E kaue recebe 19
#calcula a chave secreta compartilhada

# chave do Kaue 
chave_1 = calculo_b**a% p
print("chave do Kaue: ", chave_1, end="  ")

# chave do Eduardo 
chave_2 = calculo_a**b% p
print("chave do Eduardo: ", chave_2, end="  ")
