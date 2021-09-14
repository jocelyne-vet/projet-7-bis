import pickle
import pandas as pd
import numpy as np
import streamlit as st
import math
import sklearn
import plotly.express as px
import imblearn

######################################
# recupération des données 
######################################
@st.cache
def load_model():
    pickled_model, X_test= pickle.load(open("tuple_model_lr.pkl", 'rb'))
    return pickled_model, X_test
    


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
    if isinstance(data.at[int(idClient[0]), col], float):
        if math.isnan(data.at[int(idClient[0]), col]):
            return "inconnu(e)"
        else:
            return data.at[int(idClient[0]), col]
    else:
        return data.at[int(idClient[0]), col]




@st.cache
def load_prediction(data, id, clf):
        X=data
        #X = X.drop(["TARGET"], axis = 1)
        score = clf.predict_proba(X[X.index == int(id)])[:,1]
        return score


     
#@st.cache(allow_output_mutation=True)
def getHistogramme2(data, idClient, col,  mod, title):
    data_bis = data.copy()
    if not mod:
        val = data_bis.at[int(idClient[0]), col]

 
        fig = px.histogram(data_bis, x = col, title = title)
        
    else:
        col_a = col+"bis"
        data_bis[col_a] = np.abs(round((data_bis[col]/365), 2))
        val = data_bis.at[int(idClient[0]), col_a]

 
        fig = px.histogram(data_bis, x = col_a, title = title)
    
    fig.update_xaxes(title=dict(text=col))

    fig.add_vline(x = val, line_width=3, line_dash="dash", line_color="green")

 
    return fig
  

 
####################################################################################
def change_value(data, idClient):
    col = "AMT_CREDIT"
    value_credit = data.at[int(idClient), col] 
    my_range = np.arange(0,2*int(value_credit), value_credit/10)
    numberCredit = st.select_slider("AMT_CREDIT :", options = my_range, value = value_credit)
    st.write(numberCredit)
    col = "AMT_GOODS_PRICE"
    value_goods_price = data.at[int(idClient), col] 
    my_range_goods = np.arange(0,2*int(value_goods_price), value_goods_price/10)
    numberGoods = st.select_slider("AMT_GOODS_PRICE :", options = my_range_goods, value = value_goods_price)
    col = "AMT_INCOME_TOTAL"
    value_income = data.at[int(idClient), col] 
    my_range_income = np.arange(0,2*int(value_income), value_income/10)
    numberIncome = st.select_slider("AMT_INCOME_TOTAL :", options = my_range_income, value = value_income)
    col = "AMT_ANNUITY"
    value_annuity = data.at[int(idClient), col] 
    my_range_annuity = np.arange(0,2*int(value_annuity), value_annuity/10)
    numberAnnuity = st.select_slider("AMT_ANNUITY :", options = my_range_annuity, value = value_annuity)
    return numberCredit, numberGoods, numberIncome, numberAnnuity

@st.cache(allow_output_mutation=True)
def test_prediction(clf, data, idClient, numberCredit, numberGoods, numberIncome, numberAnnuity):        
    dfClient = get_data(data, idClient)
    dfClient = dfClient.copy()
    dfClient.at[0, "AMT_CREDIT"] = numberCredit

    dfClient.at[0, "AMT_GOODS_PRICE"] = numberGoods
    dfClient.at[0, "AMT_INCOME_TOTAL"] = numberIncome
    dfClient.at[0, "AMT_ANNUITY"] = numberAnnuity
    
    dfClient['NEW_CREDIT_TO_INCOME_RATIO'] = dfClient['AMT_CREDIT'] / dfClient['AMT_INCOME_TOTAL'] 

    dfClient['NEW_CREDIT_TO_GOODS_RATIO'] = dfClient['AMT_CREDIT'] / dfClient['AMT_GOODS_PRICE'] 
    dfClient['NEW_ANNUITY_TO_INCOME_RATIO'] = dfClient['AMT_ANNUITY'] / dfClient['AMT_INCOME_TOTAL'] 
    dfClient['NEW_ANNUITY_TO_CREDIT_RATIO'] = dfClient['AMT_ANNUITY'] / dfClient['AMT_CREDIT'] 
    dfClient['NEW_INCOME_TO_CREDIT_RATIO'] = dfClient['AMT_INCOME_TOTAL'] / dfClient['AMT_CREDIT'] 
    dfClient['NEW_INCOME_PER_PERSON'] = dfClient['AMT_INCOME_TOTAL'] / dfClient['CNT_FAM_MEMBERS']
    
    
    
    score = clf.predict_proba(dfClient[dfClient.index == 0])[:,1]
    return score