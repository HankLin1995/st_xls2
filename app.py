import streamlit as st
from pages import NoselectPage, Uchannel, Tchannel, Cchannel,steelsheetpile  # 導入各個頁面的模組

st.set_page_config(
    page_title="HYD Calculator",
    page_icon="	:sweat_drops:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 初始化或更新 session_state 以追踪當前顯示的頁面
if 'current_page' not in st.session_state:
    st.session_state.current_page = ''

# 在側邊欄添加一個標題
st.sidebar.title(":balloon:水理計算系統")
type = st.sidebar.selectbox("**選擇構造物**", ["明渠", "擋土設施","暗渠", "倒虹吸工"])
st.sidebar.divider()

# 使用 session_state 來記住按下的按鈕
if type == "明渠":
    if st.sidebar.button(":one: U型溝"):
        st.session_state.current_page = 'Uchannel'
    if st.sidebar.button(":two: 梯形溝"):
        st.session_state.current_page = 'Tchannel'
    if st.sidebar.button(":three: 圓形溝"):
        st.session_state.current_page = 'Cchannel'

elif type=="擋土設施":
    if st.sidebar.button(":one: 懸臂式板樁"):
        st.session_state.current_page = 'steelsheetpile'
else:
    st.session_state.current_page = 'NoselectPage'

# 根據 session_state 中記錄的狀態顯示對應的頁面
if st.session_state.current_page == 'Uchannel':
    Uchannel()
elif st.session_state.current_page == 'Tchannel':
    Tchannel()
elif st.session_state.current_page == 'Cchannel':
    Cchannel()
elif st.session_state.current_page == 'steelsheetpile':
    steelsheetpile()
else:
    NoselectPage()
