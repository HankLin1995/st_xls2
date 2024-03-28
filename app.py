import streamlit as st
# from streamlit_extras.badges import badge
from pages import  Uchannel  # 導入各個頁面的模組
from page_Foundation import SP


def NoselectPage():
    st.header(":dart:歡迎來到主頁面!")
    st.write("請從:point_right:**側邊欄**:point_left:選擇一個構造物名稱。")
    st.info("作者: HankLin")
    # 使用 st.write 函數來設置超連結的樣式
    st.markdown("""
        <a href="https://hankvba.blogspot.com/" target="_blank" style="display: inline-block; background-color: #ffcccc; color: black; padding: 5px 20px; border-radius: 5px; text-decoration: none;">部落格</a>
    """, unsafe_allow_html=True)
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
st.sidebar.title(":sweat_drops: 雲端計算系統")
# st.sidebar.info("作者:**HankLin**")

st.sidebar.divider()
st.sidebar.write(":books: 構造物名稱")
type = st.sidebar.selectbox( ">>",["明渠", "擋土設施","暗渠", "倒虹吸工"])
st.sidebar.divider()

st.sidebar.write("	:page_facing_up: 計算項目")

# 使用 session_state 來記住按下的按鈕
if type == "明渠":
    st.session_state.current_page = 'NoselectPage'
    if st.sidebar.button(" :small_blue_diamond: U型溝"):
        st.session_state.current_page = 'Uchannel'
elif type=="擋土設施":
    # st.session_state.current_page = 'NoselectPage'
    if st.sidebar.button(" :small_blue_diamond:  懸臂式板樁"):
        st.session_state.current_page = 'SP'
else:
    st.session_state.current_page = 'NoselectPage'

st.sidebar.divider()

with st.sidebar.expander("**:department_store: 工程資訊**"):

    # st.sidebar.write("**:department_store: 報表設定**")
    st.write("")
    st.text_input(":small_orange_diamond: 公司名稱",value="雲林管理處", key="company")
    st.text_input(":small_orange_diamond: 工程名稱", key="conName")
    st.text_input(":small_orange_diamond: 工程地點", key="conLoc")

# 根據 session_state 中記錄的狀態顯示對應的頁面
if st.session_state.current_page == 'Uchannel':
    Uchannel()
elif st.session_state.current_page == 'SP':
    SP()
else:
    NoselectPage()
