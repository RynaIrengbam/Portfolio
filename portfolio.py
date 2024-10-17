import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components
from streamlit_timeline import st_timeline
import json

st.set_page_config('Ryna\'s Portfolio', layout='wide')
st.header("Summary")
st.write("An aspiring Data Scientist pursuing an MA in Statistics at Columbia University. An M.Sc in Mathematics with a strong academic record and a passion for leveraging analytical skills to drive data-driven insights. Experienced in due diligence, and portfolio management. Skilled in developing robust web applications, creating analytical dashboards, and conducting exploratory data analysis. Adept at collaborating with cross-functional teams to deliver innovative solutions. I possess skills in software such as MS Office, Advanced Excel, Tableau, PowerBI, MS SQL and programming languages like Python.")

linkedin_url = 'https://www.linkedin.com/in/ryna-irengbam-6ba24118b/?embed=true'
with st.sidebar:
    embed_component={'linkedin':'''
    <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
    <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ryna-irengbam-6ba24118b" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/ryna-irengbam-6ba24118b?trk=profile-badge">Ryna Irengbam</a></div>
    '''}
    components.html(embed_component['linkedin'],height=310)
st.sidebar.caption("Wish to connect")
st.sidebar.write("📧: ri2298@columbia.edu")
pdfFileObj = open('Resume_Ryna Irengbam.pdf','rb')
st.sidebar.download_button('Download Resume',pdfFileObj,file_name='RynaIrengbam_Resume.pdf',mime='pdf')

st.header("Education")
df = {'Education':['MA Statistics','M.Sc Mathematics','B.Sc Mathematics'],'University':['Columbia University','University of Delhi','University of Delhi'],'Year':['2024-2025','2020-2022','2017-2020'],'CGPA':['','4.0','4.0']}
st.table(df)

with open('timeline.json', "r") as f: 
       data = json.load(f)        
st_timeline(data, height=500)

st.header("Skills")
columns = st.columns(6)
columns[0].button("MS Office")
columns[1].button("Advanced Excel(VBA)")
columns[2].button("Tableau")
columns[3].button("Power BI")
columns[4].button("MS SQL")
columns[5].button("Python")

st.header("Projects")

st.subheader("Udemy Course Data Analysis")
st.write("The analysis aims to track the performance of Udemy courses and identify opportunities to increase revenue . The following analysis also aims to answer whether there will be an effect on the popularity of a course if there is an increase in the course charge . The data provided by Udemy divides the courses into different subjects including Business Finance, Web Development, Musical Instruments and Graphic Design. For each course, data on published timestamp, price, level, number of subscribers, number of reviews, rating and content duration has been provided.")
url1 = 'https://public.tableau.com/app/profile/ryna6151/viz/UdemyCourseAnalysis_16274987683140/Dashboard1'
st.markdown(f'''
<a href={url1}><button style="background-color:LightRed;">Tableau Dashboard Link</button></a>
''',
unsafe_allow_html=True)

st.subheader("Cryptocurrency Market Analysis")
st.write("With cryptocurrency being touted as the next big thing, a lot of people are considering investing in the same. The project aims to identify the most popular cryptocurrencies and examine the cryptocurrency market trends. The analysis seeks to help investors understand the functioning of the cryptocurrency market which in turn will help them make better decisions.")
url2 = 'https://public.tableau.com/app/profile/ryna6151/viz/CryptocurrencyMarketAnalysis/Story1'
st.markdown(f'''
<a href={url2}><button style="background-color:LightRed;">Tableau Dashboard Link</button></a>
''',
unsafe_allow_html=True)

st.subheader("Student Dropout Web App")
st.write("The business problem addressed by the student dropout web application is the identification of at-risk students in educational institutions. By analyzing various data points and utilizing machine learning algorithms, the application helps identify students who are more likely to drop out, allowing timely intervention strategies to be implemented and improving student retention rates.")
url3 = 'https://student-dropout-app.streamlit.app/'
st.markdown(f'''
<a href={url3}><button style="background-color:LightRed;">Streamlit App Link</button></a>
''',
unsafe_allow_html=True)
