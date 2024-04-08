from collections import deque

# Função para verificar se um estado já foi visitado
def estado_visitado(estado, visitados):
    return estado in visitados

# Função para verificar se o estado é objetivo
def estado_objetivo(estado, litros_desejados):
    return estado[0] == litros_desejados or estado[1] == litros_desejados

# Função para gerar novos estados possíveis
def gerar_estados(estado, visitados):
    novos_estados = []
    jarro_A, jarro_B = estado

    # Operações possíveis: encher, esvaziar, transferir
    operacoes = [
        ("Encher jarro A", (5, jarro_B)),
        ("Encher jarro B", (jarro_A, 7)),
        ("Esvaziar jarro A", (0, jarro_B)),
        ("Esvaziar jarro B", (jarro_A, 0)),
        ("Transferir de B para A", (min(jarro_A + jarro_B, 5), max(0, jarro_A + jarro_B - 5))),
        ("Transferir de A para B", (max(0, jarro_A + jarro_B - 7), min(jarro_A + jarro_B, 7)))
    ]

    # Para cada operação, verifica se o novo estado é válido e não foi visitado
    for operacao, (novo_jarro_A, novo_jarro_B) in operacoes:
        novo_estado = (novo_jarro_A, novo_jarro_B)
        if not estado_visitado(novo_estado, visitados):
            novos_estados.append((operacao, novo_estado))
            visitados.add(novo_estado)
    return novos_estados

# Algoritmo de busca em largura
def busca_vasilhame(litros_desejados):
    visitados = set()
    fila = deque([("", (0, 0))])  # Começa com os jarros vazios
    while fila:
        operacao, estado = fila.popleft()
        print(f"Passo: {operacao} | Jarro A ({estado[0]} litros)  Jarro B ({estado[1]} litros)")
        if estado_objetivo(estado, litros_desejados):
            return operacao
        novos_estados = gerar_estados(estado, visitados)
        fila.extend((operacao + " -> " + nova_operacao, novo_estado) for nova_operacao, novo_estado in novos_estados)
    return "Não foi possível encontrar uma solução."

# Função principal
def main():
    litros_desejados = int(input("Digite a quantidade desejada de litros: "))
    print("\nSolução:", busca_vasilhame(litros_desejados))

# Executa o programa
if __name__ == "__main__":
    main()