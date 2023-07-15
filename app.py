from pathlib import Path

import streamlit as st

from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "Final_Resume.pdf"
profile_pic = current_dir / "Assets" / "profile_photo.png"

PAGE_TITLE = "Digital CV | Prakhar Kochhar"
PAGE_ICON = ":wave:"
NAME = "Prakhar Kochhar"
DESCRIPTION = """As an aspiring data analyst, I aim to leverage my analytical skills and expertise in interpreting complex datasets to uncover valuable insights that drive effective decision-making and contribute to organizational success.
"""
EMAIL = "prakharkochharknp@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/prakharkochhar/",
    "Instagram":"https://www.instagram.com/prakharkochhar_2511/",
    "GitHub": "https://github.com/kochharp",
    "HackerRank": "https://www.hackerrank.com/prakharkochhark1?hr_r=1"
}
PROJECTS = {
    "🏆 Movie Recommender System": "https://kochharp-movie-recommender-system-application-22mb2g.streamlit.app/",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon= PAGE_ICON)


# Load css, pdf & profile pic

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "📄 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime= "application/octet.stream",
    )
    st.write("📬", EMAIL)

# Social Links

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience and qualifications

st.write("#")
st.subheader("Qualifications")
st.write("""

- ✅ A descent understanding of how a financial analysis is carried out using Python and Statistics
- ✅ Strong hands on experience and knowledge in Python and Excel
- ✅ Good understanding of statistical principles and their respective applications
- ✅ A good hold on concepts of Six Sigma
""")

st.write("#")
st.subheader("Hard Skills")
st.write("""
- 🧑‍💻 Programming: Python (Scikit-learn, Pandas), SQL
- 📊 Data Visualization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 💾 Databases: Postgres, MangoDB, MySQL
- 🐝 Big data tools: Apache Spark, Apache Hadoop
- 🖥️ AWS tools: EMR clusters, EC2, S3

"""
)

# Work experience, as I have no work experience so let's leave this section empty


# Projects and accomplishments

st.write("#")
st.subheader("Projects and Accomplishments")
st.write("---")
for projects, link in PROJECTS.items():
    st.write(f"[{projects}]({link})")

st.write("""
🏆 Credit Exploratory Data Analysis

- » Objective: This case study aims to identify patterns which indicate if a client has
difficulty paying their instalments which may be used for taking actions such as denying
the loan, reducing the amount of loan, lending (to risky applicants) at a higher interest
rate, etc. This will ensure that the consumers capable of repaying the loan are not
rejected.

- » Solution: Performing Bivariate and Multivariate analysis and finding the top 10
correlations in the dataset.

- » Key Achievement: Found out factors that can help us in identifying clients with
payment difficulties.

🏆 Linear Regression(Machine Learning) Model

- » Objective: A US bike sharing provider wants to understand the factors on which the
demand for these shared bikes depends.
Solution: Designed Linear Regression models to predict how the demand vary
with different features moreover model helped us in understanding the demand
dynamics of new market.

- » Key Achievement: Developed a model with a R- Squared score of 83% on train set
and R-Squared score of 80% on the test set.
""")

st.write("#")
st.subheader("Education")
st.write("---")
st.write("""
Advance Certification Program in Data Science
          
- 🧑‍🎓 IIIT Bangalore & upGrad

Course Modules:
- 📖 Data Analysis using SQL | Introduction to Python | Introduction to Machine Learning
and Linear Regression

- 📖 Time Series Analysis | Telecom Churn Case Study | Lexical Processing | Syntactic
Processing

- 📖 Data Modelling| Introduction to Big Data and Cloud| Big Data Case Study
|Advanced SQL and Best Practices |Analytics using Spark

Bachelor of Business Administration
- 🧑‍🎓 CSJM University

""")


st.write("#")
st.subheader("Awards and Certifications")
st.write("---")

music = {
    "🎵 Music": "https://drive.google.com/file/d/1pETeQnmH3qNoT5XGBDOIfEC9SD3s8m1t/view?usp=sharing",
}
for mus, link in music.items():
    st.write(f"[{mus}]({link})")

st.write("""
- » I've been awarded a certificate with distinction grades in Hindustani Classical
Music(Singing) by Prayag Sangeet Samiti.

- » I've also managed to win a few competitions in piano solo genre of music.""")
sports = {
    "🏅 Sports": "https://drive.google.com/file/d/1Ar9lgbY3zOgNyIEtK9mOGnyPqjZ-o9gd/view?usp=sharing",
}
for sport, link in sports.items():
    st.write(f"[{sport}]({link})")

st.write("""
- » In year 2015, I bagged a silver medal in district level table tennis competition.

- » I also participated in quite a few state level table tennis cluster competitions.
""")
academics = {
    "🎓 Academics": "https://drive.google.com/file/d/1OchLKogI9npOlPZzNG0ATJt6pD_bP41H/view?usp=sharing",
}
for academic, link in academics.items():
    st.write(f"[{academic}]({link})")

st.write("""
- » I won few debate and group discussion competitions.

- » I took part in MUN conference few times.

- » I took part in quite a few public speaking competitions and managed to win few of them.""")
