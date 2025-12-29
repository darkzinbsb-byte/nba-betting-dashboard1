import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="NBA Betting Dashboard", layout="wide")

st.title("🏀 NBA Betting Analytics Dashboard")

CSV_FILE = "backtest_log.csv"

# =========================
# VERIFICA SE CSV EXISTE
# =========================
if not os.path.exists(CSV_FILE):
    st.warning(
        "⚠️ Arquivo `backtest_log.csv` não encontrado.\n\n"
        "Isso é normal na primeira execução.\n\n"
        "➡️ Rode o bot (`send_alerts.py`) localmente para gerar o arquivo\n"
        "➡️ Depois faça upload do CSV para este repositório no GitHub."
    )
    st.stop()

# =========================
# CARREGAR DADOS
# =========================
df = pd.read_csv(
    CSV_FILE,
    names=["date", "game", "market", "pick", "line", "projection"]
)

if df.empty:
    st.warning("⚠️ O arquivo existe, mas ainda não possui dados.")
    st.stop()

df["date"] = pd.to_datetime(df["date"], errors="coerce")

# =========================
# MÉTRICAS GERAIS
# =========================
st.subheader("📌 Visão Geral")

col1, col2, col3 = st.columns(3)
col1.metric("Total de Apostas", len(df))
col2.metric("Mercados", df["market"].nunique())
col3.metric("Jogos", df["game"].nunique())

# =========================
# APOSTAS POR MERCADO
# =========================
st.subheader("📊 Apostas por Mercado")

market_count = df["market"].value_counts()

fig, ax = plt.subplots()
market_count.plot(kind="bar", ax=ax)
ax.set_ylabel("Quantidade")
st.pyplot(fig)

# =========================
# EVOLUÇÃO TEMPORAL
# =========================
st.subheader("📈 Apostas ao Longo do Tempo")

daily = df.groupby(df["date"].dt.date).size()

fig2, ax2 = plt.subplots()
daily.plot(ax=ax2)
ax2.set_ylabel("Quantidade")
st.pyplot(fig2)

# =========================
# FILTROS
# =========================
st.subheader("🔍 Filtro de Apostas")

market_filter = st.selectbox(
    "Filtrar por mercado:",
    ["Todos"] + list(df["market"].unique())
)

if market_filter != "Todos":
    df = df[df["market"] == market_filter]

st.dataframe(df.tail(30))
