class Alumno:

    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def aprobado(self):
        return self.calificacion >= 6


alumnos = [
    Alumno("Ana", 9),
    Alumno("Luis", 5),
    Alumno("Sofia", 8)
]

for alumno in alumnos:

    print(alumno.nombre, alumno.calificacion)

    if alumno.aprobado():
        print("Aprobado")
    else:
        print("Reprobado")
