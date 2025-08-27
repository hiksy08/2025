import random
import time
import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(
    page_title="📚 반짝반짝 랜덤 북픽",
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
  -webkit-text-fill-color: transparent;
}
.floaty {
  display: inline-block;
  animation: float 3s ease-in-out infinite;
}
@keyframes float {
  0%   { transform: translateY(0px) rotate(0deg); }
  50%  { transform: translateY(-6px) rotate(2deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}
.chip {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.06);
  margin-right: 8px;
  font-size: 12px;
}
.small {
  font-size: 13px;
  opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- 데이터 ----------------------
BOOKS = {
    "문학 📖": [
        {"title": "백년의 고독", "mood": "마법적 사실주의의 몽환 ✨", "why": "현실과 환상이 어우러진 대서사"},
        {"title": "죄와 벌", "mood": "양심과 구원의 심연 🌓", "why": "인간 내면을 파고드는 심리 드라마"},
        {"title": "데미안", "mood": "자아 찾기의 여정 🌱", "why": "성장과 각성의 상징"},
        {"title": "1984", "mood": "디스토피아의 경고 🚨", "why": "감시와 자유에 대한 질문"}
    ],
    "인문 🧠": [
        {"title": "사피엔스", "mood": "인류의 거대한 서사 🌍", "why": "우리가 어떻게 지금의 우리가 되었는가"},
        {"title": "공정하다는 착각", "mood": "정의에 대한 토론 🗣️", "why": "능력주의와 공정성의 경계"},
        {"title": "생각의 지도", "mood": "문화와 인지의 교차로 🧭", "why": "서양/동양 사고방식의 차이"},
        {"title": "국가란 무엇인가", "mood": "정치철학 입문 🚪", "why": "국가와 시민의 역할"}
    ],
    "과학 🔬": [
        {"title": "코스모스", "mood": "우주를 산책하는 밤 🌌", "why": "과학의 경이와 인문학적 울림"},
        {"title": "시간의 역사", "mood": "블랙홀과 시간 여행 ⏳", "why": "우주의 기원을 이해하는 즐거움"},
        {"title": "이기적 유전자", "mood": "진화의 시선 🧬", "why": "유전자 중심의 생명 전략"},
        {"title": "팩트풀니스", "mood": "세상을 보는 데이터 안경 📈", "why": "오해를 걷어내는 통계적 시각"}
    ],
    "역사 🏛️": [
        {"title": "총, 균, 쇠", "mood": "문명의 불평등 해부 🧩", "why": "지리와 환경이 만든 역사"},
        {"title": "사기", "mood": "인물로 읽는 대중사 👤", "why": "흥미로운 고대 중국사의 보고"},
        {"title": "로마인 이야기 1", "mood": "제국의 시작 🦅", "why": "로마의 성장 동력"},
        {"title": "역사의 쓸모", "mood": "일상에서 쓰는 역사 🧰", "why": "현재를 읽는 역사적 관점"}
    ],
    "보건 🩺": [
        {"title": "왜 우리는 병에 걸리는가", "mood": "진화와 질병의 역학 🧪", "why": "몸의 취약성 이해"},
        {"title": "음식 혁명", "mood": "식생활 리부트 🥗", "why": "건강한 식습관의 힘"},
        {"title": "면역에 관하여", "mood": "몸의 수호자들 🛡️", "why": "면역 시스템 알기"},
        {"title": "공중보건의 눈으로 본 세상", "mood": "사회와 건강의 링크 🌐", "why": "개인의 건강을 넘는 시야"}
    ],
    "미술 🎨": [
        {"title": "서양 미술사", "mood": "명작으로 걷는 타임라인 🖼️", "why": "미술 흐름을 한눈에"},
        {"title": "칸딘스키, 예술에서의 정신적인 것", "mood": "색과 형태의 언어 🔺", "why": "추상미술의 선언"},
        {"title": "색채의 역사", "mood": "색의 문화사 🌈", "why": "색이 바꾼 미감과 권력"},
        {"title": "그림으로 보는 미술사", "mood": "비주얼 압도 📚", "why": "이미지로 읽는 교양"}
    ],
    "음악 🎵": [
        {"title": "서양 음악사", "mood": "중세부터 현대까지 🎼", "why": "장르와 양식의 진화"},
        {"title": "클래식, 나의 첫 안내서", "mood": "입문자 맞춤 길잡이 🚪", "why": "작곡가와 곡 친해지기"},
        {"title": "재즈의 역사", "mood": "즉흥과 스윙의 계보 🎷", "why": "자유와 창의의 사운드"},
        {"title": "리듬의 과학", "mood": "비트의 비밀 🥁", "why": "몸이 반응하는 이유"}
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
  <p style="margin-top:10px;">💡 <b>분위기</b>: {candidate['mood']}</p>
  <p>🌟 <b>추천 이유</b>: {candidate['why']}</p>
</div>
""", unsafe_allow_html=True)

# ---------------------- 푸터 ----------------------
st.write("")
st.markdown('<div class="small">made with ❤️ streamlit · 이모지 파티 🎉</div>', unsafe_allow_html=True)

  
 
  
