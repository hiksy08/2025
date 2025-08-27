import random
import time
import streamlit as st

# ---------------------- 기본 설정 ----------------------
st.set_page_config(
    page_title="📚 반짝반짝 랜덤 북픽",
    page_icon="📚",
    layout="wide",
)

# ---------------------- 스타일 (화려하게!) ----------------------
st.markdown("""
<style>
/* 배경 그Radient */
.main, .block-container {
  background: radial-gradient(circle at 10% 20%, #fef3c7 0%, #fde68a 15%, #f5d0fe 35%, #c7d2fe 60%, #a7f3d0 100%) !important;
}

/* 유리카드 느낌 */
.card {
  backdrop-filter: blur(10px);
  background: rgba(255,255,255,0.55);
  border: 1px solid rgba(255,255,255,0.5);
  border-radius: 22px;
  padding: 18px 20px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
}

/* 반짝이는 헤더 */
.sparkle {
  font-size: 38px;
  font-weight: 800;
  background: linear-gradient(90deg, #7c3aed, #2563eb, #059669, #f59e0b, #db2777);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

/* 둥둥 떠다니는 이모지 */
.floaty {
  display: inline-block;
  animation: float 3s ease-in-out infinite;
}
@keyframes float {
  0%   { transform: translateY(0px) rotate(0deg); }
  50%  { transform: translateY(-6px) rotate(2deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}

/* 칩 스타일 태그 */
.chip {
  display: inline-block;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.06);
  margin-right: 8px;
  font-size: 12px;
}

/* 버튼 줄 간격 조금 */
.block-container .stButton>button {
  border-radius: 14px;
  padding: 10px 16px;
  font-weight: 700;
  border: 2px solid rgba(0,0,0,0.08);
  box-shadow: 0 6px 18px rgba(0,0,0,0.06);
}

.small {
  font-size: 13px;
  opacity: 0.8;
}
</style>
""", unsafe_allow_html=True)

