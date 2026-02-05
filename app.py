import streamlit as st
import math

# Page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮")

st.title("🧮 Scientific Calculator")
st.markdown("Welcome to your Hugging Face-hosted calculator. Select your mode and perform calculations below.")

# Sidebar for operation selection
mode = st.sidebar.selectbox("Select Mode", ["Basic Arithmetic", "Scientific Functions"])

if mode == "Basic Arithmetic":
    col1, col2, col3 = st.columns([4, 2, 4])
    
    with col1:
        num1 = st.number_input("First Number", value=0.0)
    with col2:
        op = st.selectbox("Operation", ["+", "-", "*", "/", "^"])
    with col3:
        num2 = st.number_input("Second Number", value=0.0)

    if st.button("Calculate"):
        if op == "+": result = num1 + num2
        elif op == "-": result = num1 - num2
        elif op == "*": result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error: Division by Zero"
        elif op == "^": result = math.pow(num1, num2)
        
        st.success(f"**Result:** {result}")

elif mode == "Scientific Functions":
    col1, col2 = st.columns(2)
    
    with col1:
        func = st.selectbox("Function", ["sqrt", "log10", "ln", "sin", "cos", "tan"])
    with col2:
        val = st.number_input("Value", value=1.0)
    
    st.info("Note: Trig functions (sin, cos, tan) assume the input is in **Degrees**.")

    if st.button("Calculate"):
        try:
            if func == "sqrt": result = math.sqrt(val)
            elif func == "log10": result = math.log10(val)
            elif func == "ln": result = math.log(val)
            elif func == "sin": result = math.sin(math.radians(val))
            elif func == "cos": result = math.cos(math.radians(val))
            elif func == "tan": result = math.tan(math.radians(val))
            
            st.success(f"**Result:** {result}")
        except ValueError:
            st.error("Error: Invalid input for this function.")

st.markdown("---")
st.caption("Powered by Streamlit and Python Math Library")
