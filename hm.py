import streamlit as st
import pandas as pd
import numpy as np
import datetime

# Set page configuration
st.set_page_config(page_title="Hospital Management System", page_icon=":hospital:", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Patient Records", "Doctor Assignment", "Appointments", "Billing"])

# Sample data for patients and doctors
patients_data = {
    'Patient ID': [1, 2, 3],
    'Name': ['John Doe', 'Jane Smith', 'Alice Johnson'],
    'Age': [25, 34, 29],
    'Gender': ['Male', 'Female', 'Female'],
    'Disease': ['Flu', 'Diabetes', 'Asthma'],
    'Admitted': [True, False, True]
}

doctors_data = {
    'Doctor ID': [101, 102, 103],
    'Name': ['Dr. Adams', 'Dr. Baker', 'Dr. Clark'],
    'Specialization': ['General Medicine', 'Endocrinology', 'Pulmonology']
}

# Convert to DataFrames
patients_df = pd.DataFrame(patients_data)
doctors_df = pd.DataFrame(doctors_data)

# Home Page
if page == "Home":
    st.title("Welcome to the Hospital Management System")
    st.write("Use the sidebar to navigate through different sections.")
    st.image("https://placekitten.com/800/400", use_column_width=True)

# Patient Records Page
elif page == "Patient Records":
    st.title("Patient Records")
    st.write("This section displays the records of all patients.")

    st.subheader("Current Patient List")
    st.dataframe(patients_df)

    st.subheader("Add New Patient")
    new_patient_id = st.number_input("Patient ID", min_value=1, step=1)
    new_name = st.text_input("Name")
    new_age = st.number_input("Age", min_value=0, step=1)
    new_gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    new_disease = st.text_input("Disease")
    new_admitted = st.checkbox("Admitted", value=False)

    if st.button("Add Patient"):
        new_patient_data = pd.DataFrame({
            'Patient ID': [new_patient_id],
            'Name': [new_name],
            'Age': [new_age],
            'Gender': [new_gender],
            'Disease': [new_disease],
            'Admitted': [new_admitted]
        })

        patients_df = pd.concat([patients_df, new_patient_data], ignore_index=True)
        st.success("Patient added successfully!")
        st.dataframe(patients_df)

# Doctor Assignment Page
elif page == "Doctor Assignment":
    st.title("Doctor Assignment")
    st.write("Assign doctors to patients.")

    st.subheader("Doctor List")
    st.dataframe(doctors_df)

    st.subheader("Assign Doctor")
    patient_id = st.number_input("Patient ID", min_value=1, step=1)
    doctor_id = st.selectbox("Doctor", doctors_df['Doctor ID'])

    if st.button("Assign Doctor"):
        patient_name = patients_df[patients_df['Patient ID'] == patient_id]['Name'].values[0]
        doctor_name = doctors_df[doctors_df['Doctor ID'] == doctor_id]['Name'].values[0]
        st.success(f"Doctor {doctor_name} assigned to Patient {patient_name}.")

# Appointments Page
elif page == "Appointments":
    st.title("Appointments")
    st.write("Schedule and view patient appointments.")

    st.subheader("Schedule Appointment")
    appointment_patient_id = st.number_input("Patient ID", min_value=1, step=1)
    appointment_doctor_id = st.selectbox("Doctor", doctors_df['Doctor ID'])
    appointment_date = st.date_input("Appointment Date", datetime.date.today())
    appointment_time = st.time_input("Appointment Time")

    if st.button("Schedule Appointment"):
        st.success(f"Appointment scheduled for Patient ID {appointment_patient_id} with Doctor ID {appointment_doctor_id} on {appointment_date} at {appointment_time}.")

    st.subheader("View Appointments")
    st.write("This feature can be implemented to show upcoming and past appointments.")

# Billing Page
elif page == "Billing":
    st.title("Billing")
    st.write("Generate and view billing details.")

    st.subheader("Generate Bill")
    bill_patient_id = st.number_input("Patient ID for Billing", min_value=1, step=1)
    treatment_cost = st.number_input("Treatment Cost", min_value=0, step=100)
    room_charges = st.number_input("Room Charges", min_value=0, step=100)
    medication_cost = st.number_input("Medication Cost", min_value=0, step=100)

    if st.button("Generate Bill"):
        total_cost = treatment_cost + room_charges + medication_cost
        st.success(f"Bill generated for Patient ID {bill_patient_id}. Total Cost: ${total_cost}")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Hospital Management System | Powered by Streamlit")
