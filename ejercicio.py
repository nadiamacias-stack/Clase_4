class Paciente():
    def __init__(self):
        self.__nombre:str = ""
        self.__cedula:int = 0
        self.__genero:str = ""
        self.__servicio:str = ""

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s
    
    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula 
    def verGenero(self):
        return self.__genero 
    def verServicio(self):
        return self.__servicio
    

class Sistema():
    def __init__(self):
        self.__lista_pacientes = []
        self.__numero_pacientes = len(self.__lista_pacientes)
    
    def ingresarPaciente(self):
        nombre = input("ingresar nombre: ")
        cedula = int(input("ingresar cedula: "))
        genero = input("ingrese genero: ")
        servicio = input("ingrese servicio: ")

        p = Paciente()
        p.asignarNombre(nombre)
        p.asignarCedula(cedula)
        p.asignarGenero(genero)
        p.asignarServicio(servicio)

        self.__lista_pacientes.append(p)
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPaciente(self):
        cedula = int(input("ingresar cedula a buscar: "))
        
        for paciente in self.__lista_pacientes:
            if cedula == paciente.verCedula():
                print (f" Nombre: {paciente.verNombre()} \n Cédula: {str(paciente.verCedula())} \n Genero: {paciente.verGenero()} \n Servicio: {paciente.verServicio()}") 

mi_sistema = Sistema()

while True:
    opcion= int(input ("""
                 1. Nuevo paciente
                 2. Número de pacientes
                 3. Datos paciente 
                 4. salir
                 """))
    if opcion == 1:
        mi_sistema.ingresarPaciente()
    elif opcion == 2:
        print(f"ahora hay: {str(mi_sistema.verNumeroPacientes())}")
    elif opcion == 3:
        mi_sistema.verDatosPaciente()
    elif opcion == 4:
        break
    else:
        print("opcion invalida")
