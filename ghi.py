import streamlit as st
import pandas as pd

# Đọc dữ liệu từ file Excel
df = pd.read_excel("./Book1.xlsx")

# Khai báo giá trị k để so sánh

# Danh sách để lưu số hàng thỏa mãn điều kiện
#bd = st.number_input("Biên độ của cầu")
nd = int(st.number_input("Số ngày soi cầu"))
kd = int(st.number_input("Ngày trong tháng:"))
bd = 1
#if bd == 0 :
    #bd = 5
    #st.write("Bên độ soi cầu là: ",bd)
num_r = []
numx = []
numy = []
num_d = []
# Duyệt qua các hàng của DataFrame
st.write("Ngày dừng lại để tính toán",df.iloc[kd, 0])
if nd > 2:
    for u in range(0, nd):
        x_u = str(int(df.iloc[u+kd, 1]))[-2:]
        y_u = df.iloc[u, 0]
        numx.append(x_u)
        numy.append(y_u)
        if u > 0:
            st.write(int(numx[u]) - int(numx[u-1]))
st.write(str(numx),df.iloc[0, 0])
for bd in range(1,16):
    if nd > 2:
        for i in range(1,len(df)-20):
            l = int(str(int(df.iloc[i, 1]))[-2:])  # Lấy hai ký tự cuối cùng của giá trị và chuyển thành chuỗi
            l1 = int(str(int(df.iloc[i + 1, 1]))[-2:])
            x1 = l1 - l
            if (int(numx[1]) - int(numx[0])) - bd <= x1 <= (int(numx[1]) - int(numx[0])) + bd:
                match_found = True
                for p in range(2, nd):
                    l_p = int(str(int(df.iloc[i+p, 1]))[-2:])
                    l_f = int(str(int(df.iloc[i+p-1, 1]))[-2:])
                    x_p = l_p - l_f
                    if (int(numx[p]) - int(numx[p-1]))- bd <= x_p <= (int(numx[p]) - int(numx[p-1])) + bd:
                        if p == nd - 1:
                            lits=[]
                            for m in range(0,nd):
                                pl = i+m
                                lits.append(df.iloc[pl, 1])
                            num_r.append(str(int(df.iloc[i-1, 1]))[-2:])
                            st.write(df.iloc[i, 0])
                            #st.write(lits,)
                            st.write(str(int(df.iloc[i-1, 1]))[-2:])
                    else:
                        break
        #st.write("Các chỉ số hàng thỏa mãn điều kiện:")
        #st.write(str(num_r))
    tl = len(num_r)
    #st.write(tl)
    st.subheader(f":red[Biên độ dao động của cầu = {bd}]")
    #st.write(nd)
    lon = 0
    be = 0
    if tl != 0:
        for nu in range(0,tl):
            kh = int(num_r[nu])
            if kh > 50:
                lon = lon + 1
            else:
                be = be + 1
            st.write("Tỉ lệ ra số Lớn là :",round((lon/tl)*100,2),"%")
            st.write("Tỉ lệ ra số Bé là :",round((be/tl)*100,2),"%")
    else:
        st.write("Dữ liệu không có cầu này! Vui lòng chọn ngày cầu nhỏ hơn")
    num_r = []
st.write(num_d)
