from cgitb import text


print(print)
print(print())

"""
the function name is a reference to the function object, so we can rewrite this reference
"""

f = print

f("123")
print = "this was print func"
f(print)

print = f

"""
def <function_name>(<arguments>):
    <operator_1>
    <operator_2>
    ...
    <operator_n>
"""

# send_mail() - error


def send_mail():
    print("sending email") # function body


send_mail()

send_email = send_mail
send_email()


def send_email_2(name):
    text =f"sending email to {name}"
    print(text)


# send_email_2() - error
send_email_2("Riwi")


def send_email_3(name, years):
    text =f"sending email to {name} which {years} years old"
    print(text)


# send_email_2() - error
send_email_3("Riwi", 18)
