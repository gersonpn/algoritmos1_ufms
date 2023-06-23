horas = int (input ("Digite as horas : "))

if horas >= 0 and horas <= 11:
    print ("Bom dia")
elif horas >= 12 and horas <= 17:
    print ("Boa tarde")
else:
     print ("Boa noite")