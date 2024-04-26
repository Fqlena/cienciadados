

import statistics
import pandas as pd

# Atribui a variável o nome do arquivo a ser utilizado como banco de dados.
nome_arquivo = "C:/Users/Avell/Downloads/glicose_data_suja.csv"

# Cria a classe Glicemia
class Glicemia:
    def __init__(self, dia, ano, glicemia, insulina, kcal, carb, sono):
        self.dia = dia
        self.ano = int(ano)
        self.glicemia = int(glicemia)
        self.insulina = int(insulina)
        self.kcal = int(kcal)
        self.carb = int(carb)
        self.sono = sono

    def __str__(self):
        return f"{self.dia}, {self.ano}, {self.glicemia}, {self.insulina}, {self.kcal}, {self.carb}, {self.sono}"

# Abre e lê o arquivo e cria um DataFrame
dados = []
with open(nome_arquivo, "r", encoding="utf8") as arquivo:
    for linha in arquivo:
        partes = linha.strip().split(",")
        dados.append(partes)

df = pd.DataFrame(dados, columns=["Dia", "Ano", "AC", "Glicemia", "Insulina", "Kcal", "Carb", "Sono"])
df = df.astype({"Ano": int, "Glicemia": int, "Insulina": int, "Kcal": int, "Carb": int})

# Calcula e imprime a média, mediana e moda para glicemia, kcal e carb em estilo de tabela.
print("*** Tabela com os resultados ***\n")
print("|          | Média | Mediana | Moda |")
print("|----------|-------|---------|------|")
for atributo in ['Glicemia', 'Kcal', 'Carb']:
    media = df[atributo].mean()
    mediana = df[atributo].median()
    try:
        moda = df[atributo].mode()[0]
    except KeyError:
        moda = 'N/A'
    print(f"| {atributo} | {media:.2f} | {mediana:.2f} | {moda} |")

# Imprime o DataFrame
print("")
print("*** Lista o conteúdo do banco de dados ***\n")
print(df)

     
