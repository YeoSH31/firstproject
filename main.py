import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 영화 추천 🎬", page_icon="🎈")

# 제목과 설명
st.title("🎉 MBTI로 찾는 과학·수학 명작 영화 🎬")
st.caption("MBTI를 고르면 해당 성향과 잘 어울릴 만한 수학·과학 명작 영화를 추천해 드려요! 🚀")

# MBTI 선택 옵션
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_choice = st.selectbox("당신의 MBTI를 선택하세요 😊", mbti_types)

# MBTI별 추천 영화 딕셔너리
recommendations = {
    "INTJ": ["A Beautiful Mind (2001)", "Interstellar (2014)", "The Imitation Game (2014)"],
    "INTP": ["Pi (1998)", "Primer (2004)", "The Man Who Knew Infinity (2015)"],
    "ENTJ": ["Hidden Figures (2016)", "The Martian (2015)", "Apollo 13 (1995)"],
    "ENTP": ["Ex Machina (2014)", "Good Will Hunting (1997)", "The Social Network (2010)"],
    "INFJ": ["The Theory of Everything (2014)", "Contact (1997)", "Gattaca (1997)"],
    "INFP": ["Contact (1997)", "October Sky (1999)", "Gattaca (1997)"],
    "ENFJ": ["The Theory of Everything (2014)", "Hidden Figures (2016)", "The Martian (2015)"],
    "ENFP": ["Back to the Future (1985)", "The Martian (2015)", "October Sky (1999)"],
    "ISTJ": ["A Beautiful Mind (2001)", "Apollo 13 (1995)", "The Man Who Knew Infinity (2015)"],
    "ISFJ": ["Hidden Figures (2016)", "The Theory of Everything (2014)", "October Sky (1999)"],
    "ESTJ": ["Apollo 13 (1995)", "Gattaca (1997)", "Hidden Figures (2016)"],
    "ESFJ": ["The Martian (2015)", "October Sky (1999)", "Hidden Figures (2016)"],
    "ISTP": ["Primer (2004)", "The Martian (2015)", "Apollo 13 (1995)"],
    "ISFP": ["October Sky (1999)", "Gattaca (1997)", "Contact (1997)"],
    "ESTP": ["Interstellar (2014)", "The Martian (2015)", "Back to the Future (1985)"],
    "ESFP": ["Back to the Future (1985)", "The Martian (2015)", "October Sky (1999)"]
}

# MBTI 선택 시 결과 출력
if mbti_choice:
    st.subheader(f"🌟 {mbti_choice} 맞춤 추천 영화 목록 🌟")
    for movie in recommendations.get(mbti_choice, []):
        st.write(f"🎥 {movie}")
    st.balloons()
