sudo pip3 install scikit-learn
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model_path = 'best_titanic_model.pkl'
scaler_path = 'scaler.pkl'

with open(model_path, 'rb') as file:
    model = pickle.load(file)

with open(scaler_path, 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app
def main():
    st.title("Titanic Survival Prediction")
    st.write("### Enter passenger details to predict survival:")

    # Input fields for user data
    pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3], index=2)
    sex = st.selectbox("Sex", ["Male", "Female"], index=0)
    age = st.number_input("Age", min_value=0.0, max_value=100.0, value=30.0, step=1.0)
    sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", min_value=0, max_value=10, value=0, step=1)
    parch = st.number_input("Number of Parents/Children Aboard (Parch)", min_value=0, max_value=10, value=0, step=1)
    fare = st.number_input("Fare", min_value=0.0, max_value=600.0, value=32.0, step=1.0)
    embarked = st.selectbox("Port of Embarkation (Embarked)", ["C", "Q", "S"], index=2)

    # Preprocess inputs
    sex_encoded = 0 if sex == "Male" else 1
    embarked_encoded = {"C": 0, "Q": 1, "S": 2}[embarked]
    family_size = sibsp + parch + 1
    is_alone = 1 if family_size == 1 else 0

    # Combine features into a dataframe
    data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex_encoded],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked_encoded],
        "FamilySize": [family_size],
        "IsAlone": [is_alone]
    })

    # Scale numerical features
    numerical_features = ["Age", "Fare"]
    data[numerical_features] = scaler.transform(data[numerical_features])

    # Predict
    if st.button("Predict Survival"):
        prediction = model.predict(data)[0]
        prediction_proba = model.predict_proba(data)[0][1]

        if prediction == 1:
            st.success(f"The passenger is likely to survive with a probability of {prediction_proba:.2f}.")
        else:
            st.error(f"The passenger is unlikely to survive with a probability of {1 - prediction_proba:.2f}.")

if __name__ == "__main__":
    main()
