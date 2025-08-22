# app.py
import random
import streamlit as st

# ----------------------------
# 페이지 기본 설정
# ----------------------------
st.set_page_config(
    page_title="📚 진로교육 책 추천기",
    page_icon="📚",
    layout="wide",
)

# ----------------------------
# 스타일
# ----------------------------
CUSTOM_CSS = """
<style>
.stApp {
  background: linear-gradient(135deg, #f7e8ff 0%, #e6f7ff 30%, #fff6e6 60%, #f8ffe6 100%);
}
h1 .sparkle {
  animation: shine 2s infinite linear;
  background: linear-gradient(90deg,#ff7eb3,#ffd86f,#a6ffcb);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
@keyframes shine {
  0% { filter: drop-shadow(0 0 0px rgba(255,255,255,0.5)); }
  50% { filter: drop-shadow(0 0 8px rgba(255,255,255,0.8)); }
  100% { filter: drop-shadow(0 0 0px rgba(255,255,255,0.5)); }
}
.glass {
  background: rgba(255,255,255,0.55);
  border-radius: 24px;
  padding: 26px;
  border: 1px solid rgba(255,255,255,0.45);
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  backdrop-filter: saturate(160%) blur(10px);
}
.badge { font-size: 48px; line-height: 1; }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ----------------------------
# 카테고리별 책 추천 데이터
# ----------------------------
BOOKS = {
    "문학": {
        "emoji": "📖",
        "title": "데미안",
        "author": "헤르만 헤세",
        "why": "자아 탐색과 성장에 관한 고전으로, 자신의 정체성을 찾는 데 도움을 줍니다.",
        "insight": "내면의 목소리를 따르는 용기가 진정한 성장을 이끈다.",
        "paths": ["작가", "문예창작", "출판"],
    },
    "인문": {
        "emoji": "🏛️",
        "title": "정의란 무엇인가",
        "author": "마이클 샌델",
        "why": "사회와 삶의 여러 문제를 비판적으로 바라보는 인문적 사고를 길러줍니다.",
        "insight": "정의는 단순한 답이 아니라, 함께 논의하며 찾는 과정이다.",
        "paths": ["철학", "정치학", "교육"],
    },
    "과학": {
        "emoji": "🔬",
        "title": "코스모스",
        "author": "칼 세이건",
        "why": "우주와 과학의 아름다움을 탐구하며 과학적 호기심을 키워줍니다.",
        "insight": "작은 지구에서 우리가 할 수 있는 선택이 우주의 의미를 만든다.",
        "paths": ["천문학자", "물리학자", "연구원"],
    },
    "역사": {
        "emoji": "📜",
        "title": "사피엔스",
        "author": "유발 하라리",
        "why": "인류의 역사와 문명을 통찰하며 현재와 미래를 바라보는 시각을 길러줍니다.",
        "insight": "과거를 이해하는 것이 미래를 준비하는 힘이 된다.",
        "paths": ["역사가", "교사", "정책분석가"],
    },
    "보건": {
        "emoji": "🩺",
        "title": "나는 의사다",
        "author": "의학 드라마 사례집",
        "why": "의료 현장의 실제 사례를 통해 보건·의료 진로에 대한 생생한 시각을 제공합니다.",
        "insight": "치유는 지식뿐 아니라 공감에서 시작된다.",
        "paths": ["의사", "간호사", "보건교사"],
    },
    "미술": {
        "emoji": "🎨",
        "title": "이것이 현대미술이다",
        "author": "윌 곰퍼츠",
        "why": "현대 미술의 흐름을 알기 쉽게 설명해 창의적 진로 탐색에 도움을 줍니다.",
        "insight": "예술은 세상을 새롭게 보는 또 다른 언어다.",
        "paths": ["화가", "큐레이터", "디자이너"],
    },
    "음악": {
        "emoji": "🎶",
        "title": "베토벤 바이러스",
        "author": "이재규",
        "why": "음악의 힘과 예술가의 열정을 보여주며 음악 진로에 대한 영감을 줍니다.",
        "insight": "음악은 사람의 마음을 움직이는 가장 순수한 힘이다.",
        "paths": ["작곡가", "연주자", "음악교사"],
    },
}

CATEGORIES = list(BOOKS.keys())

# ----------------------------
# 헤더
# ----------------------------
st.markdown(
    f"""
    <h1>📚 <span class="sparkle">진로교육 책 추천기</span> ✨</h1>
    <p class="badge">📖🏛️🔬📜🩺🎨🎶</p>
    """,
    unsafe_allow_html=True,
)
st.write("원하는 분야를 선택하면 해당 분야에 어울리는 **책 한 권**을 추천해드려요! 🌟")

# ----------------------------
# 선택 & 추천
# ----------------------------
col1, col2 = st.columns([1.2,1])
with col1:
    cat = st.selectbox("📂 책 종류를 골라주세요", CATEGORIES)
    fire = st.button("🎁 책 추천 받기", use_container_width=True)

if fire:
    data = BOOKS[cat]
    st.balloons()
    st.markdown(
        f"""
        <div class="glass">
          <div style="text-align:center" class="badge">{data['emoji']}</div>
          <h3>{data['title']}</h3>
          <p><b>저자:</b> {data['author']}</p>
          <hr>
          <p>💡 <b>추천 이유:</b> {data['why']}</p>
          <p>✨ <b>한 줄 인사이트:</b> {data['insight']}</p>
          <p>🧭 <b>관련 진로:</b> {", ".join(data['paths'])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

