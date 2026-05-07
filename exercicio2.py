def acaso_semaforo(cor: str):
    cor = cor.lower()

    if cor == 'vermelho':
        return 'Pare'
    elif cor == 'amarelo':
        return 'Atenção'
    elif cor == 'verde':
        return 'Siga'
    else:
        return 'Cor inválida'