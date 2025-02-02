from datetime import datetime, timedelta

class Prestamo:

    def __init__(self, id_prestamo, id_libro, id_lector, dias_prestamo, fecha_prestamo, fecha_entrega):
        self.id_prestamo = id_prestamo
        self.id_libro = id_libro
        self.id_lector = id_lector
        self.dias_prestamo = dias_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega

    # Representación de la clase Prestamo en forma de cadena

    def __str__(self):
        return f"ID prestamo: {self.id_prestamo}, ID libro: {self.id_libro}, ID lector: {self.id_lector}, Dias prestamo: {self.dias_prestamo}, Fecha del prestamo: {self.fecha_prestamo}, Fecha de entrega: {self.fecha_entrega}"
    
    #--------------------------------------------------------------- getter --------------------------------------------------------------
 
    def getIdPrestamo(self):
        return self.id_prestamo
    
    def getIdLibro(self):
        return self.id_libro
    
    def getIdLector(self):
        return self.id_lector
    
    def getDiasPrestamo(self):
        return self.dias_prestamo
    
    def getFechaPrestamo(self):
        return self.fecha_prestamo
    
    def getFechaEntrega(self):
        return self.fecha_entrega
    
    #-------------------------------------------------------------- setter --------------------------------------------------------------

    def setIdPrestamo(self, id_prestamo):
        self.id_prestamo = id_prestamo
    
    def setIdLibro(self, id_libro):
        self.id_libro = id_libro
    
    def setIdLector(self, id_lector):
        self.id_lector = id_lector
    
    def setDiasPrestamo(self, dias_prestamo):
        self.dias_prestamo = dias_prestamo
    
    def setFechaPrestamo(self, fecha_prestamo):
        self.fecha_prestamo = fecha_prestamo
    
    def setFechaEntrega(self, fecha_entrega):
        self.fecha_entrega = fecha_entrega

    #-------------------------------------------------------------- operaciones --------------------------------------------------------------

    def calcularFechaEntrega(self):
        self.fecha_entrega = self.fecha_prestamo + timedelta(days=self.dias_prestamo)