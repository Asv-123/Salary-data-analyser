import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data

def load_data():
    var = pd.read_csv('survey_results_public.csv')
    return var

df = load_data()
df = df[['DevType','ConvertedCompYearly']]

df = df.dropna(subset=['ConvertedCompYearly','DevType'])

df= df[df['ConvertedCompYearly']>1000]

average_sal = df.groupby('DevType')['ConvertedCompYearly'].mean().reset_index()

topsalary = average_sal.sort_values(by = 'ConvertedCompYearly',ascending= False)
topsalary = topsalary.head(5)

st.write('Top 5 Dev Roles based on salary')
st.write(topsalary)

plt.figure(figsize=(10,6))
plt.barh(topsalary['DevType'],topsalary['ConvertedCompYearly'], color = 'red',alpha = 0.5)
plt.xlabel('Average Salary $')
plt.title('Top 5 roles based on salary')
plt.gca().invert_yaxis()
plt.savefig('top5roles.png')
st.pyplot(plt)

if st.button('Download clean data'):
    cleaned_data = df.to_csv(index = False)
    st.download_button(
        label = 'Downlaod the clean data as a csv file',
        data = cleaned_data,
        file_name = 'Cleaned_data.csv',
        mime = 'text/csv'

    )

if st.button('Download graph'):

    st.download_button(
        label = 'Download the salary graph',
        data = open('top5roles.png','rb').read(),
        file_name= 'top5roles.png',
        mime = 'image/png'
    )