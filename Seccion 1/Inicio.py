def pedir_pizza():
    print("Pedir pizza")

def checar_entrada(edad):
    if edad<18:
        print("No puedes entrar panardo".upper())
    elif edad >= 21:
        print("Puedes Entrar al bar y tambien puede beber")
    else:
        print("Puedes entrar al bar pero no puedes beber")
edad = 17
edad_2 = 17

checar_entrada(edad)

checar_entrada(edad_2)