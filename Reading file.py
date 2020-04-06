
employee_file = open('Employees.txt', 'r')

# Read a single line
print(employee_file.readline())

# Read multiple lines
print(employee_file.readlines())

employee_file.close()
