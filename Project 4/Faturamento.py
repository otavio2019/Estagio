class FaturamentoEstado:
    def __init__(self, estado, valor):
        self.estado = estado
        self.valor = valor

class Distribuidora:
    def __init__(self, faturamentos):
        self.faturamentos = faturamentos

    def calcular_total_mensal(self):
        return sum(faturamento.valor for faturamento in self.faturamentos)

    def calcular_percentual_por_estado(self):
        total_mensal = self.calcular_total_mensal()
        return {faturamento.estado: (faturamento.valor / total_mensal) * 100 for faturamento in self.faturamentos}

# Exemplo de uso
faturamentos = [
    FaturamentoEstado("SP", 67836.43),
    FaturamentoEstado("RJ", 36678.66),
    FaturamentoEstado("MG", 29229.88),
    FaturamentoEstado("ES", 27165.48),
    FaturamentoEstado("Outros", 19849.53)
]

distribuidora = Distribuidora(faturamentos)

percentuais = distribuidora.calcular_percentual_por_estado()

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")
