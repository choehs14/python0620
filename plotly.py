import streamlit as st
import random
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

# Streamlit 설정
st.set_page_config(page_title="MBTI 직업 추천 💼✨", page_icon="🧩", layout="wide")

# 제목 및 설명
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3.5em; color: #8B5CF6;'>🎀 중학생을 위한 MBTI 직업 추천기 🎀</h1>
        <p style='font-size: 1.2em; color: #666;'>나의 성격에 딱 맞는 직업은 뭘까? 재미있고 귀엽게 찾아보자! 🧁🎈</p>
    </div>
""", unsafe_allow_html=True)

# MBTI 리스트 및 직업 매핑 (중학생 맞춤)
mbti_career_map = {
    "INTJ": ["🧠 과학자", "📊 데이터 분석가", "🤖 AI 연구자", "🧮 수학 선생님", "🧑‍💻 프로그래머"],
    "INFP": ["✍️ 동화 작가", "🎨 삽화가", "🎭 연극 배우", "📚 문학 연구자", "💌 웹툰 작가"],
    "ESFP": ["🎤 가수", "💃 댄서", "📸 인플루언서", "🎉 행사 기획자", "🎬 유튜버"],
    "ENTP": ["🚀 발명가", "📢 홍보 기획자", "🧑‍💼 스타트업 CEO", "📱 앱 개발자", "🎯 콘텐츠 디자이너"],
    "ISFJ": ["🧸 유치원 선생님", "🧁 제과제빵사", "📖 사서", "🎀 심리상담사", "🐶 동물 간호사"],
    "ENFP": ["🎨 디자이너", "🎤 방송인", "📝 기자", "🎈 놀이공원 기획자", "🌟 크리에이터"]
}

# 사용자 MBTI 선택 인터페이스
st.markdown("""
    <div style='margin-top: 30px; padding: 20px; background-color: #EDE9FE; border-radius: 15px;'>
        <h3 style='color: #7C3AED;'>📌 아래에서 나의 MBTI를 골라주세요!</h3>
""", unsafe_allow_html=True)

mbti_options = list(mbti_career_map.keys())
selected_mbti = st.selectbox("🔍 MBTI를 선택하세요:", mbti_options)

st.markdown("""
    </div>
""", unsafe_allow_html=True)

# MBTI에 따라 추천 직업 표시
if selected_mbti:
    st.markdown(f"""
        <div style='background-color: #F3F4F6; padding: 30px; border-radius: 15px; margin-top: 30px;'>
            <h2 style='color: #4B5563;'>💖 {selected_mbti} 유형에게 어울리는 직업들 💖</h2>
            <ul style='font-size: 1.3em; color: #374151;'>
    """, unsafe_allow_html=True)

    for job in mbti_career_map[selected_mbti]:
        st.markdown(f"<li>🌟 {job}</li>", unsafe_allow_html=True)

    st.markdown("""
            </ul>
        </div>
    """, unsafe_allow_html=True)

# 하단 인사말 + 정보교사 응원 메시지 추가
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <img src='https://media.giphy.com/media/3o7aCTfyhYawdOXcFW/giphy.gif' width='250'>
        <h4 style='color:#8B5CF6;'>🌈 꿈을 향해 한 걸음씩 나아가 볼까요? ✨</h4>
        <p style='color:#666;'>모든 MBTI는 멋진 미래를 만들어갈 수 있어요! 🚀</p>
    </div>

    <div style='text-align: center; margin-top: 40px; background-color: #E0E7FF; padding: 30px; border-radius: 15px;'>
        <h3 style='color:#4C51BF;'>🧑‍🏫 함께 배우는 정보 선생님들께</h3>
        <p style='font-size: 1.1em; color:#4A5568;'>
            오늘도 파이썬과 깃허브, 스트림릿을 배우며 고군분투하는 당신!<br>
            토요일에도 교육을 위해 열정을 쏟는 모습이 정말 멋집니다. 💪💜<br>
            잠깐의 커피 한 잔과 이 따뜻한 이미지가 위로가 되기를 바래요 ☕🍀
        </p>
        <img src='https://media.giphy.com/media/l0HlRmU2QdhrmDWKQ/giphy.gif' width='200'>
        <p style='font-size: 1em; color:#718096;'>"작은 배움이 모여 아이들의 미래를 만듭니다." 💻✨</p>
    </div>
""", unsafe_allow_html=True)

# 📈 글로벌 시가총액 TOP 10 기업 주가 시각화
st.markdown("""
    <div style='margin-top: 60px;'>
        <h2 style='color:#4338CA;'>📈 글로벌 시가총액 TOP 10 기업의 최근 1년 주가 변화</h2>
    </div>
""", unsafe_allow_html=True)

# 티커 심볼 목록 (2024 기준 상위 기업들)
top10_tickers = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOGL': 'Alphabet (Google)',
    'AMZN': 'Amazon',
    'NVDA': 'NVIDIA',
    'META': 'Meta (Facebook)',
    'TSLA': 'Tesla',
    'BRK-B': 'Berkshire Hathaway',
    'TSM': 'Taiwan Semiconductor',
    'LLY': 'Eli Lilly'
}

end_date = datetime.today()
start_date = end_date - timedelta(days=365)

fig = go.Figure()

for ticker, name in top10_tickers.items():
    data = yf.download(ticker, start=start_date, end=end_date)
    if not data.empty:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['Adj Close'],
            mode='lines',
            name=name
        ))

fig.update_layout(
    title="최근 1년간 주가 변화",
    xaxis_title="날짜",
    yaxis_title="종가 (USD)",
    legend_title="기업명",
    template="plotly_white",
    height=600
)

st.plotly_chart(fig, use_container_width=True)
