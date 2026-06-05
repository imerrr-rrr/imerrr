import tkinter as tk
class Encuesta:
    def __init__(self):
        self.bueno = 0
        self.medio = 0
        self.poco = 0
        self.nada = 0

    def registrar(self, opcion):

        if opcion == 1:
            self.bueno += 1

        elif opcion == 2:
            self.medio += 1

        elif opcion == 3:
            self.poco += 1

        elif opcion == 4:
            self.nada += 1

    def resultado(self):

        mayor = max(
            self.bueno,
            self.medio,
            self.poco,
            self.nada
        )

        if mayor == self.bueno:
            return "Llevas una vida saludable."

        elif mayor == self.medio:
            return "Tus hábitos son aceptables, pero pueden mejorar."

        elif mayor == self.poco:
            return "Debes mejorar varios de tus hábitos."

        else:
            return "Tus hábitos actuales no son saludables."


class Persona:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def clasificacion(self):
        imc = self.calcular_imc()

        if imc < 18.5:
            return "Bajo peso"
        elif imc < 25:
            return "Peso normal"
        elif imc < 30:
            return "Sobrepeso"
        else:
            return "Obesidad"

    def consejo(self):
        estado = self.clasificacion()

        if estado == "Bajo peso":
            return (
                "Tu peso está por debajo del rango recomendado.\n"
                "Procura llevar una alimentación equilibrada\n"
                "y consultar a un profesional si es necesario."
            )

        elif estado == "Peso normal":
            return (
                "¡Felicidades!\n"
                "Tu peso se encuentra dentro de un rango saludable.\n"
                "Mantén tus buenos hábitos."
            )

        elif estado == "Sobrepeso":
            return (
                "Tu peso está por encima del rango recomendado.\n"
                "Se recomienda realizar actividad física\n"
                "y mejorar los hábitos alimenticios."
            )

        else:
            return (
                "Tu IMC indica obesidad.\n"
                "Es recomendable consultar a un profesional\n"
                "para recibir orientación personalizada."
            )


class Estadisticas:
    def __init__(self):
        self.registros = []

    def agregar(self, estado):
        self.registros.append(estado)

    def porcentaje_sobrepeso(self):
        if len(self.registros) == 0:
            return 0

        cantidad = self.registros.count("Sobrepeso")

        return round((cantidad / len(self.registros)) * 100, 1)


estadisticas = Estadisticas()


def escala_imc(imc):

    if imc < 18.5:
        return "|██░░░░░░░░|"

    elif imc < 25:
        return "|█████░░░░░|"

    elif imc < 30:
        return "|███████░░░|"

    else:
        return "|██████████|"


def proceso():
    try:
        peso = float(entrada_peso.get())
        altura = float(entrada_altura.get())

        persona = Persona(peso, altura)

        imc = persona.calcular_imc()
        estado = persona.clasificacion()
        consejo = persona.consejo()

        estadisticas.agregar(estado)

        barra = escala_imc(imc)

        if estado == "Bajo peso":
            color = "orange"
        elif estado == "Peso normal":
            color = "green"
        elif estado == "Sobrepeso":
            color = "goldenrod"
        else:
            color = "red"

        etiqueta_estado.config(
            text=estado,
            fg=color
        )

        etiqueta_resultado.config(
            text=f"Tu IMC es: {round(imc, 2)}"
        )

        etiqueta_consejo.config(
            text=consejo
        )

        etiqueta_escala.config(
            text=barra
        )

        etiqueta_estadisticas.config(
            text=f"Registros: {len(estadisticas.registros)}\n"
                 f"% con sobrepeso: {estadisticas.porcentaje_sobrepeso()}%"
        )

    except ValueError:
        etiqueta_estado.config(
            text="Error",
            fg="red"
        )

        etiqueta_resultado.config(
            text="Ingresa únicamente números."
        )

        etiqueta_consejo.config(
            text=""
        )


