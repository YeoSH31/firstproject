import streamlit as st

# -------------------------------------------------
# MBTI x The Black Skirts Track Recommender 🎸🎈
# -------------------------------------------------

st.set_page_config(page_title="🎸 MBTI x 검정치마", page_icon="🎈")

st.title("🎈 MBTI로 찾는 검정치마 트랙 추천 🎧")
st.caption("당신의 성격 유형에 어울리는 \U0001F452검정치마 노래를 만나보세요!")

# MBTI 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 입력
mbti_choice = st.selectbox("당신의 MBTI를 선택하세요 😊", mbti_types)

# 트랙 데이터 (분위기별)
track_by_mood = {
    "bright": [
        "Love Shine", "Confetti and Balloons", "Powder Blue", "Stand Still", "Flying Bobs", "Love Is All", "Follow You", "Freeloader"
    ],
    "calm": [
        "International Love Song", "In My City of Seoul", "Sunday Girl", "Puppy", "Jersey Girl", "Breakfast", "My Little Lambs"
    ],
    "dreamy": [
        "Antifreeze", "Diamond", "Garden State Dreamers", "That's Not Me", "Love You The Same"
    ],
    "dark": [
        "Who Do You Love", "Wrong Question", "Island (Queen of Diamonds)", "Baptized In Fire", "Lester Burnham", "Cicadas"
    ]
}

# MBTI -> 분위기 매핑
mbti_to_mood = {
    "ENFP": "bright", "ENFJ": "bright", "ESFP": "bright", "ESFJ": "bright", "ENTP": "bright", "ESTP": "bright", "ESTJ": "bright",
    "ISFP": "calm", "ISFJ": "calm", "INFP": "calm", "INFJ": "calm", "ISTJ": "calm",
    "INTP": "dreamy", "INTJ": "dreamy",
    "ENTJ": "dark", "ISTP": "dark"
}

# 추천 출력
if mbti_choice:
    mood = mbti_to_mood.get(mbti_choice, "bright")
    st.subheader(f"🌟 {mbti_choice} — {mood.capitalize()} Mood 추천 트랙 🌟")
    for song in track_by_mood[mood]:
        st.write(f"🎵 {song}")
    st.balloons()

st.markdown("""<hr style='border:1px solid #f0f0f0'>
<div style='text-align:center'>
    <small>ⓘ 추천 결과는 개인적 감상 기준으로 제작되었습니다. 즐겁게 감상해 주세요! 🎶</small>
</div>
""", unsafe_allow_html=True)
