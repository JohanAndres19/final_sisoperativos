from PyQt5.QtCore import QThread, pyqtSignal
import time
#----------------------------------------
class CPU:
    def __init__(self):    
        self.cola_srt=Cola_Srt(1)
        self.cola_round=Cola_Round(2)
        self.cola_fifo= Cola_FIFO(3)
        self.command_srt=ShortRafaga(self.cola_srt)
        self.command_round=Round_robin(self.cola_round)
        self.command_fifo=Command_FIFO(self.cola_fifo)
        self.hiloactual=None
        
    def Ejecutar(self):
        self.command_srt.start()

#----------------------------------------------
class Proceso:
    def __init__(self):
        print()

class Cola:
    def __init__(self,prioridad):
        self.lista=[]
        self.prioridad=prioridad
    
    def isvacia(self):
        return len(self.lista)==0

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
    def __init__(self,cola):
        super().__init__()
        self.cola=cola
    
    def Ejecutar(self):
        pass

class ShortRafaga(Command):
    def __init__(self, cola):
        super().__init__(cola)
    
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
        while len(self.cola.lista):
            self.Ordenar()
            proceso=self.cola.lista.pop(0)
            while proceso.Get_rafaga()>0 and self.isbloqueado():
                pass
    
    def run(self):
        self.Ejecutar()

class Round_robin(Command):
    def __init__(self, cola):
        super().__init__(cola)
        self.quamtum=4
    
    def Ejecutar(self):
        while len(self.cola.lista)>0:
            proceso =self.cola.lista.pop(0)
            while proceso.Get_rafaga()>0 and self.isbloqueado():
                pass
        else:
            pass

            
    def run(self):
        print("hilo command round")
        time.sleep(1)

class Command_FIFO(Command):
    def __init__(self, cola):
        super().__init__(cola)

    def run(self):
        print("hilo command fifo")
        time.sleep(1)


