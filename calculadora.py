num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: ")) 

valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir
            5- elevar numero
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("la suma es",num1+num2)
        break;
    if valor == 2:
        print("la resta es",num1-num2)
        break;
    if valor == 3:
        print("la multiplicacion es",num1*num2)
        break;
    if valor == 4:
        print("la division es",num1/num2)
        break;
    if valor==5:
        print("la elevacion es",num1**num2)
    else:
        print("Opcion incorrecta")
        break;