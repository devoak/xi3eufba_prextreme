import sys

def main():
    entrada = sys.stdin.read().split()
    if not entrada:
        return

    # OTIMIZAÇÃO 1: 'map' nativo em C é dezenas de vezes mais rápido que um laço 'for'
    dados = list(map(int, entrada))
    
    N = dados[0]
    # OTIMIZAÇÃO 2: Tuplas são mais rápidas para leitura de dados estáticos do que listas
    disponivel = tuple(dados[1:N + 1])
    
    M = dados[N + 1]
    
    pratos = []
    idx = N + 2
    for _ in range(M):
        pratos.append(tuple(dados[idx:idx + N]))
        idx += N

    max_programmers = 0

    for i in range(M):
        # OTIMIZAÇÃO 3: Cache de variável local. 
        # Acessar 'prato_i[k]' é mais rápido que acessar 'pratos[i][k]' repetidas vezes.
        prato_i = pratos[i] 
        
        for j in range(i + 1, M):
            prato_j = pratos[j]
            
            # Substituímos o float('inf') por um número inteiro gigante. 
            # Operações exclusivas entre inteiros são mais leves no interpretador.
            refeicoes_deste_par = 2147483647 

            for k in range(N):
                necessidade = prato_i[k] + prato_j[k]
                
                if necessidade > 0:
                    possiveis = disponivel[k] // necessidade
                    
                    # OTIMIZAÇÃO 4 (A MAIS IMPORTANTE - Poda / Pruning):
                    # Se este ingrediente já limitou o número de refeições para um valor
                    # menor ou igual ao recorde atual, abortamos este par imediatamente.
                    if possiveis <= max_programmers:
                        refeicoes_deste_par = -1
                        break
                    
                    if possiveis < refeicoes_deste_par:
                        refeicoes_deste_par = possiveis

            if refeicoes_deste_par > max_programmers:
                max_programmers = refeicoes_deste_par

    print(max_programmers)

if __name__ == '__main__':
    main()