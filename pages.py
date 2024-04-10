import streamlit as st
from data_stream import stream_data  # 導入資料流模組
import math
import sympy as sp

def Uchannel():
    st.header(":bookmark_tabs: U型溝計算")
    # 創建一個表單
    with st.form("input_form"):
        st.write("**已知條件：**")
        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            q = st.number_input("計畫流量Q (CMS)", value=18.0)
            n = st.number_input("糙率係數n", value=0.0180, format="%.3f")
            s = st.number_input("渠道縱坡 s=1/", value=1000)
            b = st.number_input("渠寬W (M)", value=6.0)
            fill_angle = st.number_input("填角F (M)", value=0.0)
            # material = st.selectbox("材質", ["鋼筋混凝土", "其他"])
        with col2:
            st.image('photos/images.jpg', caption='U型溝照片範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")


    if submit_button:

        st.write("計畫流量Q:", q, "CMS")
        st.write("糙率係數n:", n)
        st.write("渠道縱坡 s=1/", s)
        st.write("渠道寬度W:", b, "M")
        st.write("填角F:", fill_angle, "M")
        # st.write("材質:", material)
        
    st.session_state.current_page = 'Uchannel'
