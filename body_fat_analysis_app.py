import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the data
data = pd.read_csv('C:\Users\sagar\OneDrive\Desktop\mahesh\AML body fat\bodyfat.csv')

# Add BMI column
Height_meter = (data['Height'] * 0.0254).round(2)
Weight_Kg = (data['Weight'] * 0.454).round(2)
BMI_score = (Weight_Kg/Height_meter**2).round()
data.insert(0,'BMI',BMI_score)

# Create a Streamlit app
st.title("Body Fat Analysis App")

# Sidebar
st.sidebar.header("Select a feature to analyze")
feature = st.sidebar.selectbox("Feature", data.columns)

# Main page
if feature == "BodyFat":
    st.header("Correlation between BodyFat and other features")
    corr = data.corr(method='pearson')
    corr = corr.BodyFat
    cr = corr.sort_values(ascending=False)[1:]
    fig, ax = plt.subplots()
    sns.barplot(x=cr, y=cr.index, ax=ax)
    ax.set_title("Correlation between BodyFat and other features")
    st.pyplot(fig)
elif feature == "BMI":
    st.header("Correlation between BMI and other features")
    corr = data.corr(method='pearson')
    corr = corr.BMI
    cr = corr.sort_values(ascending=False)[1:]
    fig, ax = plt.subplots()
    sns.barplot(x=cr, y=cr.index, ax=ax)
    ax.set_title("Correlation between BMI and other features")
    st.pyplot(fig)
else:
    st.header("Scatter plot of BMI vs. " + feature)
    fig = px.scatter(data, x="BMI", y=feature)
    st.plotly_chart(fig)

# Additional plots
st.header("Additional Plots")
st.write("Average BodyFat by Age")
avg_bodyfat_age = data.groupby('Age')['BodyFat'].mean().reset_index()
fig = px.line(avg_bodyfat_age, x='Age', y='BodyFat')
st.plotly_chart(fig)

st.write("Average BMI by Age")
avg_BMI_age = data.groupby('Age')['BMI'].mean().reset_index()
fig = px.line(avg_BMI_age, x='Age', y='BMI')
st.plotly_chart(fig)

st.write("Average BMI by BodyFat")
avg_BodyFat_age = data.groupby('BodyFat')['BMI'].mean().reset_index()
fig = px.line(avg_BodyFat_age, x='BodyFat', y='BMI')
st.plotly_chart(fig)

st.write("BMI Score Distribution")
fig, ax = plt.subplots()
plt.hist(data['BMI'])
plt.xticks(np.arange(15,35,1))
plt.title('BMI Score')
plt.xlabel('BMI')
plt.axvline(x=18.5, color='orange', lw=4)
plt.text(16,20, 'Underweight')
plt.text(16,17, 'BMI<18.5')
plt.axvline(x=22, color='blue', lw=2)
plt.text(20,40, 'Healthy')
plt.text(20,37, '18.5<BMI<24.5')
plt.axvline(x=27, color='red', lw=4)
plt.text(24.5,62, 'Overweight')
plt.text(24.5,58, '24.5<BMI<29.5')
plt.axvline(x=31, color='red', lw=6)
plt.text(29.5,40, 'Obesity')
plt.text(29.5,37, 'BMI>29.5')
st.pyplot(fig)