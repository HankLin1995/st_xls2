import streamlit as st

# 初始化或更新session_state以跟踪當前顯示的頁面
if 'current_page' not in st.session_state:
    st.session_state.current_page = ''

def NoselectPage():
    st.header("	:dart:歡迎來到主頁面!")
    st.write("請從	:point_right:**側邊欄**:point_left:選擇一個構造物名稱。")
    st.session_state.current_page = 'NoselectPage'

def Uchannel():
    st.header("	:bookmark_tabs: U型溝計算")
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

def Tchannel():
    st.subheader("梯型溝")
    with st.form("my_form"):
        col1, col2 = st.columns([1, 1])  # 两列，宽度比例为 1:1
        with col1:
            first_name = st.text_input("First Name2", key="first_name")
        with col2:
            last_name = st.text_input("Last Name2", key="last_name")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            # 更新頁面狀態以保留在當前頁面
            st.session_state.current_page = 'Tchannel'

def Cchannel():
    st.subheader("圓型溝")
    with st.form("my_form"):
        col1, col2 = st.columns([1, 1])  # 两列，宽度比例为 1:1
        with col1:
            first_name = st.text_input("First Name3", key="first_name")
        with col2:
            last_name = st.text_input("Last Name3", key="last_name")
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            st.write("First Name:", first_name)
            st.write("Last Name:", last_name)
            # 更新頁面狀態以保留在當前頁面
            st.session_state.current_page = 'Cchannel'
# 在側邊欄添加一個標題
st.sidebar.title("	:balloon:水理計算系統")
type=st.sidebar.selectbox("**選擇構造物**", ["明渠", "暗渠", "倒虹吸工"])
st.sidebar.divider()

# 使用session_state來記住按下的按鈕

if type=="明渠":

    if st.sidebar.button(":one: U型溝"):
        st.session_state.current_page = 'Uchannel'
    if st.sidebar.button(":two: 梯形溝"):
        st.session_state.current_page = 'Tchannel'
    if st.sidebar.button(":three: 圓形溝"):
        st.session_state.current_page = 'Cchannel'
else:
    st.session_state.current_page = 'NoselectPage'

# 根據session_state中記錄的狀態顯示對應的頁面
if st.session_state.current_page == 'Uchannel':
    Uchannel()
elif st.session_state.current_page == 'Tchannel':
    Tchannel()
elif st.session_state.current_page == 'Cchannel':
    Cchannel()
else:
    NoselectPage()
