import streamlit as st
from pages import  Uchannel  # 導入各個頁面的模組
from page_Foundation import SP # 導入各個頁面的模組

st.set_page_config(
    page_title="HYD Calculator",
    page_icon="	:sweat_drops:",
    layout="centered",
    initial_sidebar_state="expanded",
)

if 'current_page' not in st.session_state:
    st.session_state.current_page = ''

def NoselectPage():
    st.header(":dart:歡迎來到主頁面!")

    st.write("""
    #### 使用說明:
    :one: 請從:point_right:**側邊欄**:point_left:選擇一個構造物名稱\n
    :two: 選擇計算項目後顯示計算畫面\n
    :three:計算前可先填寫工程資訊\n
    :four:輸入基本參數後點選計算\n
    :red[規範內容引用有錯誤再煩請指教更正]\n
    """)

    st.info(" **作者:** HankLin\n\n **部落格:** https://hankvba.blogspot.com/")
    st.session_state.current_page = 'NoselectPage'

#------側邊欄設置內容------

st.sidebar.write(st.session_state)

st.sidebar.title(":sweat_drops: 雲端計算系統")
st.sidebar.info("作者:**HankLin**")

st.sidebar.divider()

st.sidebar.write(":books: 構造物名稱")
type = st.sidebar.selectbox( ">>",["明渠", "擋土設施","暗渠", "倒虹吸工"])

if type == "明渠":
    if st.sidebar.button(" :small_blue_diamond: U型溝"):
        st.session_state.current_page = 'Uchannel'
    if st.sidebar.button(" :small_blue_diamond: T型溝"):
        st.session_state.current_page = 'Uchannel'
elif type=="擋土設施":
    if st.sidebar.button(" :small_blue_diamond:  懸臂式板樁"):
        st.session_state.current_page = 'SP'
else:
    st.session_state.current_page = 'NoselectPage'

st.sidebar.divider()

with st.sidebar.expander("**:department_store: 報表設定**"):

    st.markdown("---")
    st.text_input(":small_orange_diamond: 公司名稱", key="company") #加入key之後就會變成session_state
    st.text_input(":small_orange_diamond: 工程名稱", key="conName")
    st.text_input(":small_orange_diamond: 工程地點", key="conLoc")

#------主要計算項目------

if st.session_state.current_page == 'Uchannel':
    Uchannel()
elif st.session_state.current_page == 'SP':
    SP()
else:
    NoselectPage()
