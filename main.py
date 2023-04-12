import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

"""
タイトル設定st.title
"""
st.title('Streamlit 超入門')

"""
文字挿入st.write
"""
st.write('Interacrive Widgets')


condition = st.slider('あなたの今の調子は？',0,100,50)

'コンディション：',condition


text = st.text_input('あなたの趣味を教えて下さい。')

'あなたの趣味：',text,'です。'

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)


'あなたの好きな数字は、', option ,'です。'


if st.checkbox('Show Image'):

    img = Image.open('image.jpg')
    st.image(img, caption='test',use_column_width=True)






