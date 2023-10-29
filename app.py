import streamlit as st
import catboost
import numpy as np
import pandas as pd
import joblib

# Load the preprocessor and trained model
# The preprocessor is assumed to be a transformer object with a 'transform' method
# The trained model is loaded from a .cbm file, which is CatBoost’s binary format
preprocessor = joblib.load('preprocessor.pkl')
cat_model = catboost.CatBoost()
cat_model.load_model('CatBoost_model.cbm')

def predict(data):
    """
    Make a salary prediction based on the input data.
    
    :param data: DataFrame, contains input features for prediction
    :return: np.ndarray, the predicted salary
    """
    # Transform the data using the preprocessor
    processed_data = preprocessor.transform(data)
    # Make a prediction using the trained CatBoost model
    return cat_model.predict(processed_data)

# Setting up the Streamlit interface
st.title("Predicting Salaries: Leveraging the 2023 Stack Overflow Developer Survey Data")
st.warning("Disclaimer: This is a machine learning project and the model used for salary prediction has inherent inaccuracies and uncertainties. Please take the predictions with caution and do not consider them as definitive or precise salary recommendations.")


# Dropdown options
age_options = sorted(['18-24 years old', '25-34 years old', '35-44 years old', '45-54 years old', '55-64 years old', '65 years or older'])
remote_work_options = ['Hybrid (some remote, some in-person)', 'In-person', 'Remote']
ed_level_options = ['Bachelor’s degree', 'Less than a Bachelors', 'Master’s degree', 'Post grad']
org_size_options = ['Freelancer', 'Small Business', 'Medium Business', 'Large Business']
country_options = sorted(['Argentina', 'Australia', 'Austria', 'Belgium', 'Brazil', 'Bulgaria', 'Canada', 'Colombia', 'Czech Republic', 'Denmark', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Lithuania', 'Mexico', 'Netherlands', 'New Zealand', 'Norway', 'Poland', 'Portugal', 'Romania', 'Russian Federation', 'Serbia', 'Slovakia', 'Slovenia', 'South Africa', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom of Great Britain and Northern Ireland', 'United States of America', 'other'])
dev_type_options = ['Academic researcher', 'Blockchain', 'Cloud infrastructure engineer', 'Data or business analyst', 'Data scientist or machine learning specialist', 'Database administrator', 'Developer Experience', 'Developer, QA or test', 'Developer, back-end', 'Developer, desktop or enterprise applications', 'Developer, embedded applications or devices', 'Developer, front-end', 'Developer, full-stack', 'Developer, game or graphics', 'Developer, mobile', 'DevOps specialist', 'Educator', 'Engineer, data', 'Engineer, site reliability', 'Engineering manager', 'Hardware Engineer', 'Product manager', 'Project manager', 'Research & Development role', 'Scientist', 'Security professional', 'Senior Executive (C-Suite, VP, etc.)', 'System administrator', 'other']
years_code_pro_options = sorted(['less than one year', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, "35 or over 35"], key=lambda x: (isinstance(x, str), x))

# Streamlit widgets to take user input
age = st.selectbox("Age", age_options)
remote_work = st.selectbox("Remote Work", remote_work_options)
ed_level = st.selectbox("Education Level", ed_level_options)
years_code_pro = st.selectbox("Years of Professional Coding Experience", years_code_pro_options)

# Converting years of professional coding experience to numerical value
if years_code_pro == 'less than one year':
    years_code_pro_value = 0.5
elif years_code_pro == '35 or over 35':
    years_code_pro_value = 35
else:
    years_code_pro_value = years_code_pro

dev_type = st.selectbox("Developer Type", dev_type_options)
org_size = st.selectbox("Organization Size", org_size_options)
country = st.selectbox("Country", country_options)

# Checkboxes for employment status
employed = st.checkbox("Employed")
freelancer = st.checkbox("Freelancer")

# Creating a DataFrame to hold the input data
data = pd.DataFrame({
    "Age": [age],
    "RemoteWork": [remote_work],
    "EdLevel": [ed_level],
    "YearsCodePro": [years_code_pro_value],
    "DevType": [dev_type],
    "OrgSize": [org_size],
    "Country": [country],
    "Employed": [employed],
    "freelancer": [freelancer]
})

# Button to trigger prediction
pred = st.button("Predict Salary")
if pred:
    # Making prediction using the input data
    prediction = predict(data)
    # Formatting and displaying the prediction result
    formatted_prediction = "{:,.0f}".format(prediction[0])
    st.write(formatted_prediction)
