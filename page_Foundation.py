import streamlit as st
from data_stream import stream_data  # 導入資料流模組
import math
import sympy as sp
import numpy as np

def calculate_active_pressure_coefficient(phi):
    Ka = (1 - math.sin(math.radians(phi))) / (1 + math.sin(math.radians(phi)))
    return Ka

def calculate_passive_pressure_coefficient(phi):
    Kp = (1 + math.sin(math.radians(phi))) / (1 - math.sin(math.radians(phi)))
    return Kp

def resolve_d0(Ka,Kp,H,FS,r):

    d0 = sp.Symbol('d0')

    Mr = (1/2) * r * (H + d0)**2 * Ka * ((H + d0) / 3)
    Ml = (1/2) * r * d0**2 * Kp * (d0 / 3)        # 彎矩平衡方程
    equation = sp.Eq(Ml, FS*Mr)

    # 解方程，得到d0
    d0_solutions = sp.solve(equation, d0)
    # 筛选出正的解
    positive_solutions = [sol.evalf() for sol in d0_solutions if sol.is_real and sol.evalf() > 0]

    for sol in positive_solutions:
        d0_sol=float(sol)
    return d0_sol
    
def resolve_D(d0_sol, r, H,R, Ka, Kp):
    i_value = None
    S_test_value = None
    for i in np.arange(1.1, 1.21, 0.01):
        D_test = i * d0_sol
        P_Al = (1/2) * (r * d0_sol * Ka + r * D_test * Ka) * (D_test - d0_sol)
        P_pl = (1/2) * (r * (H + d0_sol) * Kp + r * (H + D_test) * Kp) * (D_test - d0_sol)
        S_test = P_pl - P_Al
        if S_test > R:
            i_value = i
            S_test_value = S_test
            break
    return i_value, S_test_value


def SP():
    st.header(":memo: 懸臂式板樁")
    # 創建一個表單
    with st.form("input_form"):
        st.write("**已知條件：**")
        st.write("")
        col1, col2 = st.columns(2)

        with col1:

            H = st.number_input("開挖深度[H]", value=5.0,help="單位=公尺")
            r = st.number_input("土壤單位重", value=1.8,help="計算上不影響結果")
            phi = st.number_input("土壤安息角", value=30,help="常見為30~33")
            FS = st.number_input("安全係數", value=1.5,help="規範建議>=1.5")

        with col2:
            # st.image('st_xls2/photos/St.jpg', caption='Fig1.懸臂式板樁範例')
            st.image('photos/St.jpg', caption='Fig1.懸臂式板樁範例')
        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")

    
    if submit_button:

        #計算過程

        Ka = calculate_active_pressure_coefficient(phi)
        Kp = calculate_passive_pressure_coefficient(phi)

        d0_sol=resolve_d0(Ka,Kp,H,FS,r)
        
        # 代入 d0 的解到 P_A 和 P_p 的表达式中
        P_A_value = (1/2) *r * (H + d0_sol)**2 * Ka
        P_p_value = (1/2) * r * (d0_sol)**2 * Kp

        # 计算 R
        R_value = P_p_value - P_A_value
        i_value, S_test_value = resolve_D(d0_sol, r, H,R_value, Ka, Kp)

        D=i_value*d0_sol

        #說明開始

        st.write(" #### 1.規範依據")
        url = "https://www.nlma.gov.tw/filesys/file/EMMA/L1120811.pdf"
        st.write(":clipboard:內政部建築物基礎構造設計規範(112年)--7.5.3")
        st.write(":link:點我查看[PDF](%s)" % url)
        #基本參數設定

        st.divider()
        st.write("#### 2.基本參數")
        
        st.latex(r"\phi = " + str(phi) + r"^\circ")

        st.write("主動土壓力係數（Ka）的計算公式如下：")
        st.latex(r"K_a = \frac{{1 - \sin(\phi)}}{{1 + \sin(\phi)}}")
        st.write("Ka=", Ka)

        st.write("被動土壓力係數（Kp）的計算公式如下：")
        st.latex(r"K_p = \frac{{1 + \sin(\phi)}}{{1 - \sin(\phi)}}")
        st.write("Kp=", Kp)

        st.divider()

        #計算第一階段

        st.write("#### 3.第一階段(上部)計算")

        st.write("""(1) 假設 O 點為不動點，將擋土牆分為上下兩部分。下圖之牆後被動
                                土壓力與牆前主動土壓力的差值，以一集中力 R 作用於上圖 O 點。
                                \n(2) 對上圖之 O 點取彎矩平衡，取適當的彎矩安全係數 FS，可求得 d0；
                                取水平力平衡，可得 R 值。""")

        st.latex(r"P_A = \frac{1}{2} \cdot \gamma \cdot (H + d_0)^2 \cdot K_a")
        st.latex(r"P_p = \frac{1}{2} \cdot \gamma  \cdot (d_0)^2 \cdot K_p")
        st.latex(r"R = P_p- P_A")

        st.write("**對上圖之 O 點取彎矩平衡，FS放置於右側彎矩。**")

        st.write("右側彎矩計算式=")
        st.latex(r"M_r = \frac{1}{2} \cdot r \cdot (H + d_0)^2 \cdot K_a \cdot \frac{(H + d_0)}{3}")    
        st.write("左側彎矩計算式=")
        st.latex(r"M_l = \frac{1}{2} \cdot r \cdot d_0^2 \cdot K_p \cdot \frac{d_0}{3}")

        st.write("解出的d0：",  d0_sol,"M")
        st.write("**對上圖取力平衡**")

        # 显示结果
        st.write("計算得到的R值為:", R_value)

        #計算第二階段
        st.divider()
        st.write("#### 4.第二階段(下部)計算")
        st.write("**計算目的:至少須滿足  S>=R**")
        st.write("根據經驗  D=1.1~1.2d0")

        st.latex(r"P_{\text{Al}} = \frac{1}{2}(r \cdot d_0 \cdot K_a + r \cdot D \cdot K_a)(D - d_0)")
        st.latex(r"P_{\text{pl}} = \frac{1}{2}(r \cdot (H + d_0) \cdot K_p + r \cdot (H + D) \cdot K_p))(D - d_0)")
        st.latex(r"S = P_{\text{pl}}- P_{\text{Al}}")

        st.write("當i=",round(i_value,2),"時，S=",S_test_value)
        st.write("此時滿足  S>=R，則D=", i_value*d0_sol)

        st.divider()
        st.write("#### 5.計算成果")
        st.write("計算所得之H+D=",H+D,"M")
        st.write(" ##### :heavy_check_mark: 建議採用懸臂式板樁長度為",math.ceil(H+D),"M")
        st.session_state.current_page = 'SP'
        
    st.session_state.current_page = 'SP'
