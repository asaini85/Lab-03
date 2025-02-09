def hello():
    print("Hello World")
    print("Inside a Function")

hello()
hello()
hello()
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name
    return greeting

text = return_text_value()
print(text)
def return_number_value():
    num1 = 10
    num2 = 5
    return num1 + num2

number = return_number_value()
print(number)
