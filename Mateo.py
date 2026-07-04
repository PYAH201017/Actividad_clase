import time

# Un pequeño efecto dramático para empezar... o algo asi :v
print("Iniciando Escáner de Humor Docente v1.0...")
time.sleep(1)
print("------------------------------------------")

# La primer pregunta
print("Pregunta 1: Teacher, ¿no le gustaría pasarme de materia de una vez? :3")
respuesta1 = input("Respuesta (Si/No): ")

print("\nProcesando respuesta...")
time.sleep(1.5)

if respuesta1.lower() == "si" or respuesta1.lower() == "sí":
    print("¡EXCELENTE EXCELENTISIMO! ¡Muchas gracias Teacher :D! 🌟")
    print("Anisando la nota de una vez... ¡Procesado con éxito! 10/10")
else:
    # Si dice "No" (o cualquier otra cosa) pasara aquí
    print("¡¿EH?!, ¡¿COMO QUE NO?! :C")
    print("Teacher, no diga eso... 💔")
    
    print("\n------------------------------------------")
    time.sleep(1)
    
    # Pregunta 2 (La oportunidad de redención jsjsj)
    print("Pregunta 2: Está bien... pero si se rie con este codigo, ¿me da puntos extra? <3")
    respuesta2 = input("Respuesta (Si/No): ")
    
    print("\nCalculando probabilidad de éxito...")
    time.sleep(1.5)
    
    if respuesta2.lower() == "si" or respuesta2.lower() == "sí":
        print("¡BELLISSIMO! Sabía que al final aceptaria. ¡Prometo dar el 100%! 🚀")
    else:
        print("Ughhhh... 💀 Tocarà activar el plan de contingencia: Estudiar el triple🤕.")

print("\n------------------------------------------")
print("Fin del programa. ¡Gracias por su tiempo, Teacher! :D")