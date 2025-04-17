def preparar_ingredientes():# faça a separação dos ingredientes
    print("Pegando os ingredientes...")
    ingredientes = [
        "3 ovos",
        "2 xícaras de farinha de trigo",
        "1 xícara de açúcar",
        "1 xícara de leite",
        "1 colher de fermento em pó",
        "1/2 xícara de óleo"
    ]
    for item in ingredientes:
        print(f"Adicionando {item}")
    print("Ingredientes preparados!\n")
    return ingredientes

def misturar(ingredientes):
    print("Misturando os ingredientes...")
    print("Bate tudo até a massa ficar homogênea.\n")
    return "massa homogênea"

def assar(massa):
    print("Pré-aquecendo o forno a 180°C...")
    print("Colocando a massa no forno...")
    print("Assando por 40 minutos...\n")
    return "Bolo assado"

def servir(bolo):
    print("Retirando o bolo do forno...")
    print("Esperando esfriar...")
    print("Cortando o bolo...")
    print("Bolo pronto para servir! 🍰")

def fazer_bolo():
    ingredientes = preparar_ingredientes()
    massa = misturar(ingredientes)
    bolo = assar(massa)
    servir(bolo)
# Executar
fazer_bolo()