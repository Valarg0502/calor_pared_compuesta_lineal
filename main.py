from calor_pared_compuesta_lineal import ParedCompuesta
    
ejemplo_pared_compuesta = {
    'condiciones_interior': {
        'T': 20,
        'h': 10
    },
    'capas': [
        {
            'L': 0.004,
            'k': 0.78,
            'nombre': 'Vidrio'
        },
        {
            'L': 0.01,
            'k': 0.026,
            'nombre': 'Aire'
        },
        {
            'L': 0.004,
            'k': 0.78,
            'nombre': 'Vidrio'
        }
    ],
    'condiciones_exterior': {
        'T': -10,
        'h': 40
    },
    'area': 0.8*1.5
}
pared = ParedCompuesta()
resultado = pared.calcular_pared_compuesta(**ejemplo_pared_compuesta)
print(resultado)
resultado['fig'].show()
input("PRESS ENTER TO CONTINUE.")