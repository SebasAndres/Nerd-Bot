from models.uni_models import Materia, PlanDeEstudios, Cuatrimestre

# MATERIAS 
AnalisisI = Materia("Analisis I", 10)
AnalisisII = Materia("Analisis II", 10, requirements=[AnalisisI])
IntroProgramacion = Materia("Introduccion Programacion", 10, requirements=[])
AED = Materia("Algoritmo y Estructura de Datos", 15, requirements=[IntroProgramacion])
Algebra = Materia("Algebra I", 13)
ALC = Materia("Algebra Lineal Computacional", 10, requirements=[Algebra, IntroProgramacion])
Paradigmas = Materia("Paradigmas de Programacion", 10, requirements=[AED])
TDA = Materia("Tecnicas de Diseño de Algoritmos", 10, requirements=[AED])
SD = Materia("Sistemas Digitales", 5, requirements=[IntroProgramacion])
IngSoft = Materia("Ingenieria en Software", 10, requirements=[Paradigmas])
LFAyC = Materia("Lenguajes Formales, Automatas y Computabilidad", 5, requirements=[AED])
AOC = Materia("Arquitectura y Organizacion de Computadores", 10, requirements=[SD])
Complej = Materia("Complejidad Computacional", 5, requirements=[TDA, LFAyC])
SO = Materia("Sistemas Operativos", 10, requirements=[AOC])
Estadistica = Materia("Estadistica Computacional", 10, requirements=[ALC, AnalisisI])
Info =  Materia("Almacenamiento y Recuperacion de la Informacion", 10, requirements=[IngSoft])
Redes = Materia("Redes de Comunicaciones y Computo Distribuido", 10, requirements=[Estadistica, TDA, SO])
Paralela = Materia("Programacion Concurrente y Paralela", 10, requirements=[SO, Paradigmas])
# MATERIAS ESPECIALES
Optativa1 = Materia("Optativa1", 0)
Optativa2 = Materia("Optativa2", 0)
Optativa3 = Materia("Optativa3", 0)
Tesis = Materia("Tesis", 15, requirements=[Redes, Info, Paralela])

# PLANES DE ESTUDIO
REWARD_TITULO_INTERMEDIO = 50
REWARD_TITULO_GRADO = 100

LicenciadoCS = PlanDeEstudios("Licenciado Ciencias de la Computacion",
                              "Grado",
                              {
                                1: [Algebra, IntroProgramacion],
                                2: [AED, AnalisisI],
                                3: [Paradigmas, TDA, SD],
                                4: [IngSoft, LFAyC, AOC],
                                5: [ALC, Complej, SO],
                                6: [Estadistica, Info, Optativa1],
                                7: [Paralela, Redes, Optativa2],
                                8: [Tesis, Optativa3]
                              },
                              REWARD_TITULO_GRADO
                            )
IntermedioCS = PlanDeEstudios("Analista Ciencias de la Computacion",
                              "Intermedio",
                              {
                                1: [Algebra, IntroProgramacion],
                                2: [AED],
                                3: [Paradigmas, TDA, SD],
                                4: [IngSoft, AOC]
                              },
                              REWARD_TITULO_INTERMEDIO
                            )


cuatrimestres_cursados = [ 
    Cuatrimestre ([AnalisisI, Algebra], 2022, 2),
    Cuatrimestre ([IntroProgramacion, AnalisisII], 2022, 2),
]

materias_cursadas = [AnalisisI, Algebra, IntroProgramacion, AnalisisII]
materias_por_cursar = list(set(LicenciadoCS.materias) - set(materias_cursadas))

planes_de_carreras = [
    IntermedioCS,
    LicenciadoCS,
]
