class Datos :
  name = ""
  age = 0
  RUT = 0
  address = ""
  telephone = 0
  passport_number = 0
  allergies = ""
  surgical_history = ""
  current_medications = ""
  
##metodos##
  def __init__ (self, name, age, RUT, address, telephone, passport_number, allergies, surgical_history, current_medications):
    self.name = name
    self.age = age
    self.RUT = RUT
    self.address = address
    self.telephone = telephone
    self.passport_number = passport_number
    self.allergies = allergies
    self.surgical_history = surgical_history
    self.current_medications = current_medications
  

def data_menu ():   ##muestra datos a travez de un menu##
  print("1.-name \n 2.-age \n 3.-RUT \n 4.-address \n 5.-telephone \n 6.-passport_number \n 7.-allergies \n 8.-surgical_history 9.-current_medications ")
def data_entry (name, age, RUT, address, telephone, passport_number, allergies, surgical_history, current_medications):   ##entra datos segun el numero escogido##
  
  while(true):
    choice = input("¿Desea ingresar datos? \n (1) Si    (2)No")
    if (choice =="1"):
      option = input("Ingrese el numero de la opcion que desee: ")
      if (option == "1"):
        name = input("nombre: ")
      elif (option == "2"):
        age = input("edad: ")
      elif (option == "3"):
        RUT = input("RUT: ")
      elif (option == "4"):
        address = input("direccion: ")
      elif (option == "5"):
        telephone = input("telefono: ")
      elif (option == "6"):
        passport_number = input("numero de pasaporte: ")
      elif (option == "7"):
        allergies = input("alergias: ")
      elif (option == "8"):
        surgical_history = input("antecedentes quirurjicos: ")
      elif (option == "9"):
        current_medications = input("medicamentos actuales: ")
    elif (choice =="2"):
      break
    
data_menu()
data_entry (name, age, RUT, address, telephone, passport_number, allergies, surgical_history, current_medications)
