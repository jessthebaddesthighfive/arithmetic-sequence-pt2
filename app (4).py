import streamlit as st

st.set_page_config(page_title="Arithmetic Sequence Generator", layout="centered")

st.title("📐 Arithmetic Sequence Generator")
st.write(
    "Enter the **first term**, **common difference**, and **number of terms** "
    "to generate an arithmetic sequence."
)

# User inputs
a1 = st.number_input("First term (a₁)", value=1.0)
d = st.number_input("Common difference (d)", value=1.0)
n = st.number_input("Number of terms (n)", min_value=1, step=1, value=10)

def arithmetic_sequence(a1, d, n):
    return [a1 + i * d for i in range(int(n))]

if st.button("Generate Sequence"):
    sequence = arithmetic_sequence(a1, d, n)

    st.subheader("📋 Sequence Terms")
    st.write(sequence)

    st.subheader("🧮 General Term Formula")
    st.latex(r"a_n = a_1 + (n-1)d")

    st.write(f"**Substituted:**  aₙ = {a1} + (n − 1)({d})")
