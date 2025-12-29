import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="NBA Betting Dashboard", layout="wide")

st.title("🏀 NBA Betting Analytics Dashboard")

# =========================
# CARREGAR DADOS
# =========================
df = pd.read_csv(
    "backtest_log.csv",
    names=["date", "game", "market", "pick", "line", "projection"]
)

df["date"] = pd.to_datetime(df["date"])

# =========================
# MÉTRICAS GERAIS
# =========================
total_bets = len(df)
st.metric("Total de Apostas", total_bets)

# =========================
# APOSTAS POR MERCADO
# =========================
st.subheader("📊 Apostas por Mercado")
market_count = df["market"].value_counts()

fig, ax = plt.subplots()
market_count.plot(kind="bar", ax=ax)
st.pyplot(fig)

# =========================
# EVOLUÇÃO TEMPORAL
# =========================
st.subheader("📈 Apostas ao Longo do Tempo")
daily = df.groupby("date").size()

fig2, ax2 = plt.subplots()
daily.plot(ax=ax2)
st.pyplot(fig2)

# =========================
# FILTROS
# =========================
st.subheader("🔍 Filtro por Mercado")
selected_market = st.selectbox(
    "Escolha o mercado:",
    ["Todos"] + list(df["market"].unique())
)

if selected_market != "Todos":
    df = df[df["market"] == selected_market]

st.dataframe(df.tail(20))
