import streamlit as st
import pandas as pd
import io
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
st.set_page_config(
    page_title="Trang Chủ",
    page_icon="👋",
    #initial_sidebar_state = "expanded"
    layout= "wide",
    initial_sidebar_state = "collapsed",
)
# Đọc dữ liệu từ file Excel
df = pd.read_excel("./Book1.xlsx")
sf = pd.read_excel("./result.xlsx")
excel_file = "result.xlsx"
excel_file1 = "Book1.xlsx"
# Khai báo giá trị k để so sánh
def write_to_excel(ks, row, d, excel_file):
    row1 = row + 1
    ab = st.session_state.get("ex", None)
    gf = pd.DataFrame([ab])
    with pd.ExcelWriter(excel_file, mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:
        gf.to_excel(writer, startrow=row1, startcol=d, index=False, header=False)
    return
if st.button("Cập nhật dữ liệu"):
    today = datetime.now()
    st.subheader(df.iloc[0, 0])
    time = str(today - df.iloc[0, 0])
    time1 = int(str(time[:2]))
    if time1 > 1:
        maeday = str(df.iloc[0, 0])
        date_object1 = datetime.strptime(maeday, '%Y-%m-%d %H:%M:%S')
        date_object2 = date_object1 + timedelta(days=1)
        maeday2 = str(date_object2)
        maeday1 = maeday2[:10]
        date_object = datetime.strptime(maeday1, '%Y-%m-%d')
        new_date_string = date_object.strftime('%d-%m-%Y')
        url = 'https://3ketqua.net/xo-so-mien-bac.php?ngay='+new_date_string
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
        soup = BeautifulSoup(html_content, 'html.parser')
        elements_with_id = soup.find(id='rs_0_0')
        div_text = elements_with_id.text
        #element_dict = json.loads(elements_with_id)
        #st.write(f"ID: {element_dict['id']}")
        #st.write(f"Name: {element_dict['name']}")
        new_row = {}
        new_row_df = pd.DataFrame([new_row])
        kf = pd.concat([df.iloc[:0], new_row_df, df.iloc[0:]], ignore_index=True)
        kf.to_excel(excel_file1, index=False)
        ks = date_object
        st.session_state["ex"] = ks
        write_to_excel(ks, 0, 0, excel_file1)
        ks1 = int(div_text)
        st.session_state["ex"] = ks1
        write_to_excel(ks1, 0, 1, excel_file1)
h = int(st.number_input("Ngày bắt đầu đếm dữ liệu", step = 1))
tab1, tab2 = st.tabs(["TỔNG HỢP", "CHỌN NGÀY"])
with tab2:
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    with col1:
        st.subheader(df.iloc[h, 0])
    with col2:
        st.subheader(df.iloc[h, 1])
    nd = int(st.number_input("Số ngày đếm dữ liệu", step = 1))
    k = nd + 1
    num_r = []
    numx = []
    ff = pd.DataFrame(columns=['Lớn', 'Bé'])
    for bd in range (h,h+20):
        for i in range(h,h+k):
            l = int(str(int(df.iloc[i, 1]))[-2:])  # Lấy hai ký tự cuối cùng của giá trị và chuyển thành chuỗi
            if l >= 50:
                num_r.append(1)
            else:
                numx.append(1)
        if nd != 0:
            big = round((len(num_r)/(k))*100,2)
            small = round((len(numx)/(k))*100,2)
            ff = ff._append({'Lớn': big, 'Bé': small},ignore_index=True)
        k = k + 1
        num_r = []
        numx = []
    st.dataframe(ff, use_container_width=True)
with tab1:
    j = int(st.number_input("Ngày bắt đầu đếm", step = 1))
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    with col1:
        st.subheader(df.iloc[j, 0])
    with col2:
        st.subheader(df.iloc[j, 1])
    nd = int(st.number_input("Số ngày", step = 1))
    k = nd + j
    col1, col2 = st.columns([0.5, 0.5], gap="small")
    with col1:
        st.subheader(df.iloc[k, 0])
    with col2:
        st.subheader(df.iloc[k, 1])
    num_r = []
    numx = []
    ff = pd.DataFrame(columns=['Lớn', 'Bé'])
    for i in range(j, k):
        l = int(str(int(df.iloc[i, 1]))[-2:])  # Lấy hai ký tự cuối cùng của giá trị và chuyển thành chuỗi
        if l >= 50:
            num_r.append(1)
        else:
            numx.append(1)
    if nd != 0:
        col1, col2 = st.columns([0.5, 0.5], gap="small")
        with col1:
            st.write("Tỉ lệ ra số lớn: ",round((len(num_r) / (k - j)) * 100, 2))
            st.write("Tỉ lệ ra số bé: ",round((len(numx) / (k - j)) * 100, 2))
        with col2:
            st.subheader(df.iloc[j-1, 0])
            st.subheader(df.iloc[j-1, 1])
            st.subheader(df.iloc[j, 1])
