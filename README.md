# Problema da Troca de Moedas (Coin Change Problem)

## Integrantes do Grupo
-Nome: Augusto Rocha Silva RM556316

## Introdução

O Problema da Troca de Moedas (Coin Change Problem) consiste em determinar o menor número de moedas necessárias para formar um valor M, dado um conjunto de moedas de valores inteiros e quantidade ilimitada.

Este problema é um caso clássico de Otimização e Programação Dinâmica, pois envolve a escolha de combinações ótimas de subsoluções.

## Definição de Programação Dinâmica

A Programação Dinâmica (PD) é uma técnica usada para resolver problemas complexos dividindo-os em subproblemas menores, resolvendo cada um uma única vez e armazenando seus resultados.

### Pilares:
- Subestrutura Ótima: A solução ótima do problema pode ser construída a partir das soluções ótimas de seus subproblemas.
- Subproblemas Sobrepostos: Os mesmos subproblemas aparecem diversas vezes, justificando o uso de cache (memoização) ou tabelas (PD).

## Implementações

### 1. Estratégia Gulosa (Iterativa)

- Ideia: Escolhe sempre a maior moeda possível até atingir o montante.
- Limitação: Só funciona corretamente em sistemas de moedas “canônicos” (ex: 1, 5, 10, 25, 50).
- Complexidade:
  - Tempo: O(n log n)
  - Espaço: O(1)
- Exemplo de falha:
  Para M = 6 e moedas = [1, 3, 4], o algoritmo guloso escolhe 4 + 1 + 1 = 6 (3 moedas), mas o ótimo é 3 + 3 = 6 (2 moedas).

### 2. Recursiva Pura (Ingênua)

- Ideia: Tenta todas as combinações possíveis.
- Problema: Recalcula subproblemas repetidamente.
- Complexidade:
  - Tempo: O(n^M) (exponencial)
  - Espaço: O(M)
- Uso: Apenas para fins didáticos, pois é ineficiente para valores grandes.

### 3. Recursiva com Memoização (Top Down)

- Ideia: Usa cache para armazenar resultados de subproblemas já resolvidos.
- Vantagem: Evita recomputações desnecessárias.
- Complexidade:
  - Tempo: O(n * M)
  - Espaço: O(M)
- Ligação com PD: É uma abordagem Top-Down de Programação Dinâmica.

### 4. Programação Dinâmica (Bottom Up)

- Ideia: Resolve os subproblemas menores primeiro e constrói a solução final de forma iterativa.
- Tabela DP: dp[i] representa o menor número de moedas para o montante i.
- Complexidade:
  - Tempo: O(n * M)
  - Espaço: O(M)
- Vantagem: Evita chamadas recursivas e tem leve ganho de performance sobre o Top-Down.

## Comparativo de Complexidade

| Abordagem | Tipo | Tempo | Espaço | Observações |
|------------|------|--------|--------|--------------|
| Estratégia Gulosa | Iterativa | O(n log n) | O(1) | Não garante solução ótima |
| Recursiva Pura | Recursiva | O(n^M) | O(M) | Muito lenta |
| Recursiva + Memoização | Top-Down | O(n * M) | O(M) | Boa eficiência |
| Programação Dinâmica | Bottom-Up | O(n * M) | O(M) | Melhor abordagem prática |

## Conclusão

O método de Programação Dinâmica Bottom-Up é o mais eficiente e robusto para resolver o Problema da Troca de Moedas. Ele explora a subestrutura ótima e elimina o reprocessamento de subproblemas, mostrando como a PD é essencial em problemas de otimização.
