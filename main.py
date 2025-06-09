import streamlit as st

# -----------------------------
# 2022 개정 교육과정 과목 추천기
# -----------------------------

st.set_page_config(page_title="🎓 과목 추천기", page_icon="📚")

st.title("🚀 희망 전공 맞춤 고교 과목 추천")
st.caption("2022 개정 교육과정 일반·진로·융합 선택 과목을 한눈에! ✨")

# -----------------------------
# 데이터 섹션
# -----------------------------

# 전공 키워드 사전
major_keywords = {
    "humanities": [
        "국어", "문학", "철학", "사학", "역사", "신학", "언어", "고전", "문화"
    ],
    "social": [
        "경제", "경영", "행정", "정치", "사회", "심리", "커뮤니케이션", "미디어", "관광", "광고", "회계", "무역"
    ],
    "natural": [
        "수학", "물리", "화학", "생명", "생물", "지구", "통계", "해양", "식품", "환경", "천문"
    ],
    "engineering": [
        "컴퓨터", "소프트웨어", "전기", "전자", "기계", "토목", "건축", "화학공학", "재료", "산업", "항공", "자동차", "AI", "로봇"
    ],
    "arts": [
        "음악", "미술", "디자인", "체육", "무용", "연극", "영화", "패션", "콘텐츠", "예술"
    ]
}

# 카테고리 한글명
category_korean = {
    "humanities": "인문계열",
    "social": "사회계열",
    "natural": "자연계열",
    "engineering": "공학계열",
    "arts": "예체능계열"
}

# 과목 추천 사전
recommendations = {
    "humanities": {
        "general": [
            "언어와 매체", "화법과 작문", "문학", "한국사", "세계사", "세계지리", "사회문화"
        ],
        "career": [
            "고전읽기", "한국문학과 매체탐구", "심리학과 사회문화", "논리학", "철학"
        ],
        "fusion": [
            "융합논리", "디지털인문지리", "융합사회문제탐구"
        ]
    },
    "social": {
        "general": [
            "경제", "정치와 법", "사회문화", "한국지리", "동아시아사"
        ],
        "career": [
            "국제관계학개론", "경제심화", "빅데이터 기초", "소비자경제", "사회문제탐구"
        ],
        "fusion": [
            "데이터과학", "융합사회문제탐구", "AI 수학"
        ]
    },
    "natural": {
        "general": [
            "수학Ⅰ", "수학Ⅱ", "미적분", "기하", "물리학Ⅰ", "화학Ⅰ", "생명과학Ⅰ", "지구과학Ⅰ"
        ],
        "career": [
            "물리학Ⅱ", "화학Ⅱ", "생명과학Ⅱ", "지구과학Ⅱ", "환경과학", "수학탐구실험", "통계심화", "AI 수학"
        ],
        "fusion": [
            "융합과학", "과학사 및 과학철학", "데이터과학"
        ]
    },
    "engineering": {
        "general": [
            "수학Ⅰ", "수학Ⅱ", "미적분", "기하", "물리학Ⅰ", "화학Ⅰ"
        ],
        "career": [
            "물리학Ⅱ", "화학Ⅱ", "정보과학", "프로그래밍", "AI 수학", "융합과학"
        ],
        "fusion": [
            "데이터과학", "AI 프로그래밍", "융합과학"
        ]
    },
    "arts": {
        "general": [
            "음악", "미술", "체육", "생활과 과학"
        ],
        "career": [
            "음악실기", "미술전문실기", "연극영화", "무용", "스포츠과학", "패션디자인", "영상예술"
        ],
        "fusion": [
            "미디어아트", "문화콘텐츠제작", "융합예술과 테크"
        ]
    }
}

# -----------------------------
# 함수 정의
# -----------------------------

def infer_category(major_name: str):
    """전공명으로부터 계열을 추론한다."""
    name = major_name.strip().lower()
    for cat, keys in major_keywords.items():
        for kw in keys:
            if kw.lower() in name:
                return cat
    return None

# -----------------------------
# UI 인터랙션
# -----------------------------

major_input = st.text_input("🎯 희망 전공(학과)을 입력하세요", placeholder="예: 화학공학, 심리학, 영화학 ...")

if st.button("과목 추천 받기 🎁"):
    if not major_input.strip():
        st.error("학과를 입력해 주세요! 😊")
    else:
        category = infer_category(major_input)
        if category is None:
            st.warning("아직 데이터가 부족해 해당 학과를 분류하지 못했어요. 🤔\n비슷한 학과명으로 다시 시도해 주세요.")
        else:
            subj_set = recommendations[category]
            st.success(f"{major_input} → {category_korean[category]} 전공으로 분류되었습니다! 🌟")

            st.markdown("""---""")
            st.subheader("📖 일반 선택 과목")
            for sub in subj_set["general"]:
                st.write(f"• {sub}")

            st.subheader("🛠️ 진로 선택 과목")
            for sub in subj_set["career"]:
                st.write(f"• {sub}")

            st.subheader("🔗 융합 선택 과목")
            for sub in subj_set["fusion"]:
                st.write(f"• {sub}")

            st.balloons()

st.markdown("""
<div style='text-align:center'>
    <small>📚 추천 과목은 참고용입니다. 실제 개설 여부는 학교·교육청에 따라 달라질 수 있어요!</small>
</div>
""", unsafe_allow_html=True)
