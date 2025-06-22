# Análise Exploratória de Dados de Livros com Python

Este projeto realiza uma análise exploratória de um dataset de livros utilizando **Pandas**, **Seaborn**, **Matplotlib** e **SciPy**. A análise inclui geração de histogramas baseados na Regra de Sturges, filtragem por avaliações (rating), estatísticas por categoria e exportação de resultados.

---

## Funcionalidades

- 📊 Geração de histograma de preços com a Regra de Sturges
- 🔍 Identificação de intervalo de menor frequência
- ⭐ Filtragem de livros com avaliação "Five"
- 📚 Estatísticas por categoria (média, moda, menor preço)
- 📈 Exportação de dados em arquivos `.csv`
- 🖼️ Salvamento de histograma como imagem `.png`
- ✅ Análises por classificação (`rating`) dos livros

---

## Estrutura do Dataset

O script espera um arquivo `.csv` com ao menos as seguintes colunas:

| Coluna     | Descrição                          |
|------------|------------------------------------|
| `title`    | Título do livro                    |
| `price`    | Preço do livro (numérico)         |
| `rating`   | Classificação (ex: "Five", "Four") |
| `category` | Categoria do livro (ex: Romance)   |

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/seunome/repositorio-livros.git
cd repositorio-livros
