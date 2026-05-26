import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title="Dashboard de Prefeitos",
    layout="wide"
)

# ==========================================
# LEITURA DOS DADOS
# ==========================================

dados = pd.read_excel("DadosBahia_20251.xlsx")

dados.columns = dados.columns.str.strip()

# ==========================================
# TÍTULO
# ==========================================

st.title("Dashboard de Prefeitos")

st.markdown("---")

# ==========================================
# TABELA DESCRITIVA
# ==========================================

st.subheader("Estatísticas Descritivas")

st.table(
    dados.describe().round(2)
)

# ==========================================
# HISTOGRAMA
# ==========================================

grafico = px.histogram(
    dados,
    x="Idade",
    title="Distribuição de Idade dos Prefeitos",
    color_discrete_sequence=["#323795"],
    nbins=15
)

grafico.update_layout(
    template="plotly_white",

    title={
        "text": "Distribuição de Idade dos Prefeitos",
        "x": 0.5,
        "xanchor": "center",
        "font": {
            "size": 24,
            "color": "black"
        }
    },

    xaxis_title="Idade",
    yaxis_title="Quantidade",

    height=500
)

st.plotly_chart(
    grafico,
    use_container_width=True
)

# ==========================================
# GRÁFICO DE BARRAS
# ==========================================

contagem = dados.groupby(
    ["Escolaridade", "Genero"]
).size().reset_index(name="Quantidade")

grafico2 = px.bar(
    contagem,
    x="Escolaridade",
    y="Quantidade",
    color="Genero",
    color_discrete_sequence=["#323795", "#D72638"],
    barmode="group"
)

grafico2.update_layout(
    template="plotly_white",

    title={
        "text": "Distribuição da Escolaridade por Gênero",
        "x": 0.5,
        "xanchor": "center",
        "font": {
            "size": 22,
            "color": "black"
        }
    },

    xaxis_title="Escolaridade",
    yaxis_title="Quantidade",

    height=500
)

st.plotly_chart(
    grafico2,
    use_container_width=True
)
