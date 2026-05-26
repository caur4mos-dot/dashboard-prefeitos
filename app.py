import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="Dashboard de Prefeitos",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# OCULTAR MENU STREAMLIT
# ==================================================

hide_streamlit = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit, unsafe_allow_html=True)

# ==================================================
# LEITURA DOS DADOS
# ==================================================

dados = pd.read_excel("DadosBahia_20251.xlsx")

dados.columns = dados.columns.str.strip()

# ==================================================
# TÍTULO
# ==================================================

st.markdown(
    """
    <h1 style='text-align: center;
    color: #323795;
    font-size: 42px;'>
    Dashboard de Prefeitos
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==================================================
# KPIs
# ==================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total de Prefeitos",
        len(dados)
    )

with col2:
    st.metric(
        "Idade Média",
        round(dados["Idade"].mean(), 1)
    )

with col3:
    st.metric(
        "Maior Idade",
        dados["Idade"].max()
    )

st.markdown("---")

# ==================================================
# ESTATÍSTICAS
# ==================================================

st.subheader("Estatísticas Descritivas")

st.table(
    dados.describe().round(2)
)

st.markdown("---")

# ==================================================
# HISTOGRAMA
# ==================================================

grafico = px.histogram(
    dados,
    x="Idade",
    nbins=15,
    color_discrete_sequence=["#323795"]
)

grafico.update_layout(
    template="plotly_white",

    title={
        "text": "Distribuição de Idade",
        "x": 0.5,
        "font": {
            "size": 24,
            "color": "black"
        }
    },

    xaxis_title="Idade",
    yaxis_title="Quantidade",

    height=450,

    showlegend=False
)

# REMOVE BOTÕES DO PLOTLY
config = {
    "displayModeBar": False
}

# ==================================================
# GRÁFICO DE BARRAS
# ==================================================

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
        "text": "Escolaridade por Gênero",
        "x": 0.5,
        "font": {
            "size": 24,
            "color": "black"
        }
    },

    xaxis_title="Escolaridade",
    yaxis_title="Quantidade",

    height=450
)

# ==================================================
# LAYOUT DOS GRÁFICOS
# ==================================================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        grafico,
        use_container_width=True,
        config=config
    )

with col2:
    st.plotly_chart(
        grafico2,
        use_container_width=True,
        config=config
    )
