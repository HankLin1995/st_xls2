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
            q = st.number_input("計畫流量q (cms)", value=18.0)
            n = st.number_input("曼寧係數n", value=0.0180, format="%.3f")
            s = st.number_input("渠道縱坡 s=1/", value=1000)
            b = st.number_input("渠寬b (m)", value=6.0)
            fill_angle = st.number_input("填角F (m)", value=0.0)
            # material = st.selectbox("材質", ["鋼筋混凝土", "其他"])
        with col2:
            st.image('photos/images.jpg', caption='Fig1.U型溝照片範例')

        # 表單提交按鈕
        submit_button = st.form_submit_button("計算",type="primary")


    if submit_button:

        #---計算開始---

        ## 計算y
        y = sp.Symbol('y')

        P = (b-2*fill_angle)+2*math.sqrt(2)*fill_angle + 2*(y-fill_angle)
        A = b * y-fill_angle**2
        R = A / P
        V=(1 / n) * R** (2/3) * math.sqrt(1/s)
        Q = A * V

        solution = sp.solve(Q - q, y)
        y_sol=float(solution[0])
        st.write("y=" ,y_sol,"m")

        ## 帶入 y,計算Fr,V
        y=y_sol

        P = (b-2*fill_angle)+2*math.sqrt(2)*fill_angle + 2*(y-fill_angle)
        A = b * y-fill_angle**2
        R = A / P
        V=(1 / n) * R** (2/3) * math.sqrt(1/s)
        Q = A * V
        T=b
        Fr=V/(9.81*A/T)**0.5
        hv=V**2/(2*9.81)

        st.write("V =" ,V,"m/s")
        st.write("Fr =" ,Fr)
        # st.write("Q=",Q,"cms")
        st.write("hv=",hv,"m")

        ## 計算yc

        yc=sp.Symbol('yc')
        Tc=b
        Ac=b*yc

        eq=q**2*Tc-9.81*(Ac**3)

        solution2 = sp.solve(eq,yc)
        yc_sol=float(solution2[0])
        st.write("yc=" ,yc_sol,"m")

        Vc=Q/(yc_sol*b)
        st.write("Vc =" ,Vc,"m/s")

        #---過程描述---#

        with open("./md/U.md", "r", encoding="utf-8") as file:
            markdown_text = file.read()

        markdown_text = markdown_text.format(
            q=q,
            n=n,
            B=b,
            F=fill_angle,
            s=s,
            y=round(y,3),
            Q=round(Q,3),
            V=round(V,3),
            Fr=round(Fr,3),
            yc=round(yc_sol,3),
            Vc=round(Vc,3),
            Wall=1

        )

        st.markdown(markdown_text)


        #---計算檢核---#
        err_state=False
        if V>0.7:
            st.write(":white_check_mark:最小容許流速 " )
        else:
            st.write('	:x:最小容許流速請再檢討')
            err_state=True

        if V<3:
            st.write(":white_check_mark:最大容許流速(農工手冊) " )
        elif V<4:
            st.write(":white_check_mark:最大容許流速(合訂本)) " )
        else:
            st.write('	:x:最大容許流速請再檢討')
            err_state=True

        if V<0.66*Vc:
            st.write(":white_check_mark:避免臨界流速(農工手冊)" )
        elif V<0.8*Vc:
            st.write(":white_check_mark:避免臨界流速(合訂本) " )
        else:
            st.write('	:x:臨界流速請再檢討')
            err_state=True

        Fb=max(1/3*y,0.15)

        y_ans=round(y+Fb,3)

        if err_state==False:
            st.info("建議採用牆高至少為 " + str(y_ans) + " M",icon="✔️")



    st.session_state.current_page = 'Uchannel'
