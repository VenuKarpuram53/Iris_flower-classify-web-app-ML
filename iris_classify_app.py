# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:24:26 2020

@author: Venu Karpuram
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 11:24:04 2020

@authors: Thanvika, Venu, Yoshitha.
"""
import streamlit as st
import pickle




neuron_model=pickle.load(open('neuron_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))
svc_model=pickle.load(open('svc_model.pkl','rb'))
decision_model=pickle.load(open('decision_model.pkl','rb'))


def classify(num):
    if num<0.5:
        return 'Setosa'
    elif num <1.5:
        return 'Versicolor'
    else:
        return 'Virginica'
def main():
    st.title("Major Project")
    html_temp = """
    <div style="background-color:red ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>

    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Neural Network','Logistic Regression','SVM','Decision Tree']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)
    sl=st.slider('Select Sepal Length', 0.0, 10.0)
    sw=st.slider('Select Sepal Width', 0.0, 10.0)
    pl=st.slider('Select Petal Length', 0.0, 10.0)
    pw=st.slider('Select Petal Width', 0.0, 10.0)
    inputs=[[sl,sw,pl,pw]]
    if st.button('Classify'):
        if option=='Neural Network':
            st.success(classify(neuron_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))
        elif option=='Decision Tree':
            st.success(classify(decision_model.predict(inputs)))
        else:
           st.success(classify(svm.predict(inputs)))


if __name__=='__main__':
    main()

