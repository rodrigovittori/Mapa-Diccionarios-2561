import time

# M4.L3 - Actividad #5: "Llave"

mapa = {
        # 1ª CLAVE (del mapa) :    VALOR (otro diccionario)
        #                       2º diccionario (cada habitacion tiene su propio diccionario)
        #                       lista_habitaciones, lista_items, (pueden agregar: lista_trampas y/o lista_enemigos)
        
        'Spawn'               : { 'lista_habitaciones' :  ['1', '2'], 'items' : [] },
        '1'                   : { 'lista_habitaciones' :  ['Spawn', '3', '4'], 'items' : [] },
        '2'                   : { 'lista_habitaciones' :  ['Spawn', '4'], 'items' : [] },
        '3'                   : { 'lista_habitaciones' :  ['1'], 'items' : ['Planta misteriosa'] },
        '4'                   : { 'lista_habitaciones' :  ['1', '2', 'Boss'], 'items' : [] },
        'Boss'                : { 'lista_habitaciones' :  ['4', 'Salida'], 'items' : [] },
        'Salida'              : { 'lista_habitaciones' :  ['Boss'], 'items' : [] }
        }
#  Habitación actual : Lista de habitaciones accesibles

# Seteamos habitación inicial (Spawn)
habitacion_actual = "Spawn"
tiene_arma_legendaria = False

# Bucle de Juego:
while(True): # To-do: agregar una condición para detener el bucle de juego
  print('============================')
  print('Estás en la habitación', habitacion_actual)

  # Mostrar habitaciones disponibles/accesibles:
  for habitacion_contigua in mapa[habitacion_actual]['lista_habitaciones']:
    print("Puedes ir a", habitacion_contigua)

  nueva_habitacion = input("¿Qué habitación eliges?: ")

  #Validamos habitación destino:
  if nueva_habitacion not in mapa[habitacion_actual]['lista_habitaciones']:
    print("¡No puedes hacer eso!, ", nueva_habitacion, " NO es accesible desde aquí.")
    time.sleep(2)
    continue

  else:
    
    # Si la habitacion ES válida
    if (nueva_habitacion == "Salida"):
      print("¡Eres libre!")
      time.sleep(2)
      break

    elif (nueva_habitacion == "Boss") and not tiene_arma_legendaria:
      print("La presencia del malo malvado es tan maléficamente malvada que tus piernas se vuelven blandas como malvaviscos y no puedes obligarte a entrar.")
      print("AUN NO ESTAS LISTO, ¡ENCUENTRA EL ARMA LEGENDARIA QUE LO DERROTARÁ!")
      time.sleep(2)

    elif (nueva_habitacion == "Boss") and tiene_arma_legendaria:
      print("El malo malvado comienza un laaaaaaaaargo discurso sobre como unos aventureros como ustedes nunca podrán con un mago tan poderoso como él que ha aterrorizado estas tierras por más de 500 años.")
      print("-\"Y es EXACTAMENTE lo que nuestro amiguito estaba buscando\" :)")
      print("-\"¡VÉ JUAN!, ¡ATRÁPALO!\"")
      print("** Juan es una iguana devoradora de maná **")
      print("La escencia vital del mago malvado es absorbida en un instante por Juan, quien crece descomunalmente, empjándote hacia la Salida...")
      print("No sólo has salvado al reino, sino que has hecho muy feliz a tu nuevo (y ya no tan pequeño) amigo: JUAN")
      print("\n GOOD ENDING: \" My friend JUAN\" ")
      time.sleep(2)

    habitacion_actual = nueva_habitacion

    # Chequear items
    if "Planta misteriosa" in mapa[habitacion_actual]['items']:
      tiene_arma_legendaria = True
      print("En la habitación encuentras una pequeña planta misteriosa que llama tu atención, al acercarte se enrieda en tu antebrazo y no logras despegarla de tí")
      mapa[habitacion_actual]['items'].remove('Planta misteriosa')
      time.sleep(2)
      continue