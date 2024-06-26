import statistics

nome_arquivo = "glicose_data_suja.csv"

class Glicemia:
    def __init__(self, dia, ano, glicemia, insulina, kcal, carb, sono):
        self.dia = str(dia)
        self.ano = int(ano)
        self.glicemia = int(glicemia)
        self.insulina = int(insulina)
        self.kcal = int(kcal)
        self.carb = int(carb)
        self.sono = str(sono)

    def __str__(self):
        return f"{self.dia}, {self.ano}, {self.glicemia}, {self.insulina}, {self.kcal}, {self.carb}, {self.sono}"
        #return f"{self.dia}"

# open arq

lista_glicemias = []
#try:
with open(nome_arquivo,"r",encoding="utf8") as procurador:
    for i,linha in enumerate(procurador):
        vetor_linha = linha.split(",")
        #obj = Glicemia(vetor_linha[0])
        try:
            obj = Glicemia(vetor_linha[0],vetor_linha[1],vetor_linha[3],vetor_linha[4],vetor_linha[5],vetor_linha[6],vetor_linha[7])
            lista_glicemias.append(obj)
        except Exception as e:
            print('Erro:' , i, e)
#except:
 #   print("Algum problema para localizar o arquivo...")


# media mediana moda
def calcular_media(valores):
    return sum(valores) / len(valores)

def calcular_mediana(valores):
    return statistics.median(valores)

def calcular_moda(valores):
    return statistics.mode(valores)


for atributo in ['glicemia', 'kcal', 'carb']:
    valores = [getattr(glicemia, atributo) for glicemia in lista_glicemias]
    print(f"A média da {atributo} é", calcular_media(valores))
    print(f"A mediana da {atributo} é", calcular_mediana(valores))
    print(f"A moda da {atributo} é", calcular_moda(valores))
