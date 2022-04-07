from PyQt5.QtCore import QThread, pyqtSignal, QObject
import time
#----------------------------------------

class CPU(QObject):
    colamayorp=pyqtSignal(bool,int)
    def __init__(self):
        super().__init__()    
        self.cola_srt=Cola_Srt(1)
        self.cola_round=Cola_Round(2)
        self.cola_fifo= Cola_FIFO(3)
        self.command_srt=ShortRafaga(self.cola_srt,self)
        self.command_round=Round_robin(self.cola_round,self)
        self.command_fifo=Command_FIFO(self.cola_fifo,self)
        self.Tiempocomienzo=0
        self.hiloactual=None
        #-------------------------------------------------------
        #-------------------------------------------------------
        self.command_srt.cambiarP.connect(self.ejecutar_MayorP)
        self.command_round.cambiarP.connect(self.ejecutar_MayorP)
        self.command_fifo.cambiarP.connect(self.ejecutar_MayorP)
        self.command_srt.siguiente.connect(self.ejecutar_Siguiente)
        self.command_round.siguiente.connect(self.ejecutar_Siguiente)
        self.command_srt.senal_actualizarespera.connect(self.Actualizar_Espera)
        self.command_round.senal_actualizarespera.connect(self.Actualizar_Espera)
        self.fila=0
        self.ejecutado=False

    def Ejecutar(self):
        self.ejecutado=True
        self.command_srt.start()

    def Mayorprioridad(self,prioridad):
        if prioridad==1:
            return self.command_srt
        elif prioridad ==2:
            return self.command_round
        elif prioridad ==3:
            return self.command_fifo
        else:
            return None

    def ejecutar_MayorP(self,prioridad1,prioridad2):
        if prioridad1==0 and prioridad1!=prioridad2 and prioridad1<prioridad2:
            self.Mayorprioridad(prioridad2).terminate()
            self.Mayorprioridad(prioridad1).start()
    
    def Agregar(self,opcion,proceso):
        if opcion==1:
            self.command_srt.cola.Add_Componente(proceso)
        elif opcion==2:
            self.command_round.cola.Add_Componente(proceso)
        elif opcion==3:
            self.command_fifo.cola.Add_Componente(proceso)
        self.colamayorp.emit(True,opcion)


    def Actualizar_Espera(self,prioridad):
        if prioridad==1:
            self.command_round.LLenarEspera()
            self.command_fifo.LLenarEspera()
        elif prioridad==2:
            self.command_fifo.LLenarEspera()    

    def ejecutar_Siguiente(self,prioridad):
        if prioridad==1:
            self.command_round.start()
        elif prioridad==2:
            self.command_fifo.start()  

    def Get_Fila(self):
        return self.fila

    def Set_Fila(self,valor):
        self.fila=valor

    def Set_Tiempocomienzo(self,valor):
         self.Tiempocomienzo=valor

    def Get_Tiempocomienzo(self):
        return self.Tiempocomienzo
    

#----------------------------------------------
class Proceso:
    def __init__(self,nombre,tiempollegada,rafaga):
        self.Nombre=nombre
        self.tiempollegada=tiempollegada
        self.rafaga=rafaga
        self.prioridad=0
        self.tiempocomienzo=0
        self.tiempofinal=0
        self.tiemporetorno=0
        self.tiempoespera=0
        self.isbloqueado=False
        self.indice=0
        self.rafaga_ejecutada=0

    def Set_isbloqueado(self,booleano):
        self.isbloqueado=booleano

    def Get_isbloqueado(self):
        return self.isbloqueado            

    def Get_nombre(self):
        return self.Nombre

    def Get_tiempollegada(self):
        return self.tiempollegada

    def Get_rafaga(self):
        return self.rafaga        

    def Get_tiempocomienzo(self):
        return self.tiempocomienzo

    def Get_tiempofinal(self):
        return self.tiempofinal

    def Get_tiemporetorno(self):
        return self.tiemporetorno       

    def Get_tiempoespera(self):
        return self.tiempoespera

    def Get_rafaga_ejecutada(self):
        return self.rafaga_ejecutada

    def Set_rafaga(self,valor):
        self.rafaga=valor

    def Set_Prioridad(self,valor):
        self.prioridad=valor

    def Get_Prioridad(self):
        return self.prioridad

    def Set_tiempollegada(self,valor):
        self.tiempollegada=valor
    def Set_tiempocomienzo(self,tiempo):
        self.tiempocomienzo=tiempo

    def Set_rafaga_ejecutada(self,valor):
        self.rafaga_ejecutada=valor

    def Set_tiempofinal(self,tiempo):
        self.tiempofinal=tiempo

    def Set_tiemporetorno(self,tiempo):
        self.tiemporetorno=tiempo

    def Set_tiempoespera(self,tiempo):
        self.tiempoespera=tiempo

    def Get_indice(self):
        return self.indice

    def Set_indice(self,valor):
        self.indice=valor

class Cola:
    def __init__(self,prioridad):
        self.lista=[]
        self.prioridad=prioridad
    
    def Add_Componente(self,proceso):
        self.lista.append(proceso)

    def Size_cola(self):
        return len(self.lista)

    def isvacia(self):
        return len(self.lista)==0
    
    def Get_Prioridad(self):
        return self.prioridad

class Cola_Srt(Cola):
    def __init__(self, prioridad):
        super().__init__(prioridad)

class Cola_Round(Cola):
    def __init__(self, prioridad):
        super().__init__(prioridad)

class Cola_FIFO(Cola):
    def __init__(self, prioridad):
        super().__init__(prioridad)

