import streamlit as st
import time

st.title('Streamlit入門')

st.write('プログレスバー')
"Start!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

"Done!"

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容')

#option = st.text_input('あなたの趣味を教えてください')
#'わたしの趣味は、',option,'です。'
#condition = st.slider('あなたの今の調子は？',0,100,50)
#'調子は',condition,'です'


# if st.checkbox("Show Image"):
#     img = Image.open("woody.jpg")
#     st.image(img,caption="Woody",use_column_width=True)