def limpiar():
    entrada_peso.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)

    etiqueta_estado.config(text="")
    etiqueta_resultado.config(
        text="Ingresa tus datos para comenzar"
    )
    etiqueta_consejo.config(text="")
    etiqueta_escala.config(text="")
    etiqueta_estadisticas.config(text="")

def abrir_encuesta():

    ventana_encuesta = tk.Toplevel()
    ventana_encuesta.title("Encuesta de hábitos saludables")
    ventana_encuesta.geometry("800x700")

    preguntas = [
    ("¿Cuántas veces haces ejercicio por semana?",
     ["5 o más veces", "3 o 4 veces", "1 o 2 veces", "Nunca"]),

    ("¿Cuántas horas duermes normalmente?",
     ["8 horas o más", "7 horas", "5 o 6 horas", "Menos de 5 horas"]),

    ("¿Consumes frutas diariamente?",
     ["Todos los días", "4 o 5 días por semana", "1 o 2 días por semana", "Casi nunca"]),

    ("¿Consumes verduras diariamente?",
     ["Todos los días", "Varias veces por semana", "Ocasionalmente", "Casi nunca"]),

    ("¿Cuánta agua tomas al día?",
     ["Más de 2 litros", "Entre 1 y 2 litros", "Menos de 1 litro", "Casi no tomo agua"]),

    ("¿Desayunas todos los días?",
     ["Siempre", "Casi siempre", "Algunas veces", "Nunca"]),

    ("¿Consumes refrescos frecuentemente?",
     ["Nunca o casi nunca", "1 o 2 veces por semana", "3 o 4 veces por semana", "Todos los días"]),

    ("¿Comes comida rápida con frecuencia?",
     ["Casi nunca", "Una vez por semana", "Varias veces por semana", "Todos los días"]),

    ("¿Pasas muchas horas sentado?",
     ["Menos de 3 horas", "Entre 3 y 5 horas", "Entre 6 y 8 horas", "Más de 8 horas"]),

    ("¿Consideras equilibrada tu alimentación?",
     ["Muy equilibrada", "Bastante equilibrada", "Poco equilibrada", "Nada equilibrada"])

    ]

    respuestas = []

    tk.Label(
        ventana_encuesta,
        text="Encuesta de Hábitos Saludables",
        font=("Arial", 18, "bold")
    ).pack(pady=10)

    tk.Label(
        ventana_encuesta,
        text="1 = Saludable | 2 = Medio saludable | 3 = Poco saludable | 4 = Nada saludable",
        font=("Arial", 10)
    ).pack(pady=5)

    for pregunta in preguntas:

        variable = tk.IntVar(value=1)
        respuestas.append(variable)

        frame = tk.Frame(ventana_encuesta)
        frame.pack(anchor="w", padx=20, pady=5)

        tk.Label(
            frame,
            text=pregunta,
            font=("Arial", 10, "bold")
        ).pack(anchor="w")

        tk.Radiobutton(
            frame,
            text="1",
            variable=variable,
            value=1
        ).pack(side="left")

        tk.Radiobutton(
            frame,
            text="2",
            variable=variable,
            value=2
        ).pack(side="left")

        tk.Radiobutton(
            frame,
            text="3",
            variable=variable,
            value=3
        ).pack(side="left")

        tk.Radiobutton(
            frame,
            text="4",
            variable=variable,
            value=4
        ).pack(side="left")

    def evaluar():

        encuesta = Encuesta()

        for respuesta in respuestas:
            encuesta.registrar(respuesta.get())

        total = (
            encuesta.bueno +
            encuesta.medio +
            encuesta.poco +
            encuesta.nada
        )

        porcentaje_bueno = round((encuesta.bueno / total) * 100, 1)
        porcentaje_medio = round((encuesta.medio / total) * 100, 1)
        porcentaje_poco = round((encuesta.poco / total) * 100, 1)
        porcentaje_nada = round((encuesta.nada / total) * 100, 1)

        resultado = encuesta.resultado()

        ventana_resultado = tk.Toplevel()

        ventana_resultado.title("Resultado de la encuesta")
        ventana_resultado.geometry("500x350")

        tk.Label(
            ventana_resultado,
            text="RESULTADOS",
            font=("Arial", 18, "bold")
        ).pack(pady=10)

        tk.Label(
            ventana_resultado,
            text=f"Saludable: {porcentaje_bueno}%\n"
                 f"Medio saludable: {porcentaje_medio}%\n"
                 f"Poco saludable: {porcentaje_poco}%\n"
                 f"Nada saludable: {porcentaje_nada}%",
            font=("Arial", 12)
        ).pack(pady=15)

        tk.Label(
            ventana_resultado,
            text=resultado,
            font=("Arial", 14, "bold")
        ).pack(pady=20)

    tk.Button(
        ventana_encuesta,
        text="Evaluar encuesta",
        font=("Arial", 12, "bold"),
        command=evaluar
    ).pack(pady=20)

