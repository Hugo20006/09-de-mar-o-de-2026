peso = float(input("Digite o seu peso corporal: "))
#constantes
capacidade_por_copo = 0.25
litro_por_kg = 0.015

#funções
def calcular_agua (peso, litro_por_kg):
    return peso * litro_por_kg

def calcular_copos (agua_total, capacidade_por_copo):
    return agua_total/capacidade_por_copo

#processo
agua_total = calcular_agua(peso, litro_por_kg)
copo = calcular_copos(agua_total, capacidade_por_copo)

#saída
print(f"Seu peso é: {peso:.2f} kg")
print(f"Você deve beber aproximadamente {copo} de água por dia")
print(f"Você meta de água é de {agua_total} ml")
