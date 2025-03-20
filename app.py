import streamlit as st
import random

st.title("Bienvenue sur Randomax !")
st.write("Génère un nombre aléatoire entre deux bornes définies.")

min_val=st.number_input("Valeur minimale",value=1, step=1)
max_val=st.number_input("Valeur maximale",value=10, step=1)
decimals=st.slider("Nombre de décimales", min_value=0, max_value=12, value=2)
listing=st.checkbox("Générer une liste de plusieurs nombres")
if listing:
    len_list=st.slider("Nombre d'éléments dans la liste", min_value=1, max_value=100, value=1)
button=st.button("Générer un nombre aléatoire")
def randomize():
    factor=10**decimals
    nombre=random.randint(int(min_val*factor),int(max_val*factor))/factor
    return nombre
if min_val<max_val:
    if button and listing:
        numbers=[]
        for i in range (len_list):
            numbers.append(randomize())
        nb_format=", ".join(f"{n:.{decimals}f}" for n in numbers)
        st.success(f"Liste générée : {nb_format}")
    elif button:
        st.success(f"Nombre généré : {randomize():.{decimals}f}")
else:
    st.error("La valeur minimale doit être inférieure à la valeur maximale.")