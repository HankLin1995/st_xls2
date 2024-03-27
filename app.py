import streamlit as st
from pages import  Uchannel  # 導入各個頁面的模組
from page_Foundation import SP

def NoselectPage():
    st.header(":dart:歡迎來到主頁面!")
    st.write("請從:point_right:**側邊欄**:point_left:選擇一個構造物名稱。")
    st.session_state.current_page = 'NoselectPage'

st.set_page_config(
    page_title="HYD Calculator",
    page_icon="	:sweat_drops:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 初始化或更新 session_state 以追踪當前顯示的頁面
if 'current_page' not in st.session_state:
    st.session_state.current_page = ''
if 'conName' not in st.session_state:
    st.session_state['company'] = ''
if 'conName' not in st.session_state:
    st.session_state['conName'] = ''
if 'conLoc' not in st.session_state:
    st.session_state['conLoc'] = ''

# 在側邊欄添加一個標題
st.sidebar.title(":balloon:結構、水理計算系統")

st.sidebar.divider()
type = st.sidebar.selectbox(":books: 構造物選項", ["明渠", "擋土設施","暗渠", "倒虹吸工"])
st.sidebar.divider()

st.sidebar.subheader("	:page_facing_up: 計算項目")

# 使用 session_state 來記住按下的按鈕
if type == "明渠":
    st.session_state.current_page = 'NoselectPage'
    if st.sidebar.button(" U型溝"):
        st.session_state.current_page = 'Uchannel'
elif type=="擋土設施":
    # st.session_state.current_page = 'NoselectPage'
    if st.sidebar.button(" 懸臂式板樁"):
        st.session_state.current_page = 'SP'
else:
    st.session_state.current_page = 'NoselectPage'

st.sidebar.divider()
st.sidebar.write("**:department_store: 報表設定**")
st.sidebar.text_input("請輸入機關全銜", key="company")
st.sidebar.text_input("請輸入工程名稱", key="conName")
st.sidebar.text_input("請輸入工程地點", key="conLoc")

# 根據 session_state 中記錄的狀態顯示對應的頁面
if st.session_state.current_page == 'Uchannel':
    Uchannel()
elif st.session_state.current_page == 'SP':
    SP()
else:
    NoselectPage()
