import xml.etree.ElementTree


# importación  del fichero de configuración (Basic_Config_Game.xml)
def import_config():
    min_players, max_players, max_rounds, initial_points, auto_mode, num = "", "", "", "", "", 0
    tree = xml.etree.ElementTree.parse("Basic_Config_Game.xml")
    root = tree.getroot()
    config = []
    for child in root:
        config.append(child.text)
    for i in config:
        num += 1
        if num == 1:
            min_players = int(i)
        elif num == 2:
            max_players = int(i)
        elif num == 3:
            max_rounds = int(i)
        elif num == 4:
            initial_points = int(i)
        elif num == 5:
            auto_mode = i
    return min_players, max_players, max_rounds, initial_points, auto_mode


# importación  del fichero de configuración (Cartas.xml)
def import_cartas():
    tree = xml.etree.ElementTree.parse("Cartas.xml")
    root = tree.getroot()
    config = []
    mazo = []
    n = 0
    for child in root:
        for i in child:
            try:
                config.append(int(i.text))
            except ValueError:
                try:
                    config.append(float(i.text))
                except ValueError:
                    config.append(i.text)
    while True:
        try:
            if config[n + 4].upper() == "SI":
                mazo.append([config[n], config[n + 1], config[n + 3], config[n + 2]])
            n += 5
        except IndexError:
            break
    return mazo
