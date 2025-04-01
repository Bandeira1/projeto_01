operador = input('Digite o operador(+, -, *, /)')
num1 = float (input('Digite o numero 1 :'))
num2 = float(input('Digite o numero 2 :'))

if operador == '+':
  resultado = num1 + num2
  print('O resultado é: ', resultado)
elif operador == '-':
  resultado = num1 - num2
  print('O resultado é: ',resultado)
elif operador == '*':
  resultado = num1 * num2
  print('O resultado é: ',resultado)
elif operador == '/':
   if num2 !=0:
      resultado = num1 / num2
      print('O resultado é: ',resultado)
   else:
      resultado = 'Erro de divisao por zero!'
else:
      resultado = 'Operador invalido!'
print('Resultado: ', resultado)

