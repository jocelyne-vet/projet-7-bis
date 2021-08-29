import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import streamlit as st

######################################
# recupération des données 
######################################
@st.cache
def load_model():
    pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_Xtest, pickled_Ytest = pickle.load(open("tuple_model_lr.pkl", 'rb'))
    return pickled_model, pickled_Xtrain, pickled_Ytrain, pickled_Xtest, pickled_Ytest

@st.cache
def load_data(filename):
    data = pd.read_csv(filename)
    return data
    
    
#############################################
# remplissage de st_selectbox
#############################################
@st.cache
def list_idClient(data):
    return data.index.values
    
    
##########################################
# informations sur le client
##########################################
@st.cache
def get_data(data, idClient):
    return data[data.index == int(idClient)]
     

@st.cache    
def getInformationsClient(data, idClient,col):  
    return data.at[int(idClient[0]), col]
    
@st.cache
def getNomCol(nom):
    dict_name = {"Age":"DAYS_BIRTH", "Etat civil": "NAME_FAMILY_STATUS", "Situation du logement": "NAME_HOUSING_TYPE", "Catégorie socio-professionnel": "NAME_INCOME_TYPE",
                 "Nb enfants": "CNT_FAM_MEMBERS", "Revenu": "AMT_INCOME_TOTAL", "Profession": "OCCUPATION_TYPE", "ANCIENNETE": "DAYS_EMPLOYED"}




@st.cache
def load_prediction(data, id, clf):
        X=data
        # X = X.drop(["TARGET"], axis = 1)
        score = clf.predict_proba(X[X.index == int(id)])[:,1]
        return score

#@st.cache(allow_output_mutation=True)
def getHistogramme(data, idClient, col,  mod, title):
    fig = plt.figure()
     
    fig, ax = plt.subplots()
    data_bis = data.copy()
    if not mod:
        val = data_bis.at[int(idClient[0]), col]

        data_bis[[col]].plot(kind = "hist", ax = ax)
    else:
        col_a = col+"bis"
        data_bis[col_a] = np.abs(round((data_bis[col]/365), 2))
        val = data_bis.at[int(idClient[0]), col_a]
        print("test")

        data_bis[[col_a]].plot(kind = "hist", ax = ax)
        
    plt.axvline(x=val, color = "red")
    plt.title(title)
 
    return fig
     



############################################
# Informations relatives au score
############################################
# get_predict_solvabilité_client (oui,non)

# get probabilité_solvabilité_client

# plot diagramme importance variables

# plot observation pour le client 


##############################################
# information relatives au client
#############################################

#  getInformations (etat civil, profession, situation, logement)

# plottHistogramme (age, nb d'enfants, revenu, ancienneté) 


