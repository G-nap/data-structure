class CreateEmail :
    def  __init__(self) :
        self.firstname = ""
        self.lastname = ""

    def eMail(self) :
        if self.firstname == "" and self.lastname == "":
            return 'Please Enter Your Firstname & Lastname'
        elif self.firstname == "":
            return 'Please Enter Your Firstname'
        elif self.lastname == "":
            return 'Please Enter Your Lastname'
        return f'{self.firstname.lower()}.{self.lastname.lower()}@kmitl.ac.th'


    def fullName(self) :
        if self.firstname == "" and self.lastname == "":
            return 'Please Enter Your Firstname & Lastname'
        elif self.firstname == "":
            return 'Please Enter Your Firstname'
        elif self.lastname == "":
            return 'Please Enter Your Lastname'
        return f'{self.firstname.capitalize()} {self.lastname.capitalize()}'
    
    @property
    def firstName(self):
        if self.firstname == "":
            return 'Please Enter Your Firstname'
        return self.firstname.capitalize()

    @firstName.setter
    def firstName(self, firstname):
        if firstname != "":
            self.firstname = firstname.capitalize()
        else:
            self.firstname = ""

    @property
    def lastName(self):
        if self.lastname == "":
            return 'Please Enter Your Lastname'
        return self.lastname.capitalize()

    @lastName.setter
    def lastName(self, lastname):
        if lastname != "":
            self.lastname = lastname.capitalize()
        else:
            self.lastname = ""
 
print("*** Create Email < BY KMITL > ***")
_input = [e for e in input("Enter Input : ").split(",")]
e1 = CreateEmail()
     
for data in _input :
    dataSplit = data.split()
    dataType = dataSplit[0]
    length = len(dataSplit)
    if dataType == "E" :
        print(f"\'{dataType}\' -> Email : {e1.eMail()}")
    elif length == 3 and dataType == 'A':
        e1.firstname = dataSplit[1]
        e1.lastname = dataSplit[2]
    elif length == 2 and dataType == 'F':
        e1.firstname = dataSplit[1]
    elif length == 2 and dataType == 'L':
        e1.lastname = dataSplit[1]
    elif length == 1 and dataType == 'SA':
        print(f'\'{dataType}\' -> Fullname : {e1.fullName()}')
    elif length == 1 and dataType == 'SF':
        print(f'\'{dataType}\' -> Firstname : {e1.firstName}')
    elif length == 1 and dataType == 'SL':
        print(f'\'{dataType}\' -> Lastname : {e1.lastName}')
    elif length == 1 and dataType == 'X':
        break
    else:
        print(f'\'{data}\' is Invalid Input !!!')
        break