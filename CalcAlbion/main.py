import streamlit as st
from materials.raw_materials import SteelBar

st.set_page_config(page_title="Cálculo de Refinamento", layout="centered")

st.title("🔧 Cálculo de Custo de Refinamento")
st.markdown("Selecione as opções abaixo para ver todas as opções possíveis de refino para uma *Steel Bar*.")

# Inputs
item_type = st.selectbox("Tipo de Item", ["steel_bar"])
tier = st.selectbox("Tier", [2, 3, 4])
city = st.selectbox("Cidade", ["Martlock"])
enchantment = st.selectbox("Encantamento", [None, 1, 2, 3, 4], format_func=lambda x: "Sem Encantamento" if x is None else f"{x}")

if st.button("Calcular Custo"):
    steel_bar = SteelBar(tier, city, enchantment)
    current_price = steel_bar.price

    # Obter todas as opções de refino
    refine_paths = SteelBar.get_all_refine_paths(tier, city, enchantment)

    if refine_paths and current_price is not None:
        st.subheader(f"💡 Opções de Refino para Steel Bar T{tier}{f'@{enchantment}' if enchantment is not None else ''} em {city}:")
        for path in refine_paths:
            st.markdown(f"• **{path['descricao']}** → 💰 {path['custo_total']} prata")

        st.info(f"💱 Preço atual da **Steel Bar T{tier}{f'@{enchantment}' if enchantment is not None else ''}** em {city}: **{current_price} prata**")
    else:
        st.error("Não foi possível calcular as opções de custo. Verifique os dados ou tente novamente.")
