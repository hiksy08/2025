import random
import time
import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(
    page_title="📚 랜덤 책 추천기",
    page_icon="📚",
    layout="wide",
)

# ---------------------- 스타일 ----------------------
st.markdown("""
<style>
.main, .block-container {
  background: radial-gradient(circle at 10% 20%, #fef3c7 0%, #fde68a 15%, #f5d0fe 35%, #c7d2fe 60%, #a7f3d0 100%) !important;
}
.card {
  backdrop-filter: blur(10px);
  background: rgba(255,255,255,0.55);
  border: 1px solid rgba(255,255,255,0.5);
  border-radius: 22px;
  padding: 18px 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}
.sparkle {
  font-size: 38px;
  font-weight: 800;
  background: linear-gradient(90deg, #7c3aed, #2563eb, #059669, #f59e0b, #db2777);
  -webkit-background-clip: text;
  -webkit-text-fill-color로", "summary": "정체 모를 바이러스가 전 세계를 뒤덮고 듣지도 말하지도 못하는 동생 미소를 지키며 맨몸으로 러시아를 걸어 온 도리는 일가친척과 함께 탑차를 타고 세계를 떠돌던 지나와 만나데 되어 일어나는 일을 담은 소설이다."}
    ],
    "인문 🧠": [
        {"title": "사피엔스", "summary": "호모 사피엔스가 인류 문명의 주체가 되기까지의 과정을 탐구하는 역사 인문서."},
        {"title": "공정하다는 착각", "summary": "능력주의와 공정성의 이면을 분석하며 현대 사회 불평등 문제를 다룬 책."},
        {"title": "생각의 지도", "summary": "동양과 서양의 문화적 차이가 사고방식에 어떻게 반영되는지를 설명하는 연구서."},
        {"title": "국가란 무엇인가", "summary": "국가의 본질과 기능, 그리고 시민의 역할을 철학적으로 고찰한 책."}
    ],
    "과학 🔬": [
        {"title": "코스모스", "summary": "칼 세이건이 우주의 탄생과 과학적 탐구의 역사를 대중적으로 설명한 명저."},
        {"title": "시간의 역사", "summary": "스티븐 호킹이 시간, 우주, 블랙홀 등 현대 물리학의 핵심을 쉽게 풀어낸 책."},
        {"title": "이기적 유전자", "summary": "리처드 도킨스가 유전자 중심으로 진화의 과정을 설명한 과학 고전."},
        {"title": "팩트풀니스", "summary": "세계에 대한 잘못된 인식을 통계와 데이터로 바로잡는 시각을 제시하는 책."}
    ],
    "역사 🏛️": [
        {"title": "총, 균, 쇠", "summary": "지리적 요인과 환경이 문명의 발달과 불평등을 만든 과정을 탐구."},
        {"title": "사기", "summary": "사마천이 집필한 중국의 역사서로, 인물 중심으로 기록된 방대한 이야기."},
        {"title": "로마인 이야기 1", "summary": "로마 제국의 기원과 발전을 흥미롭게 서술한 역사 교양서."},
        {"title": "역사의 쓸모", "summary": "역사를 통해 현재의 문제를 이해하고 해결의 단서를 찾을 수 있음을 보여주는 책."}
    ],
    "보건 🩺": [
        {"title": "왜 우리는 병에 걸리는가", "summary": "진화의 관점에서 인간이 질병에 취약한 이유를 설명한 책."},
        {"title": "음식 혁명", "summary": "잘못된 식습관이 건강에 미치는 영향을 짚고 올바른 식생활을 제안한다."},
        {"title": "면역에 관하여", "summary": "우리 몸의 면역 체계를 알기 쉽게 소개하며 건강과의 관계를 설명한다."},
        {"title": "공중보건의 눈으로 본 세상", "summary": "공중보건의 시각에서 개인과 사회의 건강 문제를 다룬 책."}
    ],
    "미술 🎨": [
        {"title": "서양 미술사", "summary": "고대부터 현대까지 서양 미술의 흐름을 정리한 교양서."},
        {"title": "칸딘스키, 예술에서의 정신적인 것", "summary": "추상미술의 창시자가 예술의 본질과 정신적 가치를 논한 책."},
        {"title": "색채의 역사", "summary": "인류 문화 속에서 색이 지닌 의미와 변천사를 다룬 책."},
        {"title": "그림으로 보는 미술사", "summary": "풍부한 이미지와 함께 미술사를 쉽게 풀어낸 교양서."}
    ],
    "음악 🎵": [
        {"title": "서양 음악사", "summary": "중세부터 현대까지 음악사의 큰 흐름을 정리한 교양서."},
        {"title": "클래식, 나의 첫 안내서", "summary": "클래식 음악 입문자를 위해 작곡가와 작품을 소개한다."},
        {"title": "재즈의 역사", "summary": "재즈 음악의 기원과 발전 과정을 탐구한 책."},
        {"title": "리듬의 과학", "summary": "인간이 리듬에 반응하는 원리를 과학적으로 설명한다."}
    ],
}

CATEGORY_EMOJIS = {
    "문학 📖": "📖✨",
    "인문 🧠": "🧠🌟",
    "과학 🔬": "🔬🌌",
    "역사 🏛️": "🏛️📜",
    "보건 🩺": "🩺💚",
    "미술 🎨": "🎨🌈",
    "음악 🎵": "🎵🎧",
}

# ---------------------- 헤더 ----------------------
st.markdown('<div class="sparkle">📚 반짝반짝 랜덤 북픽 <span class="floaty">✨</span><span class="floaty">🌟</span><span class="floaty">💫</span></div>', unsafe_allow_html=True)
st.write("장르를 고르면 자동으로 **랜덤 추천** 책이 나타나요! 운명의 한 권을 만나보세요 🔮")

# ---------------------- 선택 ----------------------
selected = st.selectbox("🎯 **추천 받을 장르를 선택하세요**", list(BOOKS.keys()), index=0)

# ---------------------- 랜덤 추천 ----------------------
candidate = random.choice(BOOKS[selected])
st.balloons()

with st.spinner("반짝이는 추천을 준비 중... ✨"):
    time.sleep(1.2)

# ---------------------- 추천 결과 카드 ----------------------
st.markdown(f"""
<div class="card">
  <div class="chip">오늘의 픽</div>
  <h2 style="margin:6px 0;">{CATEGORY_EMOJIS.get(selected,'📚')} <b>{candidate['title']}</b></h2>
  <div class="small">장르: {selected}</div>
  <p style="margin-top:10px;">📖 <b>줄거리</b>: {candidate['summary']}</p>
</div>
""", unsafe_allow_html=True)

# ---------------------- 푸터 ----------------------
st.write("")
st.markdown('<div class="small">made with ❤️ streamlit · 이모지 파티 🎉</div>', unsafe_allow_html=True)


