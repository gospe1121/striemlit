import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

"""
3-11.レイアウトを整える
"""

"""
サイドバー
"""

st.sidebar.write('サイドバー')


text = st.sidebar.text_input('あなたの趣味を教えて下さい。')

'あなたの趣味：',text,'です。'

condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

'コンディション：',condition



