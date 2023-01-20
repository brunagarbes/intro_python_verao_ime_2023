"""
Este módulo contém as funcões necessárias para fazermos uma pizza
"""


def faz_pizza(tamanho, ingredientes):
    """
    Apresenta a pizza que vamos preparar
    """
    print("Vamos preparar uma pizza de tamanho", tamanho, "com os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print(" - ", ingrediente)


def assa_pizza(escolheu):
    """
    Informa se a pizza já foi ao forno
    """
    if escolheu == True:
        print("A pizza vai ser assada!")
    else:
        print("Já escolheu a sua pizza?")

