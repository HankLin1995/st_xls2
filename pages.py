import streamlit as st
from data_stream import stream_data  # 導入資料流模組
import math
import sympy as sp

def calculate_active_pressure_coefficient(phi):
    Ka = (1 - math.sin(math.radians(phi))) / (1 + math.sin(math.radians(phi)))
    return Ka

def calculate_passive_pressure_coefficient(phi):
    Kp = (1 + math.sin(math.radians(phi))) / (1 - math.sin(math.radians(phi)))
    return Kp

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
            st.image('st_xls2/photos/images.jpg', caption='U型溝照片範例')

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
            s = st.number_input(r"渠道縱坡=1\:x", value=900)
            m = st.number_input(r"側坡=1\:m", value=1.5)

        with col2:
            st.image('st_xls2/photos/images.jpg', caption='U型溝照片範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")

    if submit_button:

        st.write("最佳水利斷面條件為:")
        st.latex(r" b = 2y tan \\frac{\Theta}{2}")
        st.latex("A =  \\frac{y}{2} (b+T)")
        st.write("計畫流量Q:", q, "CMS")
        st.write("糙率係數n:", n)
        st.write("渠道縱坡 s=1/", s)
    st.session_state.current_page = 'Tchannel'

def Cchannel():
    st.subheader("圓型溝")
    # 圓型溝的實現...
    st.session_state.current_page = 'Cchannel'

def steelsheetpile():
    st.header(":bookmark_tabs: 懸臂式板樁")
    # 創建一個表單
    with st.form("input_form"):
        st.write("**已知條件：**")
        st.write("")
        col1, col2 = st.columns(2)

        with col1:
            H = st.number_input("開挖深度(M)", value=5)
            r = st.number_input("土壤單位重", value=1.8,)
            phi = st.number_input("土壤安息角", value=30,help="常見為30~33")
            FS = st.number_input("安全係數", value=1.5,help="規範建議>=1.5")


        with col2:
            st.image('st_xls2/photos/St.jpg', caption='Fig1.懸臂式板樁範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")

    
    if submit_button:

        st.write("#### 依據內政部建築物基礎構造設計規範(112年)")

        st.write("#### 1.基本參數")
        
        st.latex(r"\phi = " + str(phi) + r"^\circ")

        st.write(stream_data("主動土壓力係數（Ka）的計算公式如下："))
        st.latex(r"K_a = \frac{{1 - \sin(\phi)}}{{1 + \sin(\phi)}}")
        Ka = calculate_active_pressure_coefficient(phi)
        st.write("Ka=", Ka)

        st.write(stream_data("被動土壓力係數（Kp）的計算公式如下："))
        st.latex(r"K_p = \frac{{1 + \sin(\phi)}}{{1 - \sin(\phi)}}")
        Kp = calculate_passive_pressure_coefficient(phi)
        st.write("Kp=", Kp)

        st.divider()

        #計算第一階段

        st.write("#### 2.受力平衡計算")

        st.write(stream_data("""(1) 假設 O 點為不動點，將擋土牆分為上下兩部分。下圖之牆後被動
                                土壓力與牆前主動土壓力的差值，以一集中力 R 作用於上圖 O 點。
                                \n(2) 對上圖之 O 點取彎矩平衡，取適當的彎矩安全係數 FS，可求得 d0；
                                取水平力平衡，可得 R 值。
                                \n(3) FS 大約等於 1.5。
                                """))

        st.latex("右側土壓力="+r"P_a = \frac{1}{2} \cdot \gamma \cdot (H + d_0) \cdot K_a")
        st.latex("左側土壓力="+r"P_p = \frac{1}{2} \cdot \gamma  \cdot (d_0) \cdot K_p")

        st.write("**對上圖之 O 點取彎矩平衡。**")

        st.write("右側彎矩計算式=")
        st.latex(r"M_r = \frac{1}{2} \cdot r \cdot (H + d_0) \cdot K_a \cdot \frac{(H + d_0)}{3}")      
        st.write("左側彎矩計算式=")
        st.latex(r"M_l = \frac{1}{2} \cdot r \cdot d_0 \cdot K_p \cdot \frac{d_0}{3}")

        st.write("給定安全係數=",FS)
        st.latex(r"M_r = 1.5 \cdot M_l")        

        d0 = sp.Symbol('d0')

        # 右侧彎矩和左侧彎矩的表达式
        Mr = (1/2) * r * (H + d0) * Ka * ((H + d0) / 3)
        Ml = (1/2) * r * d0 * Kp * (d0 / 3)

        # 彎矩平衡方程
        equation = sp.Eq(FS * Ml, Mr)

        # 解方程，得到d0
        d0_solution = sp.solve(equation, d0)

        # 显示解
        st.write("解出的d0：", d0_solution)

        #計算第二階段

    st.session_state.current_page = 'steelsheetpile'