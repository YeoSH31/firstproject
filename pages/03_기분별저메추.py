import streamlit as st

# -----------------------------------------------
# 2025 © Streamlit Pasta Recommender 🍝🎈
#   · 오늘 기분 선택 → 파스타/음식 추천
#   · Pure Streamlit, no extra libs
# -----------------------------------------------

st.set_page_config(page_title="🍝 기분별 파스타 추천", page_icon="🎈")

st.title("🎈 오늘의 기분으로 고르는 파스타 🍝")
st.caption("감정에 어울리는 따끈한 파스타 한 그릇을 추천해 드려요!")

# 기분 리스트
feelings = [
    "행복해요 😊", "피곤해요 😪", "설레요 💓", "우울해요 😔", "집중하고 싶어요 🎯", "새로운 게 먹고 싶어요 🌟", "편안함을 느끼고 싶어요 🛋️", "열정 넘쳐요 🔥"
]

# 추천 사전
recommendations = {
    "행복해요 😊": ["라구 파파르델레", "토마토 바질 스파게티"],
    "피곤해요 😪": ["양송이 크림 리소토", "까르보나라"],
    "설레요 💓": ["봉골레 스파게티", "새우 로제 파스타"],
    "우울해요 😔": ["볼로네즈 라자냐", "치킨 알프레도"],
    "집중하고 싶어요 🎯": ["알리오 올리오", "시금치 페스토 펜네"],
    "새로운 게 먹고 싶어요 🌟": ["오징어 먹물 링귀니", "트러플 마카로니"],
    "편안함을 느끼고 싶어요 🛋️": ["버터 파르미자나 뇨끼", "미네스트로네 수프 & 파르펠레"],
    "열정 넘쳐요 🔥": ["아라비아타 펜네", "디아볼라 스파게티"]
}

# 사용자 인터랙션
feeling_choice = st.selectbox("오늘 기분은 어떤가요?", feelings)

if feeling_choice:
    st.markdown("---")
    st.subheader("🍽️ 추천 메뉴")
    menu = recommendations.get(feeling_choice, ["오늘은 원하는 음식을 자유롭게 즐겨보세요!"])
    for dish in menu:
        st.write(f"🍝 {dish}")
    st.balloons()

st.markdown("""<hr style='border:1px solid #f0f0f0'>
<div style='text-align:center'>
    <small>ⓘ 추천 메뉴는 예시입니다. 기호에 맞게 변형해 보세요!</small>
</div>
""", unsafe_allow_html=True)
