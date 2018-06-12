print("Enter any type of value")
a = input()
a = a.strip()
x = len(a.split(" "))
if x == 1:
    if a.isalpha():
        print("Is letter")
    elif a.isspace():
        print("Is space")
    else:
        #print("Is alpha numeric")
         a = eval(a)
         if type(a) == int:
             print("Is a  int number")
         elif type(a) == float:
             print("Is float number")
         elif type(a) == complex:
             print("Is complex number")




