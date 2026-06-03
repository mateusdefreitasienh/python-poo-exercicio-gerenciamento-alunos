def input_nome(msg):
    """
    Trata a captura de pelo menos dois nomes
    Entrada: str da mensagem
    Saída: str com o mínimo de dois nomes
    """
    while True:
        nome = input(msg).strip()
        dois_nomes = False
        for letra in nome:
            if letra == " ":
                dois_nomes = True
        if dois_nomes:
            break
        else:
            print("Necessario informar [nome] e [sobrenome]")
    return nome

def input_nota(nota, minimo=0, maximo=10):
    """
    Trata da captura de int em python
    Entrada: str da mensagem, minimo e maximo
    Saída valor int
    """

    while True:
        try:
            valor = int(input(nota))
            if minimo <= valor <= maximo:
                break
            else:
                print(f"Entrada inválida, não atende o intervalo {minimo} e {maximo}")
        except Exception as e:
            print(f"Entrada deve ser um numero inteiro")
            print(f"Erro: {e}")
    return valor