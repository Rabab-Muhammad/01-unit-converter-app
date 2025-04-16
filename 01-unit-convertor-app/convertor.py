import streamlit as st

# Apply custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton > button {
        background: linear-gradient(45deg, #0b5394, #351c75) 
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.4);
    }
    .stButton > button:hover {
        # background: linear-gradient(45deg, #92fe9d, #00c9ff);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        transform: scale(1.05);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 25px;
        margin-top: 20px;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0,201,255,0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🌟 Title and Description
st.markdown("<h1>🧮 Unit Converter with Python & Streamlit 🚀</h1>", unsafe_allow_html=True)
st.write("🔄 Easily convert between different units of **Length**, **Weight**, and **Temperature**.")

# 📌 Sidebar
conversion_type = st.sidebar.selectbox("🌐 Choose Conversion Type", ["📏 Length", "⚖️ Weight", "🌡️ Temperature"])
value = st.number_input("🔢 Enter value", value=0.0, step=0.1)

col1, col2 = st.columns(2)

# 📐 Unit Selection
if "Length" in conversion_type:
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Milimeters", "Miles", "Yards", "Inches", "Feet"])

elif "Weight" in conversion_type:
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Miligrams", "Pounds", "Ounces"])

elif "Temperature" in conversion_type:
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# 🔧 Conversion Functions
def length_convertor(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Milimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Miligrams': 1_000_000,
        'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_convertor(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else ((value - 273.15) * 9/5) + 32
    return value

# 🔘 Convert Button
if st.button("🔁 Convert Now!"):
    if "Length" in conversion_type:
        result = length_convertor(value, from_unit, to_unit)
    elif "Weight" in conversion_type:
        result = weight_convertor(value, from_unit, to_unit)
    elif "Temperature" in conversion_type:
        result = temperature_convertor(value, from_unit, to_unit)

    st.markdown(
        f"<div class='result-box'>✨ {value} {from_unit} = <strong>{result:.4f}</strong> {to_unit} ✨</div>",
        unsafe_allow_html=True
    )

# 🖋️ Footer
st.markdown("<div class='footer'>🧠 Created with ❤️ by Rabab Muhammad</div>", unsafe_allow_html=True)