ventana = tk.Tk()
ventana.title("Descubre tu tipo de cuerpo")
ventana.geometry("750x650")
ventana.config(bg="#EAF4F4")

titulo = tk.Label(
    ventana,
    text="DESCUBRE TU TIPO DE CUERPO",
    font=("Impact", 28),
    bg="#EAF4F4"
)
titulo.pack(pady=15)

subtitulo = tk.Label(
    ventana,
    text="Conoce tu Índice de Masa Corporal (IMC)\n"
         "y descubre si tu peso se encuentra en un rango saludable.",
    font=("Arial", 12),
    bg="#EAF4F4"
)
subtitulo.pack(pady=5)

marco = tk.Frame(
    ventana,
    bg="white",
    bd=2,
    relief="groove"
)

marco.pack(
    padx=40,
    pady=20,
    fill="both"
)

tk.Label(
    marco,
    text="Peso (kg)",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(pady=(20, 5))

entrada_peso = tk.Entry(
    marco,
    width=20,
    justify="center",
    font=("Arial", 12)
)
entrada_peso.pack()

tk.Label(
    marco,
    text="Altura (m)",
    font=("Arial", 12, "bold"),
    bg="white"
).pack(pady=(15, 5))

entrada_altura = tk.Entry(
    marco,
    width=20,
    justify="center",
    font=("Arial", 12)
)
entrada_altura.pack()

frame_botones = tk.Frame(
    marco,
    bg="white"
)

frame_botones.pack(pady=20)

boton_calcular = tk.Button(
    frame_botones,
    text="Analizar mi resultado",
    font=("Arial", 11, "bold"),
    command=proceso
)

boton_calcular.pack(
    side="left",
    padx=10
)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=("Arial", 11, "bold"),command=limpiar
)

boton_encuesta = tk.Button(
    frame_botones,
    text="Encuesta de hábitos",
    font=("Arial", 11, "bold"),
    command=abrir_encuesta
)

boton_encuesta.pack(
    side="left",
    padx=10
)

boton_limpiar.pack(
    side="left",
    padx=10
)

etiqueta_estado = tk.Label(
    marco,
    text="",
    font=("Arial", 18, "bold"),
    bg="white"
)

etiqueta_estado.pack(pady=10)

etiqueta_resultado = tk.Label(
    marco,
    text="Ingresa tus datos para comenzar",
    font=("Arial", 12,"bold"),
    bg="white"
)

etiqueta_resultado.pack(pady=5)

etiqueta_consejo = tk.Label(
    marco,
    text="",
    font=("Arial", 11),
    bg="white",
    wraplength=550,
    justify="center"
)

etiqueta_consejo.pack(pady=(10, 20))

etiqueta_escala = tk.Label(
    marco,
    text="",
    font=("Courier New", 14, "bold"),
    bg="white"
)

etiqueta_escala.pack(pady=5)

etiqueta_estadisticas = tk.Label(
    marco,
    text="",
    font=("Arial", 10),
    bg="white"
)

etiqueta_estadisticas.pack(pady=10)

ventana.mainloop()
