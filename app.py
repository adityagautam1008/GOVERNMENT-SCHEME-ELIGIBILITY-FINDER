import streamlit as st
from rules import check_eligibility
from report import generate_report

st.set_page_config(page_title="Government Scheme Eligibility Finder",
                   page_icon="🇮🇳",
                   layout="wide")

st.markdown("""
<div style="background-color:#0b3d91;padding:15px;border-radius:10px">
<h1 style="color:white;text-align:center;">
राष्ट्रीय सरकारी योजना सलाह प्रणाली
</h1>
<p style="color:white;text-align:center;">
Citizen Welfare Advisory Portal
</p>
</div>
""", unsafe_allow_html=True)

st.header("अपनी जानकारी भरें")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("आपका नाम")
    age = st.number_input("आयु",1,120)
    income = st.number_input("वार्षिक आय (₹)",0)
    gender = st.selectbox("लिंग",["male","female","other"])
    caste = st.selectbox("जाति",["general","obc","sc","st"])
    state = st.selectbox("राज्य", [
        "All",
        "Himachal Pradesh",
        "Punjab",
        "Haryana",
        "Uttar Pradesh",
        "Delhi",
        "Rajasthan",
        "Madhya Pradesh",
        "Bihar",
        "Gujarat",
        "Maharashtra",
        "Tamil Nadu",
        "Karnataka",
        "Kerala",
        "West Bengal",
        "Uttarakhand",
        "Assam"
    ])

with col2:
    area = st.selectbox("क्षेत्र",["rural","urban"])
    marital_status = st.selectbox("वैवाहिक स्थिति",
                                   ["Single","Married","Widow"])
    has_house = st.selectbox("पक्का घर?",["हाँ","नहीं"])
    is_farmer = st.selectbox("किसान?",["हाँ","नहीं"])
    land = st.number_input("जमीन (हेक्टेयर)",0.0)
    is_student = st.selectbox("छात्र?",["हाँ","नहीं"])
    disability = st.selectbox("विकलांग?",["हाँ","नहीं"])

if st.button("🔍 पात्रता जांचें"):

    user_data = {
        "age": age,
        "income": income,
        "gender": gender,
        "caste": caste,
        "area": area,
        "marital_status": marital_status,
        "has_house": has_house=="हाँ",
        "is_farmer": is_farmer=="हाँ",
        "land": land,
        "is_student": is_student=="हाँ",
        "disability": disability=="हाँ"
    }

    results = check_eligibility(user_data, state)
    st.session_state["results"] = results
    st.session_state["name"] = name

if "results" in st.session_state:

    results = st.session_state["results"]

    st.subheader("आप इन योजनाओं के लिए पात्र हैं")

    if len(results)==0:
        st.error("कोई योजना नहीं मिली")
    else:
        for s in results:
            with st.container(border=True):
                st.markdown(f"### 🏛️ {s['name']}")
                st.write(f"**लाभ:** {s['benefit']}")
                st.link_button("👉 आवेदन करें", s["apply_link"])

if "results" in st.session_state and len(st.session_state["results"])>0:
    pdf = generate_report(st.session_state["name"],
                          st.session_state["results"])

    st.download_button("📄 रिपोर्ट डाउनलोड करें",
                       data=pdf,
                       file_name="yojana_report.pdf",
                       mime="application/pdf")

st.markdown("""
<hr>
<center>
Final Year Project By Aditya Gautam (17222990005), SHOURABH JAMWAL(17222990056) ,
RAUNAK RANA (17222990047) , 
SAKSHAM SAINI(17222990079)
</center>
""", unsafe_allow_html=True)
