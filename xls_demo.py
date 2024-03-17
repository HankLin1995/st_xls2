import pandas as pd
import streamlit as st
import openpyxl
import os

# Streamlit App
def main():
    st.title('Excel 平均值計算和下載')

    template_file = 'template/sample.xlsx'

    workbook = openpyxl.load_workbook(template_file)

    # 取得第一個工作表
    sheet = workbook.worksheets[0]

    # 設定 sheet 工作表 A2 儲存格內容為 "Test Excel"
    sheet['A2'] = 'Test Excel.'

    # 保存文件到临时目录
    output_file = 'test.xlsx'
    workbook.save(output_file)

    # 提供下载链接给用户
    st.write('点击下面的按钮下载处理后的 Excel 文件:')
    with open(output_file, 'rb') as f:
        bytes_data = f.read()
    st.download_button(label='下载文件', data=bytes_data, file_name=output_file)

with st.form("my_form"):
    col1, col2 = st.columns([1, 1])  # 两列，宽度比例为 1:1
    with col1:
        first_name = st.text_input("First Name")
    with col2:
        last_name = st.text_input("Last Name")
    
    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.write("First Name:", first_name)
    st.write("Last Name:", last_name)

# 启动应用
if __name__ == "__main__":
    main()
