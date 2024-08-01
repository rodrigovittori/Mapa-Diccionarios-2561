# M4.L3 - Actividad #2: "Habitaciones" 

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