# ---------------------- 데이터 ----------------------
# 각 장르별 최대 4권 (설명은 가볍게, 저자정보는 생략)
BOOKS = {
    "문학 📖": [
        {"title": "백년의 고독", "mood": "마법적 사실주의의 몽환 ✨", "why": "현실과 환상이 어우러진 대서사로 몰입감 최고"},
        {"title": "죄와 벌", "mood": "양심과 구원의 심연 🌓", "why": "인간 내면을 끝까지 파고드는 심리 드라마"},
        {"title": "데미안", "mood": "자아 찾기의 여정 🌱", "why": "성장과 각성의 상징으로 가득한 소설"},
        {"title": "1984", "mood": "디스토피아의 경고 🚨", "why": "감시와 자유에 대한 날카로운 질문"}
    ],
    "인문 🧠": [
        {"title": "사피엔스", "mood": "인류의 거대한 서사 🌍", "why": "우리가 어떻게 지금의 우리가 되었는가"},
        {"title": "공정하다는 착각", "mood": "정의에 대한 토론 🗣️", "why": "능력주의와 공정성의 경계를 재고"},
        {"title": "생각의 지도", "mood": "문화와 인지의 교차로 🧭", "why": "서양/동양 사고방식의 차이를 탐구"},
        {"title": "국가란 무엇인가", "mood": "정치철학 입문 🚪", "why": "국가와 시민의 역할을 묻다"}
    ],
    "과학 🔬": [
        {"title": "코스모스", "mood": "우주를 산책하는 밤 🌌", "why": "과학의 경이와 인문학적 울림"},
        {"title": "시간의 역사", "mood": "블랙홀과 시간 여행 ⏳", "why": "우주의 기원을 이해하는 즐거움"},
        {"title": "이기적 유전자", "mood": "진화의 시선 🧬", "why": "유전자 중심으로 보는 생명의 전략"},
        {"title": "팩트풀니스", "mood": "세상을 보는 데이터 안경 📈", "why": "오해를 걷어내는 통계적 시각"}
    ],
    "역사 🏛️": [
        {"title": "총, 균, 쇠", "mood": "문명의 불평등을 해부 🧩", "why": "지리와 환경이 만든 역사"},
        {"title": "사기", "mood": "인물로 읽는 대중사 👤", "why": "흥미로운 고대 중국사의 보고"},
        {"title": "로마인 이야기 1", "mood": "제국의 시작 🦅", "why": "로마의 성장 동력을 생생히"},
        {"title": "역사의 쓸모", "mood": "일상에서 쓰는 역사 🧰", "why": "역사적 관점으로 현재를 읽다"}
    ],
    "보건 🩺": [
        {"title": "왜 우리는 병에 걸리는가", "mood": "진화와 질병의 역학 🧪", "why": "몸의 설계와 취약성 이해"},
        {"title": "음식 혁명", "mood": "식생활 리부트 🥗", "why": "건강한 식습관의 힘"},
        {"title": "면역에 관하여", "mood": "몸의 수호자들 🛡️", "why": "면역 시스템을 알면 건강이 보인다"},
        {"title": "공중보건의 눈으로 본 세상", "mood": "사회와 건강의 링크 🌐", "why": "개인의 건강을 넘는 시야"}
    ],
    "미술 🎨": [
        {"title": "서양 미술사", "mood": "명작으로 걷는 타임라인 🖼️", "why": "미술 흐름을 한눈에"},
        {"title": "칸딘스키, 예술에서의 정신적인 것", "mood": "색과 형태의 언어 🔺", "why": "추상미술의 선언"},
        {"title": "색채의 역사", "mood": "색의 문화사 🌈", "why": "색이 바꾼 미감과 권력"},
        {"title": "그림으로 보는 미술사", "mood": "비주얼 압도 📚", "why": "이미지로 술술 읽히는 교양"}
    ],
    "음악 🎵": [
        {"title": "서양 음악사", "mood": "중세부터 현대까지 🎼", "why": "장르와 양식의 진화"},
        {"title": "클래식, 나의 첫 안내서", "mood": "입문자 맞춤 길잡이 🚪", "why": "작곡가와 곡을 친해지는 법"},
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

ALL_CATEGORIES = list(BOOKS.keys())

# ---------------------- 헤더 ----------------------
st.markdown('<div class="sparkle">📚 반짝반짝 랜덤 북픽 <span class="floaty">✨</span> <span class="floaty">🌟</span> <span class="floaty">💫</span></div>', unsafe_allow_html=True)
st.write("장르를 고르고 **랜덤 추천** 버튼을 눌러보세요! 이모지 폭포수와 함께 오늘의 한 권을 선물해 드려요 🫶")

# ---------------------- 사이드바 ----------------------
with st.sidebar:
    st.markdown("### 🌈 옵션")
    st.markmarkdown = st.markdown
    st.markdown("원하는 장르를 고르고, 버튼을 누르면 해당 장르에서 무작위 추천을 드립니다.")
    fancy = st.toggle("화려함 x2 모드 ✨", value=True, help="배경/카드 효과를 더 강하게!")
    show_list = st.toggle("선택 장르의 모든 후보도 보기 👀", value=True)
    st.markdown("---")
    st.markdown("#### 📌 팁")
    st.caption("• 리스트에서 눈여겨본 책을 표시해 두고, 다시 뽑기하며 비교해 보세요!")

# ---------------------- 선택 영역 ----------------------
cols = st.columns([1, 1, 1, 1, 1, 1, 1])
for i, cat in enumerate(ALL_CATEGORIES):
    with cols[i]:
        st.markdown(f"<div class='card'><div class='chip'>장르</div><h5 style='margin:6px 0 0 0;'>{cat}</h5><div class='small'>{CATEGORY_EMOJIS.get(cat,'📚')}</div></div>", unsafe_allow_html=True)

st.write("")
selected = st.selectbox("🎯 **추천 받을 장르를 선택하세요**", ALL_CATEGORIES, index=0, help="장르당 최대 4권의 후보에서 랜덤으로 뽑아요!")

# ---------------------- 랜덤 추천 로직 ----------------------
if "history" not in st.session_state:
    st.session_state.history = []

c1, c2, c3 = st.columns([1.2, 1, 1.2])
with c1:
    go = st.button("🎲 랜덤 추천 받기", use_container_width=True)
with c2:
    reroll = st.button("🔁 다시 뽑기", use_container_width=True)
with c3:
    clear = st.button("🧹 기록 지우기", use_container_width=True)

trigger = go or reroll

if clear:
    st.session_state.history = []
    st.toast("기록을 깨끗하게 지웠어요 🧼", icon="🧹")

if trigger:
    candidate = random.choice(BOOKS[selected])
    stamp = {
        "category": selected,
        "title": candidate["title"],
        "mood": candidate["mood"],
        "why": candidate["why"],
    }
    st.session_state.history.append(stamp)
    st.balloons()
    # 가벼운 진행바 연출
    with st.spinner("반짝이는 추천을 준비 중... ✨"):
        for _ in range(12):
            time.sleep(0.03)

# ---------------------- 추천 결과 카드 ----------------------
if st.session_state.history:
    last = st.session_state.history[-1]
    st.markdown("""
    <div class="card">
      <div class="chip">오늘의 픽</div>
      <h2 style="margin:6px 0;">{emoji} <b>{title}</b></h2>
      <div class="small">장르: {cat}</div>
      <p style="margin-top:10px;">💡 <b>분위기</b>: {mood}</p>
      <p>🌟 <b>추천 이유</b>: {why}</p>
      <div class="small">다시 뽑아도 좋아요! 운명의 책을 찾을 때까지 🔮</div>
    </div>
    """.format(
        emoji=CATEGORY_EMOJIS.get(last["category"], "📚"),
        title=last["title"],
        cat=last["category"],
        mood=last["mood"],
        why=last["why"],
    ), unsafe_allow_html=True)

# ---------------------- 후보 전부 보기 ----------------------
if show_list:
    st.write("")
    st.markdown("#### 📚 이 장르의 다른 후보들")
    grid = st.columns(4)
    for i, book in enumerate(BOOKS[selected]):
        with grid[i % 4]:
            st.markdown(f"""
            <div class="card" style="margin-bottom:16px;">
              <div class="chip">후보</div>
              <h5 style="margin:4px 0 6px 0;">{book['title']}</h5>
              <div class="small">분위기: {book['mood']}</div>
              <div class="small">한 줄 이유: {book['why']}</div>
            </div>
            """, unsafe_allow_html=True)

# ---------------------- 히스토리 ----------------------
with st.expander("🗂️ 내가 뽑은 기록 펼치기"):
    if not st.session_state.history:
        st.caption("아직 기록이 없어요. 위에서 랜덤 추천을 받아보세요!")
    else:
        for h in reversed(st.session_state.history[-12:]):
            st.markdown(f"- {h['category']} — **{h['title']}** | {h['mood']} · {h['why']}")

# ---------------------- 푸터 ----------------------
st.write("")
st.markdown(
    '<div class="small">made with ❤️ streamlit · 이모지 파티 🎉</div>',
    unsafe_allow_html=True
)