#-------------------------------------------
#----------------------------------------
class Command(QThread):
    cambiarP=pyqtSignal(int,int)
    senal_actualizar=pyqtSignal(Proceso)
    siguiente=pyqtSignal(int)
    senal_actualizarespera=pyqtSignal(int)
    def __init__(self,cola,cpu):
        super().__init__()
        self.cola=cola
        self.bloquedo=False
        self.cpu=cpu
        self.tiempoenvejecimiento=20
        self.CambioP=False
        self.PrioridadActual=0
        self.cpu.colamayorp.connect(self.CambiarPrioridad)
      
    def Ejecutar(self):
        pass

    def isbloqueado(self):
        return self.bloquedo
    
    def set_bloqueado(self,valor):
        self.bloquedo=valor

    def CambiarPrioridad(self,booleano,prioridad):
        print("cambio la prioridad ",booleano,prioridad)
        self.CambioP=booleano
        self.PrioridadActual=prioridad

    def cambioPrioridad(self):
        return (self.CambioP,self.PrioridadActual)
    
    def Agregar(self,proceso):
        self.cola.Add_Componente(proceso)

    def Completar(self,proceso):
        proceso.Set_tiempofinal(self.cpu.Get_Tiempocomienzo())
        proceso.Set_tiemporetorno(proceso.Get_tiempofinal()-proceso.Get_tiempollegada())
        proceso.Set_rafaga_ejecutada(proceso.Get_rafaga_ejecutada()+(proceso.Get_tiempofinal()-proceso.Get_tiempocomienzo()))
        self.senal_actualizar.emit(proceso)
        time.sleep(1)
    
    def LLenarEspera(self):
        for i in self.cola.lista:
            i.Set_tiempoespera(i.Get_tiempoespera()+1)

class ShortRafaga(Command):
    def __init__(self, cola,cpu):
        super().__init__(cola,cpu)
    
    def Ordenar(self):
        aux=self.cola.lista[0].Get_rafaga()
        pos=-1
        for i in range(1,len(self.cola.lista)):
            if  self.cola.lista[i].Get_rafaga() <aux:
                aux=self.cola.lista[i].Get_rafaga()
                pos=i
        if pos!=-1:
            elemento=self.cola.lista.pop(pos)
            self.cola.lista.insert(0,elemento)
    
    def Ejecutar(self):
        while self.cola.Size_cola()>0:
            self.CambiarPrioridad(False, 0)
            self.Ordenar()
            proceso=self.cola.lista.pop(0)
            proceso.Set_tiempocomienzo(self.cpu.Get_Tiempocomienzo())
            print(proceso.Get_nombre())
            while proceso.Get_rafaga()>0 and not self.isbloqueado():
                print(proceso.Get_rafaga())
                proceso.Set_rafaga(proceso.Get_rafaga()-1)
                self.LLenarEspera()
                self.senal_actualizarespera.emit(self.cola.Get_Prioridad())
                self.cpu.Set_Tiempocomienzo(self.cpu.Get_Tiempocomienzo()+1)                
                time.sleep(1.5)
            if self.isbloqueado():
                pass
            self.Completar(proceso)
            valor=self.cambioPrioridad()
            if valor[0]:
                self.cambiarP.emit(valor[1],self.cola.Get_Prioridad())
        self.siguiente.emit(self.cola.Get_Prioridad())    

    def run(self):
        self.Ejecutar()

class Round_robin(Command):
    def __init__(self, cola,cpu):
        super().__init__(cola,cpu)
        self.quamtum=4
    
    def Ejecutar(self):
        while self.cola.Size_cola()>0:
            self.CambiarPrioridad(False, 0)
            proceso =self.cola.lista.pop(0)
            proceso.Set_tiempocomienzo(self.cpu.Get_Tiempocomienzo())
            quamtum=self.quamtum
            print(proceso.Get_nombre())            
            while proceso.Get_rafaga()>0 and not self.isbloqueado() and quamtum>0:
                print(proceso.Get_rafaga())
                proceso.Set_rafaga(proceso.Get_rafaga()-1)
                self.LLenarEspera()
                self.senal_actualizarespera.emit(self.cola.Get_Prioridad())
                self.cpu.Set_Tiempocomienzo(self.cpu.Get_Tiempocomienzo()+1)                
                time.sleep(1.5)
                quamtum-=1
            self.Completar(proceso)
            if proceso.Get_rafaga()>0:
                proceso.Set_tiempoespera(0)
                self.cola.Add_Componente(proceso)
            elif self.isbloqueado():
                pass
            valor=self.cambioPrioridad()
            if valor[0]:
                self.cambiarP.emit(valor[1],self.cola.Get_Prioridad())
        self.siguiente.emit(self.cola.Get_Prioridad())            
            
    def run(self):
        self.Ejecutar()

class Command_FIFO(Command):
    def __init__(self, cola,cpu):
        super().__init__(cola,cpu)

    def Ejecutar(self):
        while self.cola.Size_cola()>0:
            self.CambiarPrioridad(False, 0)
            proceso =self.cola.lista.pop(0)
            proceso.Set_tiempocomienzo(self.cpu.Get_Tiempocomienzo())           
            print(proceso.Get_nombre())
            while proceso.Get_rafaga()>0 and not self.isbloqueado():
                print(proceso.Get_rafaga())
                proceso.Set_rafaga(proceso.Get_rafaga()-1)
                self.LLenarEspera()
                self.cpu.Set_Tiempocomienzo(self.cpu.Get_Tiempocomienzo()+1)                
                time.sleep(1.5)
            if self.isbloqueado():
                pass
            self.Completar(proceso)
            valor=self.cambioPrioridad()
            if valor[0]:
                self.cambiarP.emit(valor[1],self.cola.Get_Prioridad())
        self.cpu.ejecutado=False        
    
    def run(self):
        self.Ejecutar()

