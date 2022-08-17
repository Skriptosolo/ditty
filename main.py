from datetime import datetime
import streamlit as st

st.title("Ditty Leti Priscella Hadi")
st.write("Selamat Ulang Tahun")
st.text("21 Juli")
if st.button("OK"):
    st.write('Semoga sehat selalu')
    st.balloons()

A = st.checkbox("Terima kasih banyak untuk semuanya")
if A:
    st.write('Thanks from Choirul Anam Firman Thohari')

B = st.radio(
    'Apa lagu kesukaanmu?',
    ("POP", "ROCK", "KOPLO"))
if B == 'POP':
    st.write('Kamu pilih POP')
if B == 'ROCK':
    st.write('Kamu pilih ROCK')
if B == 'KOPLO':
    st.write('Kamu pilih KOPLO')


st.image('DLPH.jpg')





