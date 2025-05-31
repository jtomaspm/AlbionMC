
import streamlit as st
from materials.raw_materials import SteelBar

st.set_page_config(page_title="Cálculo de Refinamento", layout="centered")

st.title("🔧 Cálculo de Custo de Refinamento")
st.markdown("Selecione as opções abaixo para ver o custo total de refinar uma *Steel Bar*.")

# Seleções (futuramente pode expandir com + opções)
item_type = st.selectbox("Tipo de Item", ["steel_bar"])
tier = st.selectbox("Tier", [2, 3, 4])
city = st.selectbox("Cidade", ["Martlock"])

if st.button("Calcular Custo"):
    sb = SteelBar()
    custo = sb.calc_refine_cost(tier, city)
    if custo is not None:
        st.success(f"Custo total para refinar **Steel Bar T{tier}** em **{city}**: 💰 {custo} prata")
    else:
        st.error("Não foi possível calcular o custo. Verifique os dados.")
