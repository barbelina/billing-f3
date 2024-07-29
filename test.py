import numpy as np
import pandas as pd
import streamlit as st

# Assuming kroscek is your DataFrame
# Example DataFrame for demonstration
data = {'SELISIH': [120, 80, -150, 90, 0]}
kroscek = pd.DataFrame(data)

# Define conditions and corresponding choices
conditions_100 = [
    (kroscek['SELISIH'] > 100) | (kroscek['SELISIH'] < -100),
    (kroscek['SELISIH'] <= 100) & (kroscek['SELISIH'] >= -100)
]

letters = ['Selisih Besar', 'Normal']

# Apply np.select with correct conditions and choices
kroscek['SELISIH 100%'] = np.select(conditions_100, letters, default='Undefined')

st.write(kroscek)
