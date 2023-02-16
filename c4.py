class Paciente(): 
    def __init__(self):  
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""

    def verNombre(self):
        return self.__nombre
    def verCedula(self):
        return self.__cedula
    def verGenero(self):
        return self.__genero
    def verServicio(self):
        return self.__servicio 

    def asignarNombre(self,n):
        self.__nombre = n
    def asignarCedula(self,c):
        self.__cedula = c
    def asignarGenero(self,g):
        self.__genero = g
    def asignarServicio(self,s):
        self.__servicio = s 

class Sistema():
    def __init__(self):
        # self.__lista_pacientes = {} #Manejar los pacientes en lista, objeto tipo diccionario
        self.__lista_pacientes = [] #Manejar los pacientes en lista, objeto tipo lista.
        #La siguiente variable siempre dependera del tamaño de la lista, por lo cual no se podra modificar
        # con un método de asignar
        self.__numero_pacientes = len(self.__lista_pacientes)

    def ingresarPaciente(self, p):
        # Guardar paciente en la lista
        # self.__lista_pacientes[p.verCedula()]= p
        self.__lista_pacientes.append(p)

        # Actualización la cantidad de pacientes en el sistema
        self.__numero_pacientes = len(self.__lista_pacientes)

    def verNumeroPacientes(self):
        return self.__numero_pacientes

    def verDatosPacientes(self):
        cedula = int(input("Ingrese la Cédula a buscar: "))
        # Es for paciente y no cedula porque en la lista hay pacientes no numeros 
        for paciente in self.__lista_pacientes: 
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())


def main():
    mi_sistema = Sistema()


    while True:
        menu = int(input("""1.Nuevo Paciente
        2. Número de Pacientes
        3. Datos Paciente
        4. Salir
        > """))
        if menu == 1:
            # Solicitar datos
            nombre = input("Ingrese el Nombre: ")
            cedula =int(input("Ingrese la Cédula: "))
            genero =input("Ingrese el Género: ")
            servicio = input("Ingrese el Servicio: ")

            
            # Crear objeto Paciente y le asigno los datos
            p = Paciente()
            p.asignarNombre(nombre)
            p.asignarCedula(cedula)
            p.asignarGenero(genero)
            p.asignarServicio(servicio)
            mi_sistema.ingresarPaciente(p)

        elif menu == 2:
            print("Número total de pacientes: " + str(mi_sistema.verNumeroPacientes()))
        elif menu == 3:
            mi_sistema.verDatosPacientes()
        elif menu == 4:
            break
        else: 
            print("Opción inválida")