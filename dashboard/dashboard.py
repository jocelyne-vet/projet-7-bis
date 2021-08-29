import streamlit as st 
import score
import app
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#################################################

clf, X_train, y_train, X_test, y_test = app.load_model()
data = X_train
#data = app.load_data() 

################################################


sel_col, display_col = st.columns(2)

add_selectbox = st.sidebar.container()

with add_selectbox:
    idClient = st.multiselect("Id du client: ", 
                         app.list_idClient(data)) 
    #st.text("Il y a 3 Clients dans la base")

    visualisation = st.radio("Informations: ", ('Informations relatives au score', 'Informations relatives au client', 'Comparaison des informations du client avec des clients similaires' )) 

resultats = st.container()





with resultats :
    if (visualisation == 'Informations relatives au score'):

        st.title("Informations relatives au score")
      
        
        if  len(idClient):
            score_res = app.load_prediction(data, idClient[0], clf)     
            score.show_resultat_score(score_res[0])
    elif (visualisation == 'Informations relatives au client'):
        if  len(idClient):
            st.title("Informations relatives au clients")
            
            st.write("**Sexe : **", app.getInformationsClient(data, idClient,"CODE_GENDER"))
            st.write("**Age : **{:.0f} ans".format(np.abs(int(app.getInformationsClient(data, idClient,"DAYS_BIRTH")/365))))
            st.write("**Statut familial : **", app.getInformationsClient(data, idClient,"NAME_FAMILY_STATUS"))
            st.write("**Nombre d'enfants : **{:.0f}".format(app.getInformationsClient(data, idClient,"CNT_CHILDREN")))
            st.write("**La catégorie socio professionnelle : **", app.getInformationsClient(data, idClient,"NAME_INCOME_TYPE"))
            st.write("**La profession : **", app.getInformationsClient(data, idClient,"OCCUPATION_TYPE"))
            st.write("**Le revenu : **", app.getInformationsClient(data, idClient,"AMT_INCOME_TOTAL"))
        
        
            st.pyplot(app.getHistogramme(data, idClient, "DAYS_BIRTH", True, "Distribution: âge des clients"))
            st.pyplot(app.getHistogramme(data, idClient, "DAYS_EMPLOYED",  True, "Distribution: ancienneté des cliets"))
            st.pyplot(app.getHistogramme(data, idClient, "AMT_INCOME_TOTAL",  False, "Distribution: revenu des clients"))
            st.pyplot(app.getHistogramme(data, idClient, "AMT_CREDIT",  False, "Distribution: annuité du crédit"))
    else:
        st.title("Comparaison")


