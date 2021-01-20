
import art
def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mult(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2


operations = {
  "+": add,
  "-": sub,
  "*": mult,
  "/": div
}

print(art.logo)

num1 = float(input("What is the first number: "))
num2 = float(input("What is the second number: "))

for symbol in operations:
  print(symbol)
operation_symbol = input("What is the operation: ")

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(answer)