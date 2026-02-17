import streamlit as st

st.title("imc")

poids=st.number_input("veuillez donner votre poids")

taille =st.number_input("veuillez donner votre taille")
if st.button("calcul"):
    imc=poids/(taille**2)

    st.write(imc)

if imc<18.5:
    st.warning("maigre")
elif 18.5<imc > 25:
    
    st.success("poids normal")
elif 25<imc>30:
    st.warning("surpoids")
elif imc>30 :
    st.warning("obése")
else:
    st.info("La taille doit etre superieur à 0")
    
