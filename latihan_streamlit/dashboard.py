import streamlit as st

st.title('Halaman Dashboard')
st.image('rockcat.jpg', caption='cat')

# fungsi menghitung dan menyimpan total
def total():
    total_nabung = sum(j['Jumlah']
                       for j in st.session_state ['total_semua']
                       if j ['Tipe'] == 'Menabung')
    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric('Total Menabung', f'Rp. {total_nabung}')