import random
import streamlit as st

# -------------------------
# 🎨 페이지 기본 설정
# -------------------------
st.set_page_config(
    page_title="📚 북 피커",
    page_icon="📚",
    layout="wide",
)

# -------------------------
# 📚 데이터: 카테고리별 추천
# -------------------------
BOOKS = {
    "문학": {
        "emoji": "✨📖🌙",
        "title": "어린 왕자",
        "author": "앙투안 드 생텍쥐페리",
    },
    "인문": {
        "emoji": "🧠🌍🔍",
        "title": "정의란 무엇인가",
        "author": "마이클 샌델",
    },
    "과학": {
        "emoji": "🔭🌌🧬",
        "title": "코스모스",
        "author": "칼 세이건",
    },
    "역사": {
        "emoji": "🏺📜🌐",
        "title": "사피엔스",
        "author": "유발 하라리",
    },
    "보건": {
        "emoji": "💪🩺🧠",
        "title": "바디: 우리 몸 안내서",
        "author": "빌 브라이슨",
    },
    "미술": {
        "emoji": "🎨🖼️🌟",
        "title": "서양 미술사",
        "author": "E.H. 곰브리치",
    },
    "음악": {
        "emoji": "🎵🎻🎹",
        "title": "이야기로 읽는 서양음악사",
        "author": "안인모",
    },
}

CATEGORIES = list(BOOKS.keys())

# -------------------------
# 🎉 헤더
# -------------------------
st.markdown("<h1>📚 북 피커 ✨</h1>", unsafe_allow_html=True)
st.write("👉 카테고리를 선택하면 책을 추천해드려요!")

# -------------------------
# 🧩 선택
# -------------------------
selected = st.selectbox("책 종류를 선택하세요 🎨", CATEGORIES)

# -------------------------
# 🎲 랜덤 버튼
# -------------------------
if st.button("🎲 랜덤 추천"):
    selected = random.choice(CATEGORIES)
    st.success(f"오늘의 랜덤 카테고리는 **{selected}** 🎉")

# -------------------------
# 🪄 추천 결과
# -------------------------
if selected:
    data = BOOKS[selected]
    st.markdown("---")
    st.subheader(f"{data['emoji']} {selected}")
    st.write(f"📕 **{data['title']}**")
    st.write(f"✍️ {data['author']}")

