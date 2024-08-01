import time

# M4.L3 - Actividad #4: "Transición"

mapa = {
        #       CLAVE       :               VALOR
        # Habitación actual : Lista de habitaciones accesibles
        'Spawn'             : ['1', '2'],
        '1'                 : ['Spawn', '3', '4'],
        '2'                 : ['Spawn', '4'],
        '3'                 : ['1'] , #item
        '4'                 : ['1', '2', 'Boss'],
        'Boss'              : ['4', 'Salida'],
        'Salida'            : ['Boss']
        }

# Seteamos habitación inicial (Spawn)
habitacion_actual = "Spawn"

# Bucle de Juego:
while(True): # To-do: agregar una condición para detener el bucle de juego
  print('============================')
  print('Estás en la habitación', habitacion_actual)

  # Mostrar habitaciones disponibles/accesibles:
  for habitacion_contigua in mapa[habitacion_actual]:
    print("Puedes ir a", habitacion_contigua)

  nueva_habitacion = input("¿Qué habitación eliges?: ")

  #Validamos habitación destino:
  if nueva_habitacion not in mapa[habitacion_actual]:
    print("¡No puedes hacer eso!, ", nueva_habitacion, " NO es accesible desde aquí.")
    time.sleep(2)
    continue

  else:
    
    # Si la habitacion ES válida
    if (nueva_habitacion == "Salida"):
      print("¡Eres libre!")
      time.sleep(2)
      break

    elif (nueva_habitacion == "Boss"):
      print("¡Prepárate para la batalla final!")
      time.sleep(2)

    habitacion_actual = nueva_habitacion