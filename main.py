import time

# M4.L3 - Actividad #7: "Tu laberinto (Adicional)"

mapa = {
        # 1ª CLAVE (del mapa) :    VALOR (otro diccionario)
        #                       2º diccionario (cada habitacion tiene su propio diccionario)
        #                       lista_habitaciones, lista_items, (pueden agregar: lista_trampas y/o lista_enemigos)
        
        'Dormitorio Invitados': { 'lista_habitaciones' :  ['Sala de Estar'],   'items' : [] , 'lista_trampas' : []},
        'Sala de Estar'       : { 'lista_habitaciones' :  ['Baño', 'Cocina', 'Comedor', 'Dormitorio Invitados', 'Dormitorio Principal', 'Entrada'],
                                                                               'items' : [] , 'lista_trampas' : []},
        'Baño'                : { 'lista_habitaciones' :  ['Sala de Estar'],   'items' : [] , 'lista_trampas' : ['Trampa_Escopeta']},
        'Dormitorio Principal': { 'lista_habitaciones' :  ['Sala de Estar'],   'items' : ['Llaves extra'], 'lista_trampas' : []}, # Posible tunel
        'Comedor'             : { 'lista_habitaciones' :  ['Sala de Estar', 'Cocina'],  
                                                                               'items' : [], 'lista_trampas' : []},
        'Cocina'              : { 'lista_habitaciones' :  ['Comedor'],   'items' : ['Botella de veneno'], 'lista_trampas' : []},


        'Entrada'             : { 'lista_habitaciones' :  ['Sala de Estar', 'Despacho', 'Salida'],
                                                                               'items' : [], 'lista_trampas' : []},
        
        'Despacho'            : { 'lista_habitaciones' :  ['Sala de Estar'],   'items' : [], 'lista_trampas' : []},
        'Salida'              : { 'lista_habitaciones' :  ['Entrada'],         'items' : [], 'lista_trampas' : []}
        }

#  Habitación actual : Lista de habitaciones accesibles

# Seteamos habitación inicial (Spawn)
habitacion_actual = "Dormitorio Invitados"
tiene_llave = False
intento_salir = False
game_over = False

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
    if (nueva_habitacion == "Entrada") and tiene_llave:
      print("Te aproximas a la puerta  tan rápido como puedes mientras te aseguras de que no haya ninguna trampa más y usas la llave.")
      time.sleep(2)
      print("La ansiedad dificulta que tus temblorosas manos logren introducir la pequeña llave en la intrincada cerradura sin causar mayor ruido...")
      time.sleep(2)
      print("Casi sin respirar giras la llave, accionando el mecanismo, cada segundo pesando como una eternidad mientras tus pulmones arden cy tu cabeza a punto de estallar")
      print(" Funciona, ¡ Finalmente eres libre!")
      # To-do agregar texto con condiciones para saber si tenemos pruebas de los crímenes / tesoro / si des-vivimos al asesino, etc...
      time.sleep(2)
      break

    elif ((nueva_habitacion == "Entrada") and (not tiene_llave) and (not intento_salir)):
      # To-do: agregar drama
      print("Ves la puerta, la probás, tiene llave, vos no tenés la llave. Raios.")
      intento_salir = True
      time.sleep(2)

    elif ((nueva_habitacion == "Entrada") and (not tiene_llave) and intento_salir):
      print("Una vez más te encuentras frente a la puerta, más sabes que necesitas la llave para escapar.")
      time.sleep(2)

    habitacion_actual = nueva_habitacion

    # Chequear items
    if "Llaves extra" in mapa[habitacion_actual]['items']:
      tiene_llave = True
      print("En la habitación encuentras un juego de llaves extra")
      mapa[habitacion_actual]['items'].remove('Llaves extra')
      time.sleep(2)
      continue

    if "Trampa_Escopeta" in mapa[habitacion_actual]['lista_trampas']:
      game_over = True
      print("Al entrar a la habitación {drama drama drama}, una escopeta te deja con el último look de Kurt Cobain")
      mapa[habitacion_actual]['lista_trampas'].remove('Trampa_Escopeta')
      time.sleep(2)
      break