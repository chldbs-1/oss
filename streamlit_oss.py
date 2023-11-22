import streamlit as st

# OSS 중간 시험 결과
OSS_Score = [80, 70, 55, 30, 3, 3, 1, 0]

st.write("#23114156")
st.write("## 컴퓨터소프트웨어학부")
st.write("### 문승목")

OSS_Score

st.area_chart(OSS_Score)