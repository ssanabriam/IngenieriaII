'''Registro de actividad'''
import csv
from datetime import datetime

class RegistroAsistencia:
    def __init__(self, archivo='asistencia.csv'):
        self.archivo = archivo
        self._inicializar_archivo()

    def _inicializar_archivo(self):
        """Crea el archivo CSV si no existe."""
        try:
            with open(self.archivo, 'x', newline='') as f:
                escritor = csv.writer(f)
                escritor.writerow(['ID Empleado', 'Fecha', 'Hora Entrada', 'Hora Salida'])
        except FileExistsError:
            pass

    def registrar_entrada(self, id_empleado):
        """Registra la hora de entrada de un empleado."""
        fecha_hora_actual = datetime.now()
        fecha = fecha_hora_actual.strftime('%Y-%m-%d')
        hora_entrada = fecha_hora_actual.strftime('%H:%M:%S')
        
        with open(self.archivo, 'a', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerow([id_empleado, fecha, hora_entrada, ''])
        print(f"Entrada registrada para el empleado {id_empleado} a las {hora_entrada} el {fecha}.")

    def registrar_salida(self, id_empleado):
        """Registra la hora de salida de un empleado."""
        fecha_hora_actual = datetime.now()
        fecha = fecha_hora_actual.strftime('%Y-%m-%d')
        hora_salida = fecha_hora_actual.strftime('%H:%M:%S')
        filas = []
        
        with open(self.archivo, 'r', newline='') as f:
            lector = csv.reader(f)
            for fila in lector:
                if fila[0] == id_empleado and fila[1] == fecha and fila[3] == '':
                    fila[3] = hora_salida
                filas.append(fila)
        
        with open(self.archivo, 'w', newline='') as f:
            escritor = csv.writer(f)
            escritor.writerows(filas)
        print(f"Salida registrada para el empleado {id_empleado} a las {hora_salida} el {fecha}.")
