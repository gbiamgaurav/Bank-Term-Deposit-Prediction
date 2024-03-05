import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

# Load the model and preprocessor
model = joblib.load("final_model/model.joblib")
preprocessor = joblib.load("final_model/preprocessor.joblib")

def main():
    st.title('Term Deposit Subscription Prediction App')

    st.markdown("Please enter the customer details for Term deposit subscription prediction.")

    age = st.slider('Age', 18, 100, step=1, value=None)
    balance = st.slider('Balance', -10000, 150000, step=100, value=None)
    day = st.slider('Day of the month', 1, 31, step=1, value=None)
    duration = st.slider('Call duration (seconds)', 0, 5000, step=1, value=None)
    campaign = st.slider('Number of contacts performed during this campaign', 1, 100, step=1, value=None)
    pdays = st.slider('Number of days since the customer was last contacted', -1, 1000, step=1, value=None)
    previous = st.slider('Number of contacts performed before this campaign', 0, 300, step=1, value=None)

    job = st.selectbox('Job', ['blue-collar', 'management', 'technician', 'admin.', 'services', 
                               'retired', 'self-employed', 'entrepreneur', 'unemployed',
                                'housemaid', 'student', 'unknown'])

    marital = st.selectbox('Marital Status', ['divorced', 'married', 'single'])

    education = st.selectbox('Education', ['primary', 'secondary', 'tertiary', 'unknown'])

    default = st.radio('Has credit in default?', ['no', 'yes'])

    housing = st.radio('Has housing loan?', ['no', 'yes'])

    loan = st.radio('Has personal loan?', ['no', 'yes'])

    contact = st.selectbox('Contact communication type', ['telephone', 'unknown'])

    month = st.selectbox('Last contact month of the year', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])

    poutcome = st.selectbox('Outcome of the previous marketing campaign', ['failure', 'other', 'success', 'unknown'])

    with st.form("Term Deposit Prediction"):
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            if any(value is None for value in [age, balance, day, duration, campaign, pdays, previous]):
                st.warning("Please select values for all input parameters.")
            else:
                input_data = pd.DataFrame({
                    'age': [age],
                    'balance': [balance],
                    'day': [day],
                    'duration': [duration],
                    'campaign': [campaign],
                    'pdays': [pdays],
                    'previous': [previous],
                    'job': [job],
                    'marital': [marital],
                    'education': [education],
                    'default': [default],
                    'housing': [housing],
                    'loan': [loan],
                    'contact': [contact],
                    'month': [month],
                    'poutcome': [poutcome]
                })

                # Preprocess the input data
                X_transformed = preprocessor.transform(input_data)

                # Make the prediction
                prediction = model.predict(X_transformed)[0]

                result_text = "Customer will subscribe" if prediction == 0 else "Customer will not subscribe"
                st.write(f"Predicted Result: {result_text}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
