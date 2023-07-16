import streamlit as st
import pandas as pd
from PIL import Image
import streamlit.components.v1 as components

st.set_page_config('Ryna\'s Portfolio', layout='wide')
st.header("Summary")
st.write(" I am a highly accomplished and detail-oriented professional with a strong academic background in Mathematics. I completed my M.Sc in Mathematics from Kirori Mal College, University of Delhi and my B.Sc (Hons) in Mathematics from Jesus and Mary College, University of Delhi. Currently, I am working as a Management Trainee at Genpact, where I have contributed to creating asset summary reports and conducted due diligence for high-value loans. I also have experience as a Data Analyst Intern at ResoluteAI.in, where I developed a student dropout web app and designed analytical dashboards. Additionally, I have a financial modeling internship experience at Vardhan Consulting Engineers. I possess skills in software such as MS Office, Advanced Excel, Tableau, PowerBI, MS SQL and programming languages like Python.")

with st.sidebar:
    embed_component={'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="ryna-irengbam-6ba24118b" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/ryna-irengbam-6ba24118b?trk=profile-badge">Ryna Irengbam</a></div>
              """}
    components.html(embed_component['linkedin'],height=310)
st.sidebar.caption("Wish to connect")
st.sidebar.write("📧: rynairengbam@gmail.com")
pdfFileObj = open('Ryna I CV.pdf','rb')
st.sidebar.download_button('Download Resume',pdfFileObj,file_name='Ryna I CV.pdf',mime='pdf')

st.header("Education")
df = {'Education':['B.Sc Mathematics','M.Sc Mathematics'],'University':['Kirori Mal College, Delhi University','Jesus and Mary College, Delhi University'],'Year':['2020-2022','2017-2020'],'CGPA':['9.048','9.432']}
st.table(df)

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
