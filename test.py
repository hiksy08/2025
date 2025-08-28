import random
import streamlit as st

st.set_page_config(
    page_title="랜덤 책 추천기",
    page_icon="📖",
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
        font-size: 38px; 
        font-weight: 900; 
        text-align: center; 
        margin: 10px 0;
        color: #2E2E3A;
    }
    .subtitle {
        text-align: center; 
        font-size: 16px; 
        opacity: 0.8; 
        margin-bottom: 25px;
    }
    .card {
        border-radius: 16px;
        padding: 25px;
        border: 1px solid rgba(0,0,0,0.05);
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        background: #ffffffcc;
    }
    .badge {
        display: inline-block;
        padding: 5px 12px;
        border-radius: 12px;
        font-size: 13px;
        font-weight: 600;
        background: #f1f3f8;
        color: #333;
        margin-bottom: 12px;
    }
    .book-title {
        font-size: 28px; 
        font-weight: 800; 
        margin: 8px 0 6px 0;
        color: #222;
    }
    .book-author {
        font-size: 17px; 
        opacity: 0.9;
        color: #444;
    }
    .hint {
        font-size: 14px; 
        opacity: 0.75; 
        margin-top: 14px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">📖 랜덤 책 추천기 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">원하는 장르를 고르면 오늘의 책을 추천해드려요</div>', unsafe_allow_html=True)

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
        )
    with col2:
        reroll = st.button("다시 뽑기 🔄")
        if reroll:
            st.session_state.roll += 1

# ==================
# 추천 로직 & 출력
# ==================
books_in_genre = BOOKS.get(genre, [])

st.markdown("---")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f'<span class="badge">📂 선택한 장르: {genre}</span>', unsafe_allow_html=True)

    if books_in_genre:
        random.seed((hash(genre) + st.session_state.roll) % (2**32))
        book = random.choice(books_in_genre)

        title, author = book
        st.markdown(
            f"""
            <div class="book-title">『{title}』</div>
            <div class="book-author">✍️ 저자: {author}</div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div class="hint">👉 다른 책이 궁금하다면 <b>다시 뽑기</b> 버튼을 눌러보세요!</div>', unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div style="font-size:18px; margin-top:6px;">
            아직 이 장르의 책 목록이 준비되지 않았습니다.
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("")
st.caption("🎵 좋은 책과 함께하는 하루 되세요!")
