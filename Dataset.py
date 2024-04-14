class Dataset:
    # Dataset con las conexiones entre las estaciones y los costos asociados
    _dataset = {
    # Troncal A - Caracas
    "Calle 22": {"Profamilia": 1, "Calle 57": 2, "Calle 63": 1},
    "Profamilia": {"Calle 22": 1, "Calle 57": 1, "Calle 63": 2, "Calle 19": 3},
    "Calle 57": {"Calle 22": 2, "Profamilia": 1, "Calle 63": 2, "Calle 19": 1},
    "Calle 63": {"Calle 22": 1, "Profamilia": 2, "Calle 57": 2, "Calle 19": 1},
    "Calle 19": {"Profamilia": 3, "Calle 57": 1, "Calle 63": 1, "Marly": 2},
    "Marly": {"Calle 19": 2, "Avenida 39": 3, "Calle 76": 1},
    "Avenida 39": {"Marly": 3, "Calle 76": 2, "Calle 26": 1},
    "Calle 76": {"Marly": 1, "Avenida 39": 2, "Calle 26": 2, "Calle 72": 3},
    "Calle 26": {"Avenida 39": 1, "Calle 76": 2, "Calle 72": 1},
    "Calle 72": {"Calle 76": 3, "Calle 26": 1, "Flores": 2},
    "Flores": {"Calle 72": 2, "Calle 45": 1},
    "Calle 45": {"Flores": 1, "Pepe Sierra": 3},

    # Troncal B - Norte
    "Pepe Sierra": {"Calle 45": 3, "Calle 146": 2},
    "Calle 146": {"Pepe Sierra": 2, "Calle 100": 1},
    "Calle 100": {"Calle 146": 1, "Alcalá": 3},
    "Alcalá": {"Calle 100": 3, "Cardio Infantil": 2},
    "Cardio Infantil": {"Alcalá": 2, "Calle 187": 1},
    "Calle 187": {"Cardio Infantil": 1, "Héroes": 2},
    "Héroes": {"Calle 187": 2, "Terminal": 3},
    "Terminal": {"Héroes": 3, "Calle 85": 2},
    "Calle 85": {"Terminal": 2, "Calle 106": 1},
    "Calle 106": {"Calle 85": 1, "Prado Veraniego": 2},
    "Prado Veraniego": {"Calle 106": 2, "Toberín": 3},
    "Toberín": {"Prado Veraniego": 3, "Virrey": 1},
    "Virrey": {"Toberín": 1, "Calle 127": 2},
    "Calle 127": {"Virrey": 2, "Mazuren": 3},
    "Mazuren": {"Calle 127": 3, "Calle 142": 2},
    "Calle 142": {"Mazuren": 2, "La Campiña": 1},

    # Troncal C - Suba
    "La Campiña": {"Calle 142": 1, "Rionegro": 3},
    "Rionegro": {"La Campiña": 3, "Suba - Calle 95": 1},
    "Suba - Calle 95": {"Rionegro": 1, "San Martín": 2},
    "San Martín": {"Suba - Calle 95": 2, "Suba - Av. Boyacá": 1},
    "Suba - Av. Boyacá": {"San Martín": 1, "Gratamira": 3},
    "Gratamira": {"Suba - Av. Boyacá": 3, "Clínica Shaio": 2},
    "Clínica Shaio": {"Gratamira": 2, "Puentelargo": 1},
    "Puentelargo": {"Clínica Shaio": 1, "Suba - Calle 100": 3},
    "Suba - Calle 100": {"Puentelargo": 3, "Humedal Córdoba": 2},
    "Humedal Córdoba": {"Suba - Calle 100": 2, "Suba - Tv. 91": 1},
    "Suba - Tv. 91": {"Humedal Córdoba": 1, "Niza - Calle 127": 3},
    "Niza - Calle 127": {"Suba - Tv. 91": 3, "21 Angeles": 2},
    "21 Angeles": {"Niza - Calle 127": 2, "Avenida 68": 1},

    # Troncal D - Calle 80
    "Avenida 68": {"21 Angeles": 1, "Avenida Ciudad de Cali": 3},
    "Avenida Ciudad de Cali": {"Avenida 68": 3, "Carrera 90": 2},
    "Carrera 90": {"Avenida Ciudad de Cali": 2, "Escuela Militar": 3},
    "Escuela Militar": {"Carrera 90": 3, "Las Ferias": 2},
    "Las Ferias": {"Escuela Militar": 2, "Polo": 1},
    "Polo": {"Las Ferias": 1, "Carrera 47": 3},
    "Carrera 47": {"Polo": 3, "Quirigua": 2},
    "Quirigua": {"Carrera 47": 2, "Minuto de Dios": 1},
    "Minuto de Dios": {"Quirigua": 1, "Carrera 53": 2},
    "Carrera 53": {"Minuto de Dios": 2, "Granja - Carrera 77": 3},
    "Granja - Carrera 77": {"Carrera 53": 3, "Avenida Boyac": 1},
    "Avenida Boyac": {"Granja - Carrera 77": 1, "Paloquemao": 2},

    # Troncal E - NQS Central
    "Paloquemao": {"Avenida Boyac": 2, "CAD": 1},
    "CAD": {"Paloquemao": 1, "Coliseo": 3},
    "Coliseo": {"CAD": 3, "Universidad Nacional": 2},
    "Universidad Nacional": {"Coliseo": 2, "Guatoque-Veraguas": 1},
    "Guatoque-Veraguas": {"Universidad Nacional": 1, "Tygua-San José": 3},
    "Tygua-San José": {"Guatoque-Veraguas": 3, "Av. El Dorado": 2},
    "Av. El Dorado": {"Tygua-San José": 2, "Ricaurte": 1},
    "Ricaurte": {"Av. El Dorado": 1, "Av Chile": 3},
    "Av Chile": {"Ricaurte": 3, "Simon Bolívar": 2},
    "Simon Bolívar": {"Av Chile": 2, "Campin": 1},
    "Campin": {"Simon Bolívar": 1, "NQS - Calle 75": 3},
    "NQS - Calle 75": {"Campin": 3, "La Castellana": 2},
    "La Castellana": {"NQS - Calle 75": 2},

    # Troncal F - Americas
    "De La Sabana": {"Mundo Aventura": 1},
    "Mundo Aventura": {"De La Sabana": 1, "Ricaurte": 2},
    "Ricaurte": {"Mundo Aventura": 2, "Pradera": 1},
    "Pradera": {"Ricaurte": 1, "Cr 43": 3},
    "Cr 43": {"Pradera": 3, "Mandalay": 2},
    "Mandalay": {"Cr 43": 2, "Américas - Cr 53A": 1},
    "Américas - Cr 53A": {"Mandalay": 1, "Banderas": 3},
    "Banderas": {"Américas - Cr 53A": 3, "Zona Industrial": 2},
    "Zona Industrial": {"Banderas": 2, "CDS - Cr 32": 1},
    "CDS - Cr 32": {"Zona Industrial": 1, "Marsella": 3},
    "Marsella": {"CDS - Cr 32": 3, "Biblioteca Tintal": 2},
    "Biblioteca Tintal": {"Marsella": 2, "San Facón Cr 22": 1},
    "San Facón Cr 22": {"Biblioteca Tintal": 1, "Puente Aranda": 3},
    "Puente Aranda": {"San Facón Cr 22": 3, "Patio Bonito": 2},
    "Patio Bonito": {"Puente Aranda": 2, "Tv 86": 1},
    "Tv 86": {"Patio Bonito": 1},

    # Troncal G - NQS Sur
    "Comuneros": {"TERRERO-HOSPITAL CV": 1},
    "TERRERO-HOSPITAL CV": {"Comuneros": 1, "SAN MATEO": 2},
    "SAN MATEO": {"TERRERO-HOSPITAL CV": 2, "NQS - Calle 38A Sur": 1},
    "NQS - Calle 38A Sur": {"SAN MATEO": 1, "Sevillana": 3},
    "Sevillana": {"NQS - Calle 38A Sur": 3, "Perdomo": 2},
    "Perdomo": {"Sevillana": 2, "LA DESPENSA": 1},
    "LA DESPENSA": {"Perdomo": 1, "BOSA": 3},
    "BOSA": {"LA DESPENSA": 3, "NQS - Calle 30 Sur": 2},
    "NQS - Calle 30 Sur": {"BOSA": 2, "LEON XIII": 1},
    "LEON XIII": {"NQS - Calle 30 Sur": 1, "General Santander": 3},
    "General Santander": {"LEON XIII": 3, "Madelena": 2},
    "Madelena": {"General Santander": 2, "Alquería": 1},
    "Alquería": {"Madelena": 1, "Sena": 3},
    "Sena": {"Alquería": 3, "Santa Isabel": 2},
    "Santa Isabel": {"Sena": 2, "Venecia": 1},
    "Venecia": {"Santa Isabel": 1},

    # Troncal H - Caracas Sur
    "Calle 40 Sur": {"Restrepo": 1},
    "Restrepo": {"Calle 40 Sur": 1, "Socorro": 2},
    "Socorro": {"Restrepo": 2, "Avenida Jiménez": 3},
    "Avenida Jiménez": {"Socorro": 3, "Hortúa": 1},
    "Hortúa": {"Avenida Jiménez": 1, "Quiroga": 2},
    "Quiroga": {"Hortúa": 2, "Fucha": 1},
    "Fucha": {"Quiroga": 1, "Nariño": 3},
    "Nariño": {"Fucha": 3, "Santa Lucía": 2},
    "Santa Lucía": {"Nariño": 2, "Hospital": 1},
    "Hospital": {"Santa Lucía": 1, "Consuelo": 3},
    "Consuelo": {"Hospital": 3, "Biblioteca": 2},
    "Biblioteca": {"Consuelo": 2, "Olaya": 1},
    "Olaya": {"Biblioteca": 1, "Tercer Milenio": 3},
    "Tercer Milenio": {"Olaya": 3, "Molinos": 2},
    "Molinos": {"Tercer Milenio": 2, "Parque": 1},
    "Parque": {"Molinos": 1},

    # Troncal J - Eje Ambiental
    "Av Jiménez": {"Museo del Oro": 1},
    "Museo del Oro": {"Av Jiménez": 1},

    # Troncal K - Avenida El Dorado
    "Maloka": {"Gran Estación": 1},
    "Gran Estación": {"Maloka": 1, "Aguas": 3},
    "Aguas": {"Gran Estación": 3, "Parque Renacimiento": 2},
    "Parque Renacimiento": {"Aguas": 2, "Universidades": 1},
    "Universidades": {"Parque Renacimiento": 1, "CAN": 3},
    "CAN": {"Universidades": 3, "Ciudad Universitaria": 2},
    "Ciudad Universitaria": {"CAN": 2, "Quinta Paredes": 1},
    "Quinta Paredes": {"Ciudad Universitaria": 1, "Avenida Rojas": 3},
    "Avenida Rojas": {"Quinta Paredes": 3, "Corferias": 2},
    "Corferias": {"Avenida Rojas": 2, "Modelia": 1},
    "Modelia": {"Corferias": 1, "Plaza de la Democracia": 3},
    "Plaza de la Democracia": {"Modelia": 3, "Gobernación": 2},
    "Gobernación": {"Plaza de la Democracia": 2, "Normandia": 1},
    "Normandia": {"Gobernación": 1},

    # Troncal L - Carrera Decima
    "San Victorino": {"Ciudad Jardín": 1},
    "Ciudad Jardín": {"San Victorino": 1, "Country Sur": 3},
    "Country Sur": {"Ciudad Jardín": 3, "San Diego": 2},
    "San Diego": {"Country Sur": 2, "Las Nieves": 1},
    "Las Nieves": {"San Diego": 1, "Hospitales": 3},
    "Hospitales": {"Las Nieves": 3, "Bicentenario": 2},
    "Bicentenario": {"Hospitales": 2, "Museo Nacional": 1},
    "Museo Nacional": {"Bicentenario": 1, "Policarpa": 3},
    "Policarpa": {"Museo Nacional": 3, "Avenida 1 de Mayo": 2},
    "Avenida 1 de Mayo": {"Policarpa": 2}
    }

    @classmethod
    def obtener_dataset(cls):
        return cls._dataset