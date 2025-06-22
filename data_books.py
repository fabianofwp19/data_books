#ATIVIDADE AVALIATIVA DA MATÉRIA DE CIÊNCIA DE DADOS PARA HUMANAS
#POR: FABIANO MIGUEL
#GIT: fabianofwp19

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
import os

# Carregar os dados
df = pd.read_csv("books.csv")  

# Criar pasta de saída
output_dir = "resultados"
os.makedirs(output_dir, exist_ok=True)

# ---------- PARTE 3 ----------
print("3 – Histograma com Regra de Sturges")

# a) Quantidade de observações
n = len(df)

# b) Amplitude
amplitude = df['price'].max() - df['price'].min()

# c) K (Sturges)
k = int(np.ceil(1 + 3.322 * np.log10(n)))

# d) Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['price'], bins=k, kde=False, color='skyblue', edgecolor='black')
plt.title("Histograma de Preços (Sturges)")
plt.xlabel("Preço")
plt.ylabel("Frequência")
plt.grid(True)
hist_path = os.path.join(output_dir, "histograma_sturges.png")
plt.savefig(hist_path)
plt.close()

# e) Menor frequência - detalhamento das classes
bins = np.linspace(df['price'].min(), df['price'].max(), k+1)
counts, bin_edges = np.histogram(df['price'], bins=bins)

# Montar DataFrame com classes e frequências
classes = []
for i in range(len(counts)):
    classes.append({
        'Classe': f"{bin_edges[i]:.2f} - {bin_edges[i+1]:.2f}",
        'Frequência': counts[i]
    })
tabela_classes = pd.DataFrame(classes)

print("\nTabela de classes e frequências:")
print(tabela_classes)

# Encontrar classe com menor frequência
min_freq = tabela_classes['Frequência'].min()
classe_min_freq = tabela_classes[tabela_classes['Frequência'] == min_freq]

print("\nClasse com menor frequência e quantidade de observações:")
print(classe_min_freq)

# Exportar resumo do item 3 e tabela das classes
resumo3 = {
    "Qtd Observações": [n],
    "Amplitude": [amplitude],
    "K (Sturges)": [k],
    "Menor Frequência": [min_freq],
    "Intervalo Menor Freq.": [classe_min_freq['Classe'].values[0]]
}
pd.DataFrame(resumo3).to_csv(os.path.join(output_dir, "resumo_sturges.csv"), index=False)
tabela_classes.to_csv(os.path.join(output_dir, "frequencia_classes.csv"), index=False)

# ---------- PARTE 4 ----------
print("4 – Análise com rating 'Five'")
df_five = df[df['rating'] == 'Five']

# a) Livro mais barato
livro_mais_barato = df_five.loc[df_five['price'].idxmin()]

# b) Categoria com maior média de preços
media_precos = df_five.groupby('category')['price'].mean()
categoria_mais_cara = media_precos.idxmax()

# c) Média e moda em Business
df_business = df_five[df_five['category'] == 'Business']
media_business = df_business['price'].mean()
moda_business = df_business['price'].mode().iloc[0] if not df_business['price'].mode().empty else None

# d) Livro mais barato em Romance
df_romance = df_five[df_five['category'] == 'Romance']
romance_min = df_romance.loc[df_romance['price'].idxmin()] if not df_romance.empty else None

# Exportar resultados da parte 4
resumo4 = {
    "Livro mais barato (Título)": [livro_mais_barato['title']],
    "Preço mais barato": [livro_mais_barato['price']],
    "Categoria (mais barata)": [livro_mais_barato['category']],
    "Categoria com maior média de preços": [categoria_mais_cara],
    "Média preços (Business)": [media_business],
    "Moda preços (Business)": [moda_business],
    "Preço mais barato (Romance)": [romance_min['price']] if romance_min is not None else ["N/A"],
    "Título (Romance)": [romance_min['title']] if romance_min is not None else ["N/A"]
}
pd.DataFrame(resumo4).to_csv(os.path.join(output_dir, "resumo_rating_five.csv"), index=False)

# ---------- PARTE 5 ----------
print("5 – Análise geral dos livros")

# a) Quantidade por classificação
quant_por_rating = df['rating'].value_counts().reset_index()
quant_por_rating.columns = ['rating', 'quantidade']
quant_por_rating.to_csv(os.path.join(output_dir, "quantidade_por_rating.csv"), index=False)

# b) Livro mais caro por rating
mais_caro_por_rating = df.loc[df.groupby('rating')['price'].idxmax()]
mais_caro_por_rating[['rating', 'title', 'price']].to_csv(os.path.join(output_dir, "livro_mais_caro_por_rating.csv"), index=False)

print(f"\n✅ Resultados exportados para a pasta '{output_dir}'.")
print(f"📊 Imagem do histograma salva como: {hist_path}")
