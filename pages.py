import streamlit as st
from data_stream import stream_data  # 導入資料流模組

def NoselectPage():
    st.header(":dart:歡迎來到主頁面!")
    st.write("請從:point_right:**側邊欄**:point_left:選擇一個構造物名稱。")
    st.session_state.current_page = 'NoselectPage'

def Uchannel():
    st.header(":bookmark_tabs: U型溝計算")
    # 創建一個表單
    with st.form("input_form"):
        st.write("**已知條件：**")
        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            q = st.number_input("計畫流量Q (CMS)", value=18.0)
            n = st.number_input("糙率係數n", value=0.018)
            s = st.number_input("渠道縱坡 s=1/", value=1000)
            b = st.number_input("渠道寬度B (M)", value=6.0)
            fill_angle = st.number_input("填角 (M)", value=0.0)
            material = st.selectbox("材質", ["鋼筋混凝土", "其他"])
        with col2:
            st.image('photos/images.jpg', caption='U型溝照片範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")


    if submit_button:
        st.write("計畫流量Q:", q, "CMS")
        st.write("糙率係數n:", n)
        st.write("渠道縱坡 s=1/", s)
        st.write("渠道寬度B:", b, "M")
        st.write("填角:", fill_angle, "M")
        st.write("材質:", material)
            # 更新頁面狀態以保留在當前頁面
        st.session_state.current_page = 'Uchannel'
    st.session_state.current_page = 'Uchannel'

def Tchannel():
    st.header(":bookmark_tabs: 梯型溝計算")
    with st.form("input_form"):
        st.write("**已知條件：**")
        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            q = st.number_input("計畫流量Q (CMS)", value=20)
            n = st.number_input("糙率係數n", value=0.018)
            s = st.number_input("渠道縱坡=1\:x", value=900)
            m = st.number_input("側坡=1\:m", value=1.5)

        with col2:
            st.image('photos/images.jpg', caption='U型溝照片範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")

    if submit_button:

        st.write("最佳水利斷面條件為:")
        st.latex(" b = 2y tan \\frac{\Theta}{2}")
        st.latex("A =  \\frac{y}{2} (b+T)")
        st.write("計畫流量Q:", q, "CMS")
        st.write("糙率係數n:", n)
        st.write("渠道縱坡 s=1/", s)
    st.session_state.current_page = 'Tchannel'

def Cchannel():
    st.subheader("圓型溝")
    # 圓型溝的實現...
    st.session_state.current_page = 'Cchannel'
