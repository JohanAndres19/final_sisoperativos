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
        self.command_round.start()
        self.command_fifo.start() 
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

class ShortRafaga(Command):
    def __init__(self, cola):
        super().__init__(cola)

    def run(self):
        print("hilo command short")
        time.sleep(1)

class Round_robin(Command):
    def __init__(self, cola):
        super().__init__(cola)

    def run(self):
        print("hilo command round")
        time.sleep(1)

class Command_FIFO(Command):
    def __init__(self, cola):
        super().__init__(cola)

    def run(self):
        print("hilo command fifo")
        time.sleep(1)


