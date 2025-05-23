import datetime
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 

    def verificarMedicamento(self, lista, medic):
        for m in lista:
            if medic.verNombre() == m.verNombre():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
    
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso.strftime("%d/%m/%Y")
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
        self.__DictCaninos = {}
        self.__DictFelinos = {}
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
        
    def verNumeroMascotas(self):
        return len(self.__DictCaninos) + len(self.__DictFelinos)
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
        if mascota.verTipo() == "canino":
            self.__DictCaninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo == "felino":
            self.__DictFelinos[mascota.verHistoria()] = mascota

   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__DictCaninos:
            return self.__DictCaninos[historia].verFecha()
        elif historia in self.__DictFelinos:
            return self.__DictFelinos[historia]. verFecha()
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__DictCaninos:
            return self.__DictCaninos[historia].verLista_Medicamentos()
        if historia in self.__DictFelinos:
            return self.__DictFelinos[historia].verLista_Medicamentos()
        return None
    
    def eliminarMascota(self, historia):
        if historia in self.__DictCaninos:
            self.__DictCaninos.pop(historia)
            return True
        if historia in self.__DictFelinos:
            self.__DictFelinos.pop(historia)
            return True
    
    def eliminarMedicamento(self, historia, MedicBorrar):
        if historia in self.__DictCaninos:
            mascota = self.__DictCaninos[historia]
            lista = mascota.verLista_Medicamentos() #Obtengo la lista de medicamentos de la mascota, sus objetos de la clase Medicamento
            for medicamento in lista: #medicamento en un objeto clase Medicamento
                if medicamento.verNombre() == MedicBorrar:
                    lista.pop(lista.index(medicamento))
                    #Al pop hay que pasarle una posición específica
                    #lista.index(medicamento) busca la posición del medicamento en esa lista
                    return True

        return None

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ").strip().lower()
                peso=int(input("Ingrese el peso de la mascota: "))
                print("Va a ingresar los datos de dia, mes y año: ")

                while True:
                    dia = int(input("Ingrese día (en número): "))
                    if 1<=dia <= 31:
                        break
                    else:
                        print("Ha ingresado un número incorrecto, intente de nuevo")
                        continue

                while True:
                    mes = int(input("Ingrese mes (en número): "))
                    if 1 <= mes <= 12:
                        break
                    else: 
                        print("Ha ingresado un número incorrecto, intente de nuevo")
                        continue

                while True:
                    año = int(input("Ingrese año (en número): "))
                    if año <= 2025:
                        break
                    else:
                        print("Ha ingresado un número incorrecto, intente de nuevo")
                        continue

                fecha = datetime.datetime(año, mes, dia)

                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    
                    if medicamento.verificarMedicamento(lista_med, medicamento) == True:
                        print("Ya existe un medicamento con ese nombre, no se puede agregar")
                        continue #salta a la siguiente iteración del bucle sin agregar el medicamento:
                    else:
                        lista_med.append(medicamento)
                    
                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
               
            else:
                print("Ya existe la mascota con el numero de histoira clinica")

            

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6: #Eliminar medicamento
            historia = int(input("Ingrese la historia clínica de la mascota: "))
            mediBorrar = input("Ingrese nombre del medicamento a eliminar: ")
            resultado = servicio_hospitalario.eliminarMedicamento(historia, mediBorrar)
            if resultado ==True:
                print("Medicamento eliminado con éxito")
            else:
                print("No se ha podido eliminar medicamento")
        
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()
   





            

                

