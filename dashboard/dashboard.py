#import score
import app

import streamlit as st 
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


#################################################

clf, X_test = app.load_model()
data = X_test
#data = app.load_data("X_sample.csv") 
################################################
def show_score(score):
    
    st.markdown("**Prédiction : **") 
    if score < 0.5:
        st.text("Solvable")
    else:
        st.text("Non solvable")
    
    
    
def show_probabilite(score):
    st.markdown("**Score du client: **") 
    st.text(score)




##############################################

sel_col, display_col = st.columns(2)

add_selectbox = st.sidebar.container()

with add_selectbox:
    idClient = st.multiselect("Id du client: ", 
                         app.list_idClient(data)) 
    #st.text("Il y a 3 Clients dans la base")

    visualisation = st.radio("Informations: ", ('Informations relatives au score', 'Informations relatives au client' )) 

resultats = st.container()





with resultats :
    if (visualisation == 'Informations relatives au score'):

        st.title("Informations relatives au score")
      
        
        if  len(idClient):
            score_res = app.load_prediction(data, idClient[0], clf)     
            # score.show_resultat_score(score_res[0])
            
            result_score = st.container()
            with result_score:
                col1, col2 = st.columns(2)
                cont1 = col1.container()
                with cont1:
                    show_score(score_res[0])
                    cont2 = col2.container()
                with cont2:        
                    show_probabilite(score_res[0])
        
            result_features = st.container()
            with result_features:
        
                st.title("Features importance")
                img = Image.open("features_imp.png") 
  
                st.image(img, width=700)
            
            
           
            
            
    elif (visualisation == 'Informations relatives au client'):
        if  len(idClient):
            st.title("Informations relatives au client")
            
            st.write("**Sexe : **", app.getInformationsClient(data, idClient,"CODE_GENDER"))
            st.write("**Age : **{:.0f} ans".format(np.abs(int(app.getInformationsClient(data, idClient,"DAYS_BIRTH")/365))))
            st.write("**Statut familial : **", app.getInformationsClient(data, idClient,"NAME_FAMILY_STATUS"))
            st.write("**Nombre d'enfants : **{:.0f}".format(app.getInformationsClient(data, idClient,"CNT_CHILDREN")))
            st.write("**La catégorie socio professionnelle : **", app.getInformationsClient(data, idClient,"NAME_INCOME_TYPE"))
            st.write("**La profession : **", app.getInformationsClient(data, idClient,"OCCUPATION_TYPE"))
            st.write("**Le revenu : **", app.getInformationsClient(data, idClient,"AMT_INCOME_TOTAL"))
        
        
            st.pyplot(app.getHistogramme(data, idClient, "DAYS_BIRTH", True, "Distribution: âge des clients"))
            st.pyplot(app.getHistogramme(data, idClient, "DAYS_EMPLOYED",  True, "Distribution: ancienneté des clients"))
            st.pyplot(app.getHistogramme(data, idClient, "AMT_INCOME_TOTAL",  False, "Distribution: revenu des clients"))
            st.pyplot(app.getHistogramme(data, idClient, "AMT_CREDIT",  False, "Distribution: annuité du crédit"))
    else:
        st.title("Comparaison")


