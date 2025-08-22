import random
import textwrap
import streamlit as st

# -------------------------
# 🎨 페이지 기본 설정
# -------------------------
st.set_page_config(
    page_title="📚 반짝반짝 북 피커",
    page_icon="📚",
    layout="wide",
)

# -------------------------
# 🌈 커스텀 스타일
# -------------------------
st.markdown("""
<style>
/* 배경 그RADIENT + 반짝이 */
.stApp {
  background: radial-gradient(1200px 600px at 10% 10%, #ffe9f9 0%, transparent 40%),
              radial-gradient(1000px 600px at 90% 0%, #e3f2ff 0%, transparent 40%),
              linear-gradient(135deg, #fff7ff 0%, #f5fbff 100%);
}

/* 글꼴 & 반짝 타이틀 */
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@300;400;600;800&display=swap');
html, body, [class*="css"] { font-family: 'Pretendard', system-ui, -apple-system, Segoe UI, Roboto, Noto Sans KR, 'Apple SD Gothic Neo', sans-serif; }

h1.title {
  font-size: clamp(28px, 5vw, 56px);
  font-weight: 800;
  line-height: 1.1;
  padding: 0.3rem 0;
  background: linear-gradient(90deg, #ff6fd8, #ffde59, #50e3c2, #7aa2ff, #ff6fd8);
  -webkit-background-clip: text; background-clip: text; color: transparent;
  text-shadow: 0 0 10px rgba(255, 255, 255, .7);
}

/* 글리터 라벨 */
.glitter {
  display: inline-block; padding: .35rem .7rem; border-radius: 999px;
  background: linear-gradient(135deg,#ffffffaa,#ffffff44);
  box-shadow: 0 10px 30px rgba(0,0,0,.08), inset 0 0 0 1px rgba(255,255,255,.6);
  backdrop-filter: blur(8px);
  font-weight: 600; font-size: .95rem;
}

/* 카드(글래스) */
.card {
  border-radius: 22px;
  padding: 1.2rem 1.4rem;
  background: linear-gradient(135deg, rgba(255,255,255,.85), rgba(255,255,255,.6));
  backdrop-filter: blur(10px);
  box-shadow: 0 12px 30px rgba(118, 118, 188, .18);
  border: 1px solid rgba(255,255,255,.7);
}

/* 버튼 과몰입 */
.stButton > button {
  border-radius: 16px !important;
  padding: .75rem 1rem !important;
  font-weight: 700 !important;
  box-shadow: 0 10px 25px rgba(0,0,0,.12) !important;
  border: 0 !important;
}

/* 선택 pill */
.pill {
  display:inline-flex; align-items:center; gap:.5rem;
  padding:.6rem .9rem; border-radius:999px; margin:.25rem;
  background:linear-gradient(135deg,#ffffff,#f6f6ff);
  box-shadow: 0 6px 18px rgba(0,0,0,.08);
  border:1px solid #eef;
  cursor:pointer; user-select:none;
  transition: transform .05s ease;
}
.pill:hover { transform: translateY(-1px); }
.pill.active {
  background:linear-gradient(135deg,#dff9fb,#f6f9ff);
  border-color:#cde;
}
.badge { font-size:.85rem; opacity:.9; }

.small {
  font-size: .9rem; opacity: .85;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# 📚 데이터: 카테고리별 추천
# -------------------------
BOOKS = {
    "문학": {
        "emoji": "✨📖🌙",
        "title": "어린 왕자",
        "author": "앙투안 드 생텍쥐페리",
        "why": "짧지만 깊은 상징과 질문으로 ‘어른이 된 우리’에게 잊고 있던 상상력과 다정함을 일깨워줘요.",
        "vibe": "잔잔함 · 상징 · 성찰"
    },
    "인문": {
        "emoji": "🧠🌍🔍",
        "title": "정의란 무엇인가",
        "author": "마이클 샌델",
        "why": "복잡한 사회적 딜레마를 흥미로운 사례로 풀어 ‘생각하는 근육’을 단단하게 만들어줘요.",
        "vibe": "토론 · 시민성 · 가치"
    },
    "과학": {
        "emoji": "🔭🌌🧬",
        "title": "코스모스",
        "author": "칼 세이건",
        "why": "우주와 과학의 역사, 인간의 호기심을 광활한 스케일로 안내하는 경이의 여행서.",
        "vibe": "경외 · 인문과학 · 교양"
    },
    "역사": {
        "emoji": "🏺📜🌐",
        "title": "사피엔스",
        "author": "유발 하라리",
        "why": "인류의 기원부터 미래까지 ‘이야기’로 엮어 우리가 왜 지금의 사회에 사는지 비춘 작품.",
        "vibe": "큰그림 · 통섭 · 날카로움"
    },
    "보건": {
        "emoji": "💪🩺🧠",
        "title": "바디: 우리 몸 안내서",
        "author": "빌 브라이슨",
        "why": "재치와 통찰로 인체를 구석구석 탐험—건강 지식이 ‘꿀잼’이 됩니다.",
        "vibe": "건강 · 상식 · 유머"
    },
    "미술": {
        "emoji": "🎨🖼️🌟",
        "title": "서양 미술사",
        "author": "E.H. 곰브리치",
        "why": "시대별 핵심 작품과 맥락을 깔끔히 정리—미술 감상의 ‘지도’가 생깁니다.",
        "vibe": "기초탄탄 · 흐름 · 감상력"
    },
    "음악": {
        "emoji": "🎵🎻🎹",
        "title": "이야기로 읽는 서양음악사",
        "author": "안인모",
        "why": "작곡가의 삶과 시대를 스토리로 엮어, 음악이 귀에 쏙쏙 들어와요.",
        "vibe": "스토리텔링 · 친절 · 즐거움"
    },
}

CATEGORIES = list(BOOKS.keys())

# -------------------------
# 🎉 헤더
# -------------------------
st.markdown('<h1 class="title">📚 반짝반짝 북 피커 — 카테고리 한 번, 인생책 한 권 ✨</h1>', unsafe_allow_html=True)
st.markdown(
    '<span class="glitter">💡 카테고리를 고르면 딱 맞는 추천을 드려요! 이모지 파티 시작 🎉</span>',
    unsafe_allow_html=True
)
st.write("")

# -------------------------
# 🧩 선택 영역 (Pill 스타일)
# -------------------------
cols = st.columns(4)
selected = st.session_state.get("selected")

for i, cat in enumerate(CATEGORIES):
    with cols[i % 4]:
        is_active = (selected == cat)
        label = f'<div class="pill {"active" if is_active else ""}">{"⭐" if is_active else "🌟"} <b>{cat}</b> <span class="badge">{BOOKS[cat]["emoji"]}</span></div>'
        if st.button(label, key=f"pill_{cat}", help=f"{cat} 추천 보기", use_container_width=True):
            st.session_state.selected = cat
            selected = cat

st.write("")

# 랜덤 추천
random_col1, random_col2, _ = st.columns([1,1,2])
with random_col1:
    if st.button("🎲 랜덤 추천 받기", use_container_width=True):
        st.session_state.selected = random.choice(CATEGORIES)
        selected = st.session_state.selected
        st.success(f"오늘의 랜덤 카테고리는 **{selected}** 🎉")

with random_col2:
    if st.button("🎈 축하풍선 터뜨리기", use_container_width=True):
        st.balloons()

st.write("")

# -------------------------
# 🪄 추천 결과 카드
# -------------------------
if selected:
    data = BOOKS[selected]
    st.markdown("---")
    left, right = st.columns([1.4, 1])
    with left:
        st.markdown(f"""
        <div class="card">
            <div class="small">선택한 카테고리</div>
            <h2 style="margin:.2rem 0 1rem 0"> {data["emoji"]} <b>{selected}</b></h2>
            <div class="small">오늘의 추천</div>
            <h3 style="margin:.2rem 0">📕 <b>{data['title']}</b></h3>
            <p class="small">✍️ {data['author']}</p>
            <p style="margin:.6rem 0 0 0;">{data['why']}</p>
            <div style="margin-top:.8rem; opacity:.85;">🏷️ <i>{data['vibe']}</i></div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown(f"""
        <div class="card">
            <h4 style="margin:.2rem 0 1rem 0">📌 이런 분께 특히 추천!</h4>
            <ul style="margin:0 0 .6rem 1rem;">
                <li>📚 새로운 분야를 가볍게 ‘한 권’으로 훑고 싶은 분</li>
                <li>⏱️ 길지 않은 시간에도 재미와 인사이트를 얻고 싶은 분</li>
                <li>🌈 예쁜 UI 속 이모지 파워로 독서 의욕 업! 하고 싶은 분</li>
            </ul>
            <p class="small">🎯 팁: 아래 버튼으로 클립보드에 복사해 친구에게도 추천을 전해보세요!</p>
        </div>
        """, unsafe_allow_html=True)

    # 복사 텍스트
    copy_text = textwrap.dedent(f"""
    [{selected}] {data['title']} — {data['author']}
    추천 이유: {data['why']} | 무드: {data['vibe']}
    """)

    st.code(copy_text.strip(), language="text")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.download_button(
            "💾 추천 메모(.txt) 저장",
            data=copy_text.strip(),
            file_name=f"book_reco_{selected}.txt",
            mime="text/plain",
            use_container_width=True,
        )
    with c2:
        st.button("🔁 다른 카테고리도 둘러보기", on_click=lambda: st.session_state.update(selected=None), use_container_width=True)
    with c3:
        st.info("📌 복사하고 싶다면 코드 블록 우측 상단 복사 버튼을 눌러주세요!", icon="✨")

else:
    st.markdown("""
    <div class="card">
      <b>👋 아직 카테고리를 고르지 않았어요!</b><br/>
      위의 보석 같은 <i>pill</i> 버튼들에서 <u>문학, 인문, 과학, 역사, 보건, 미술, 음악</u> 중 하나를 눌러보세요.
      <br/>🎲 망설여진다면 <b>랜덤 추천</b>도 준비되어 있어요!
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# 🧁 푸터
# -------------------------
st.markdown("---")
st.markdown("🪩 <b>Made with Streamlit</b> · 📚 반짝반짝 북 피커 · <span class='small'>읽는 즐거움에 이모지를 더해요 ✨</span>", unsafe_allow_html=True)

