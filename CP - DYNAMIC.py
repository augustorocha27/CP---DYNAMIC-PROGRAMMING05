
def qtdeMoedas(M, moedas):
    moedas.sort(reverse=True)
    qtd = 0
    for moeda in moedas:
        while M >= moeda:
            M -= moeda
            qtd += 1
    return qtd if M == 0 else -1


def qtdeMoedasRec(M, moedas):
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        res = qtdeMoedasRec(M - moeda, moedas)
        menor = min(menor, 1 + res)
    return menor


def qtdeMoedasRecMemo(M, moedas, memo=None):

    if memo is None:
        memo = {}

    if M in memo:
        return memo[M]
    if M == 0:
        return 0
    if M < 0:
        return float('inf')

    menor = float('inf')
    for moeda in moedas:
        res = qtdeMoedasRecMemo(M - moeda, moedas, memo)
        menor = min(menor, 1 + res)

    memo[M] = menor
    return menor


def qtdeMoedasPD(M, moedas):

    dp = [float('inf')] * (M + 1)
    dp[0] = 0

    for i in range(1, M + 1):
        for moeda in moedas:
            if i - moeda >= 0:
                dp[i] = min(dp[i], dp[i - moeda] + 1)

    return dp[M] if dp[M] != float('inf') else -1


if __name__ == "__main__":
    print(qtdeMoedas(6, [1, 3, 4]))
    print(qtdeMoedasRec(6, [1, 3, 4]))
    print(qtdeMoedasRecMemo(6, [1, 3, 4]))
    print(qtdeMoedasPD(6, [1, 3, 4]))
