import streamlit as st

# 페이지 제목 설정
st.title(" 오늘밤은 걸스나잇 뭐먹을지 골라!")
st.subheader("오늘 야식 메뉴 고르기")

st.write("---")

# 1. 라디오 버튼을 이용한 단일 선택 문항
choice = st.radio(
    "메뉴를 선택해주세요 👇",
    ["🌶️ 매콤함의 끝판왕, 엽떡!", "🍜 알싸한 중독성, 마라탕!"],
    index=None, # 처음에 아무것도 선택 안 된 상태로 만들기
    placeholder="메뉴를 골라보세요..."
)

st.write("---")

# 2. 사용자의 선택에 따른 결과 보여주기
if choice:
    if "엽떡" in choice:
        st.success("오늘 야식은 엽떡에 허니콤보 조합 각..")
    elif "마라탕" in choice:
        st.info("꿔바로우는 선택이 아닌 필수!")
else:
    st.warning("아직 메뉴를 고르지 않으셨어요. 신중하게 골라보세요!")
