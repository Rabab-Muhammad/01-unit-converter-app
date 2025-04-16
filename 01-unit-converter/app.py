import streamlit as st

st.title("🔄 Unit Converter App")
st.markdown("### 📏⚖️⏱️ Converts Length, Weight and Time instantly!")
st.write("👋 Welcome! Please select a category to begin:")

category = st.selectbox("📚 Choose a category", ["Length 📏", "Weight ⚖️", "Time ⏱️"])

# Remove emojis for internal logic (clean values)
category_clean = category.split()[0]

# Select conversion unit based on category
if category_clean == "Length":
    unit = st.selectbox("🔁 Select Conversion", ["Kilometers to Miles 🛣️", "Miles to Kilometers 🛤️"])
elif category_clean == "Weight":
    unit = st.selectbox("🔁 Select Conversion", ["Kilograms to Pounds 🏋️", "Pounds to Kilograms 🧱"])
elif category_clean == "Time":
    unit = st.selectbox("🔁 Select Conversion", [
        "Seconds to Minutes ⏳", "Minutes to Seconds ⌛",
        "Minutes to Hours 🕐", "Hours to Minutes 🕒",
        "Hours to Days 📆", "Days to Hours ⏰"
    ])

value = st.number_input("🔢 Enter your value")

# Conversion logic
def convert_unit(category, value, unit):
    unit = unit.split(" ")[0:3]  # Keep only actual conversion text
    unit = " ".join(unit)

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

# Convert button
if st.button("🚀 Convert"):
    result = convert_unit(category_clean, value, unit)
    st.success(f"✅ The result is: **{result:.2f}** 🎉")
