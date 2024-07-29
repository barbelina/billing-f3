import pandas as pd
import streamlit as st
import numpy as np

from st_aggrid import AgGrid, JsCode
from st_aggrid.grid_options_builder import GridOptionsBuilder

arr = np.array([1, 2, 3, 4, 5])

conditions = [arr > 2, arr < 5]
choices = [arr, arr * 2]

result = np.select(conditions, choices, default=0)

st.write(result)
