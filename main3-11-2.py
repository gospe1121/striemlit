import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

"""
3-11.レイアウトを整える
"""

"""

"""



st.sidebar.write('2カラム表示')



left_column,right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')



expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.text_input('入力欄')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')

# 'あなたの趣味：',text,'です。'

# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'コンディション：',condition



