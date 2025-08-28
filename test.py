import random
import streamlit as st

st.set_page_config(
    page_title="랜덤 책 추천기",
    page_icon="📚",
    layout="centered"
)

# =========================
# 데이터: 장르별 [제목, 저자]
# =========================
BOOKS = {
    "문학": [
        ("시한부", "백은별"),
        ("스파클", "최현진"),
        ("순례 주택", "유은실"),
        ("내가 없던 어느 밤에", "이꽃"),
    ],
    "인문": [
        ("다크 심리학", "다크 사이트 프로젝트"),
        ("경험의 멸종", "크리스틴 로젠"),
        ("먼저 온 미래", "장강명"),
        ("사랑의 기술", "에리히 프롬"),
    ],
    "과학": [
        ("코스모스", "칼 세이건"),
        ("이기적 유전자", "리처드 도킨스"),
        ("흙의 숨", "유경수"),
        ("기억의 미래", "정민환"),
    ],
    "역사": [
        ("손자병법", "임용한"),
        ("폭력의 유산", "Elkins"),
        ("최소한의 한국사", "최태성"),
        ("책문", "김태완"),
    ],
    "보건": [
        ("다문화 사회와 건강", "안옥희, 최혜정"),
        ("1분 간호지식", "김유성"),
        ("생명과 약의 연결고리", "김성훈"),
        ("동공이 약사의 알찬 약국", "동공이 약사"),
    ],
    "미술": [
        ("미술관에 간 할미", "할미"),
        ("명화의 비밀, 그때 그 사람", "성수영"),
        ("살롱 드 경성", "김인혜"),
        ("방구석 미술관", "조원재"),
    ],
    "음악": [
        ("클래식의 심장, 유럽을 걷다", "이인현"),
        ("처음 만나는 국악 수업", "이동화"),
        ("피아노와 사회", "Arthur Loesser"),
        ("책속에 스며든 클래식", "박소현"),
    ],
}

# ==============
# 헤더 & 스타일
# ==============
st.markdown(
    """
    <style>
    .title {
        font-size: 42px; 
        font-weight: 800; 
        text-align: center; 
        margin: 8px 0 2px 0;
    }
    .subtitle {
        text-align: center; 
        font-size: 16px; 
        opacity: 0.85; 
        margin-bottom: 18px;
    }
    .card {
        border-radius: 20px;
        padding: 22px;
        border: 1px solid rgba(120,120,120,0.15);
        box-shadow: 0 8px 30px rgba(0,0,0,0.08);
        background: linear-gradient(180deg, rgba(255,255,255,0.85), rgba(250,250,255,0.9));
    }
    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        border: 1px solid rgba(120,120,255,0.25);
        background: rgba(120,120,255,0.08);
        letter-spacing: .3px;
        margin-bottom: 10px;
    }
    .book-title {
        font-size: 26px; 
        font-weight: 800; 
        margin: 6px 0 4px 0;
    }
    .book-author {
        font-size: 16px; 
        opacity: 0.9;
    }
    .hint {
        font-size: 14px; 
        opacity: 0.8; 
        margin-top: 12px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">📚 랜덤 책 추천기</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">장르를 고르면 오늘의 한 권을 뽑아드려요 🎲✨</div>', unsafe_allow_html=True)

# 세션 상태로 "다시 뽑기" 동작 제어
if "roll" not in st.session_state:
    st.session_state.roll = 0

# =============
# 입력 영역 UI
# =============
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        genre = st.selectbox(
            "장르를 선택하세요",
            options=list(BOOKS.keys()),
            index=0,
            help="문학, 인문, 과학, 역사, 보건, 미술, 음악 중에서 골라보세요!",
        )
    with col2:
        reroll = st.button("🔄 다시 뽑기")
        if reroll:
            st.session_state.roll += 1  # 값만 바꿔도 재추천 트리거

# ==================
# 추천 로직 & 출력
# ==================
books_in_genre = BOOKS.get(genre, [])

st.markdown("---")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<span class="badge">선택한 장르</span>  🎼🎨🧠🧪📖🕰️💊  <b>{genre}</b>', unsafe_allow_html=True)

    if books_in_genre:
        random.seed((hash(genre) + st.session_state.roll) % (2**32))
        book = random.choice(books_in_genre)

        title, author = book
        st.markdown(
            f"""
            <div class="book-title">✨ 『{title}』</div>
            <div class="book-author">✍️ {author}</div>
            """,
            unsafe_allow_html=True,
        )

        st.toast("오늘의 한 권이 도착했어요! 📦", icon="🎉")
        st.markdown('<div class="hint">Tip: 마음에 안 들면 <b>🔄 다시 뽑기</b>를 눌러보세요!</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div style="font-size:18px; margin-top:6px;">
            아직 이 장르의 목록이 비어 있어요 😅<br>
            추천 데이터를 추가하면 바로 랜덤 추천을 드릴게요!
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("")
st.caption("© 랜덤 책 추천기 — Have a bookish day! 📘🌙")

