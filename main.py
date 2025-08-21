import streamlit as st

# 🌈 웹앱 기본 설정
st.set_page_config(page_title="MBTI 진로 추천기 💼✨", page_icon="💡", layout="centered")

# 🎨 헤더
st.title("🌟 MBTI 기반 진로 추천 사이트 🌟")
st.markdown("""
## 💖 당신의 MBTI에 맞는 최고의 직업을 찾아드립니다! 💼🚀
👉 MBTI를 선택하면 찰떡같은 직업을 추천해드려요 ✨
""")

# MBTI 선택 옵션
types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("🔮 당신의 MBTI를 선택하세요:", types)

# MBTI별 직업 추천 데이터베이스
mbti_jobs = {
    "ISTJ": ["👮 경찰", "📊 회계사", "⚖️ 판사"],
    "ISFJ": ["👩‍⚕️ 간호사", "🍳 요리사", "📚 교사"],
    "INFJ": ["🎨 예술가", "🧑‍🏫 상담가", "✍️ 작가"],
    "INTJ": ["💻 프로그래머", "📈 전략가", "🧑‍🔬 과학자"],
    "ISTP": ["🔧 엔지니어", "🚗 정비사", "🏍️ 파일럿"],
    "ISFP": ["🎶 음악가", "🎨 디자이너", "🌿 환경운동가"],
    "INFP": ["📖 작가", "🧑‍🎨 일러스트레이터", "🎤 가수"],
    "INTP": ["🧪 연구원", "💡 발명가", "📊 데이터 분석가"],
    "ESTP": ["🏀 운동선수", "💼 사업가", "🎬 배우"],
    "ESFP": ["🎤 엔터테이너", "🎶 가수", "🎭 배우"],
    "ENFP": ["🌍 여행작가", "🗣️ 강연가", "🎨 크리에이터"],
    "ENTP": ["🚀 스타트업 창업가", "🎤 방송인", "💡 혁신가"],
    "ESTJ": ["📊 관리자", "⚖️ 판사", "🏢 기업 임원"],
    "ESFJ": ["👩‍🏫 교사", "🧑‍🍳 요리사", "🤝 사회복지사"],
    "ENFJ": ["🧑‍🏫 교육자", "🎤 연설가", "📚 작가"],
    "ENTJ": ["🏦 CEO", "📈 투자자", "⚔️ 정치가"]
}

# 버튼 클릭 시 결과 출력
if st.button("✨ 나의 추천 직업 보기 ✨"):
    jobs = mbti_jobs.get(mbti, ["🤔 데이터 없음"])
    st.subheader(f"💡 {mbti} 유형 추천 직업은...")
    for job in jobs:
        st.success(f"{job} 🏆")

    st.balloons()  # 🎈 풍선 애니메이션
