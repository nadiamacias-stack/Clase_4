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
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)
    
    def verNumeroPacientes(self):
        print (f"en el sistema hay: {str(len(self.__lista_pacientes))}")
    
    def verDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c ==p.verCedula():
                return p



def main():
    sis = Sistema()

    while True:
        opcion= int(input ("""
                    1. Nuevo paciente
                    2. Número de pacientes
                    3. Datos paciente 
                    4. salir
                    """))
        if opcion == 1:
            print ("solicitando datos.....")
            nombre = input("ingresar nombre: ")
            cedula = int(input("ingresar cedula: "))
            genero = input("ingrese genero: ")
            servicio = input("ingrese servicio: ")

            pac = Paciente()
            pac.asignarNombre(nombre)
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarServicio(servicio)

            sis.ingresarPaciente(pac)
        elif opcion == 2:
            sis.verNumeroPacientes()
        elif opcion == 3:
            c=int(input("ingrese la cedula a buscar: "))
            p= sis.verDatosPaciente(c)
            print (f" Nombre: {p.verNombre()} \n Cédula: {str(p.verCedula())} \n Genero: {p.verGenero()} \n Servicio: {p.verServicio()}") 
        elif opcion == 4:
            break
        elif opcion !=0:
            continue
        else:
            print("opcion invalida")
            break

if __name__ == "__main__":
    main()