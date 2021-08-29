import streamlit as st 
import numpy as np
from PIL import Image

def show_score(score):
    
    st.markdown("**Prédiction : **") 
    if score < 0.5:
        st.text("Solvable")
    else:
        st.text("Non solvable")
    
    
    
def show_probabilite(score):
    st.markdown("**Score du client: **") 
    st.text(score)
    
    
def show_resultat_score(score):
    
    result_score = st.container()
    with result_score:
        col1, col2 = st.columns(2)
        cont1 = col1.container()
        with cont1:
            show_score(score)
        cont2 = col2.container()
        with cont2:        
            show_probabilite(score)
        
    result_features = st.container()
    with result_features:
        
        st.title("Features importance")
        img = Image.open("output.png") 
  
        st.image(img, width=700)