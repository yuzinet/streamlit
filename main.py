import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('Interactive widgets')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右からむ')

text = st.text_input('あなたの趣味を教えてください。')


expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write(text)
expander.write('問い合わせ内容を書く')

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたのコンディションは？', 0, 100, 50)

# 'あなたの好きな趣味は', text, 'です。'
# 'あなたのコンディション',condition

# if st.checkbox('Show Image', True):
#     img = Image.open('sample.png')
#     st.image(img, caption='Tanji Yuya', use_column_width=True)

