

print("Vamos Calcular?")
print("Selcione a operacao desejada:")

op = input("+ para somar | - para subtrair | * para multiplicar | / para dividir")


v1= float(input("Digite o primeiro Valor:"))
v2= float(input("Digite o segundo Valor:"))



if( op=='+'):{

   
    print('O Resultado é: ',v1+v2)

} 
elif( op=='-'):{

    print('o resultado é ',v1-v2)

}
elif(op=="*"):{

    print('o resultado é ',v1*v2)

}
elif(op=="/"):{

    print('o resultado é ',v1/v2)

}
else:{
    print("Valor inválido")
}



