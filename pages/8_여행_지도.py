import streamlit as st

# 페이지 제목 설정
st.title(" 오늘밤은 걸스나잇 뭐먹을지 골라!")
st.subheader("오늘 야식 메뉴 고르기")

st.write("---")

# index=None과 placeholder를 제거하고 기본값(0번째 항목)으로 설정
choice = st.radio(
    "메뉴를 선택해주세요 👇",
    ["매콤함의 끝판왕, 엽떡!", "알싸한 중독성, 마라탕!"]
)

st.write("---")



name = st.text_input('또 먹고 싶은 거 없어? : ')
menu = st.selectbox('뭐하고 싶어?:', ['보드게임','수다 떨기','아이돌 직캠 시청','공포영화 보기','산책하기'])
