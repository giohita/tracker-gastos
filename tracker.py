# Esta función añade un gasto a la lista de gastos.
def add_expense(expenses, amount, category):
  expenses.append({'amount': amount, 'category': category})

# Esta función imprime todos los gastos en la lista de gastos.
def print_expenses(expenses):
  for expense in expenses:
      print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

# Esta función calcula el total de todos los gastos en la lista.
def total_expenses(expenses):
  return sum(map(lambda expense: expense['amount'], expenses))

# Esta función filtra los gastos por categoría y devuelve un iterable con los gastos filtrados.
def filter_expenses_by_category(expenses, category):
  return filter(lambda expense: expense['category'] == category, expenses)

# Esta es la función principal del programa.
def main():
  expenses = []  # Lista para almacenar los gastos
  while True:
      print('\nExpense Tracker')  # Menú de opciones
      print('1. Add an expense')
      print('2. List all expenses')
      print('3. Show total expenses')
      print('4. Filter expenses by category')
      print('5. Exit')

      choice = input('Enter your choice: ')  # Solicita al usuario su elección

      if choice == '1':  # Opción para agregar un gasto
          amount = float(input('Enter amount: '))  # Solicita al usuario ingresar el monto del gasto
          category = input('Enter category: ')  # Solicita al usuario ingresar la categoría del gasto
          add_expense(expenses, amount, category)  # Llama a la función para agregar el gasto a la lista

      elif choice == '2':  # Opción para listar todos los gastos
          print('\nAll Expenses:')
          print_expenses(expenses)  # Llama a la función para imprimir todos los gastos

      elif choice == '3':  # Opción para mostrar el total de gastos
          print('\nTotal Expenses: ', total_expenses(expenses))  # Llama a la función para calcular y mostrar el total de gastos

      elif choice == '4':  # Opción para filtrar los gastos por categoría
          category = input('Enter category to filter: ')  # Solicita al usuario ingresar la categoría para filtrar
          print(f'\nExpenses for {category}:')
          expenses_from_category = filter_expenses_by_category(expenses, category)  # Filtra los gastos por categoría
          print_expenses(expenses_from_category)  # Imprime los gastos filtrados

      elif choice == '5':  # Opción para salir del programa
          print('Exiting the program.')
          break  # Sale del bucle while y termina la ejecución del programa

if __name__ == '__main__':
  main()  # Llama a la función principal si el script se ejecuta directamente
