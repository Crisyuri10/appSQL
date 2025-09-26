import streamlit as st
import pyodbc

# ---------------- Conexão com o Banco ----------------
# Usa st.cache_resource para inicializar apenas uma vez
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=" + st.secrets["server"] + ";"
        "DATABASE=" + st.secrets["database"] + ";"
        "Trusted_Connection=yes;"
    )

conn = init_connection()

# ---------------- Função para executar Query ----------------
# Usa st.cache_data para evitar recarregar sempre
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# ---------------- Exemplo de Uso ----------------
rows = run_query("SELECT * FROM mytable;")

# Exibe os resultados
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
