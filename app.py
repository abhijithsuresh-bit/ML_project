import streamlit as st
import pandas as pd
from training import predict_patient,X_train,model
# ---- Your predict function (assuming you already have it) ----
# def predict_patient(model, raw_data, feature_columns):
#     ...
#     return prediction

def main():
    st.set_page_config(page_title="Mental Illness Prediction", page_icon="🧠", layout="centered")
    st.title("🧠 Mental Illness Prediction")
    st.write("Fill out the patient information below to predict the likelihood of mental illness.")

    # Sidebar for inputs
    st.sidebar.header("Patient Information")

    program_category = st.sidebar.selectbox("Program Category", ["EMERGENCY" ,"INPATIENT","OUTPATIENT","RESIDENTIAL","SUPPORT"])
    region = st.sidebar.selectbox("Region Served", ["CENTRAL NY REGION" ,"HUDSON RIVER REGION" ,"LONG ISLAND REGION","NEW YORK CITY REGION","WESTERN REGION"])
    age_group = st.sidebar.selectbox("Age Group", ["CHILD","ADULT","UNKNOWN"])
    sex = st.sidebar.selectbox("Sex", ["MALE", "FEMALE","UNKNOWN"])
    transgender = st.sidebar.selectbox("Transgender", ["CLIENT DIDN'T ANSWER","NO, NOT TRANSGENDER", "UNKNOWN","YES TRANSGENDER"])
    sexual_orientation = st.sidebar.selectbox(
        "Sexual Orientation",
        ["STRAIGHT OR HETEROSEXUAL", "GAY OR LESBIAN", "BISEXUAL", "OTHER","UNKNOWN","CLIENT DIDN'T ANSWER"]
    )
    ethnicity = st.sidebar.selectbox(
        "Hispanic Ethnicity", ["YES, HISPANIC/LATINO", "NO, NOT HISPANIC/LATINO","UNKNOWN"]
    )
    race = st.sidebar.selectbox(
        "Race", ["WHITE ONLY","BLACK ONLY","MULTI-RACIAL","OTHER","UNKNOWN RACE"]
    )
    living = st.sidebar.selectbox(
        "Living Situation",
        ["PRIVATE RESIDENCE", "OTHER LIVING SITUATION", "INSTITUTIONAL SETTING", "UNKOWN"]
    )
    language = st.sidebar.selectbox("Preferred Language", ["ENGLISH", "SPANISH", " ALL OTHER LANGUAGES","ASIAN AND PACIFIC ISLAND","INDO-EUROPEAN","AFRO-ASIATIC","UNKOWN"])
    employment = st.sidebar.selectbox(
        "Employment Status",
        ["EMPLOYED","NON-PAID/VOLUNTEER","NOT IN LABOUR FORCE: UNEMPLOYED","UNEMPLOYED , LOOKING FOR WORK","UNKNOWN EMPLOYMENT STATUS"]
    )
    education = st.sidebar.selectbox(
        "Education Status",
        ["COLLEGE OR GRADUATE DEGREE","MIDDLE SCHOOL TO HIGH SCHOOL","NO FORMAL EDUCATION","OTHER","PRE-K TO FIFTH GRADE","SOME COLLEGE","UNKNOWN"]
    )
    diabetes = st.sidebar.selectbox("Diabetes", ["YES", "NO","UNKNOWN"])
    bp = st.sidebar.selectbox("High Blood Pressure", ["YES", "NO","UNKOWN"])

    # Build input dictionary
    new_raw = {
        'Program Category': program_category,
        'Region Served': region,
        'Age Group': age_group,
        'Sex': sex,
        'Transgender': transgender,
        'Sexual Orientation': sexual_orientation,
        'Hispanic Ethnicity': ethnicity,
        'Race': race,
        'Living Situation': living,
        'Preferred Language': language,
        'Employment Status': employment,
        'Education Status': education,
        'Diabetes': diabetes,
        'High Blood Pressure': bp
    }

    # Prediction button
    if st.sidebar.button("Predict"):
        prediction = predict_patient(model, new_raw, X_train.columns)

        st.success(f"Prediction (Mental Illness): {prediction}")

if __name__ == "__main__":
    main()
