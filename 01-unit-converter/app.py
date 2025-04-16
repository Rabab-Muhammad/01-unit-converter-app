# import streamlit as st

# st.title("Unit Converter App")

# st.markdown("### Converts Lenght , Weight and Time instantly")
# st.write("Welcome ! Select , Category")

# category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])
# def convert_unit(category, value, unit):
#     if category == "Length":
#         if unit == "Kilometers to Miles":
#             return value * 0.621371
#         elif unit == "Miles to Kilometers":
#             return value / 0.621371
        
#     elif category == "Weight":
#         if unit == "Kilegrams to pounds":
#             return value * 2.04623
#         elif unit == "Pounds to Kilegrams":
#             return value / 2.04623
    
#     elif category == "Time":
#         if unit == "Seconds to Minutes":
#             return value / 60
#         elif unit == "Minutes to Seconds":
#             return value * 60
#         elif unit == "Minutes to Hours":
#             return value / 60
#         elif unit == "Hours to Minutes":
#             return value * 60
#         elif unit == "Hours to Days":
#             return value / 24
#         elif unit == "Days to Hours":
#             return value * 24
#         if category == "Length":
#             unit = st.selectbox("Select Conversation", ["Kilemeters to Miles","Miles to kilometers",])
#         elif category == "Weight":
#             unit = st.selectbox("Select Conversation", ["Kilegrams to Pounds","Pounds to Kilegrams"])
#         elif category == "Time":
#             unit = st.selectbox("Select Conversation", ["Seconds to Minutes","Minutes to seconds","Minutes to Hours","Hours to Minutes","Hours to Days","Days to Hours"])
        
#         value = st.number_input("Enter your value")


import streamlit as st

st.title("Unit Converter App")
st.markdown("### Converts Length, Weight and Time instantly")
st.write("Welcome! Select a Category")

category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Select conversion unit based on category
if category == "Length":
    unit = st.selectbox("Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversion", [
        "Seconds to Minutes", "Minutes to Seconds",
        "Minutes to Hours", "Hours to Minutes",
        "Hours to Days", "Days to Hours"
    ])

value = st.number_input("Enter your value")

def convert_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

        value = st.number_input("Enter your value")

if st.button("Convert"):
    result = convert_unit(category, value, unit)
    st.success(f"The result is {result:2f}")
