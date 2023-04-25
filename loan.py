import pandas as pd
import numpy as np
import pickle
import streamlit as st

regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

def predict_houe_price(data):
    
    input_data_arry=np.array(data)
    input_data_reshape=input_data_arry.reshape(1,-1)
    new_data=scalar.transform(input_data_reshape)
    prediction=regmodel.predict(new_data)
    print(prediction)
    return prediction
    
    

def main():
    st.title('House Price Prediction')
    crim=st.text_input("Crime rate","Type Here")
    zn=st.text_input("ZN","Type Here")
    indus=st.text_input("Indus","Type Here")
    chas=st.text_input("CHAS","Type Here")
    nox=st.text_input("NOX","Type Here")
    rm=st.text_input("RM","Type Here")
    age=st.text_input("AGE","Type Here")
    dis=st.text_input("DIS","Type Here")
    rad=st.text_input("RAD","Type Here")
    tax=st.text_input("TAX","Type Here")
    ptratio=st.text_input("PTRATIO","Type Here")
    b=st.text_input("B","Type Here")
    lstat=st.text_input("LSTAT","Type Here")
    result=""
    if st.button("Prediction"):
        result=predict_houe_price([crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat])
    st.success('The output is {}'.format(result))
    if st.button('About'):
        st.text("lets Learn")
        st.text('BUilt with Streamlit')
        
if __name__=='__main__':
    main()