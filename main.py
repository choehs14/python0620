import streamlit as st
from PIL import Image
import random

# 직업 추천 데이터 (예시)
mbti_careers = {
    "INTJ": [
        "🧠 전략 컨설턴트", "📊 데이터 과학자", "🤖 AI 연구원",
        "🧮 수학자", "🛰 우주공학자", "🔬 과학연구원", "📈 금융 분석가", "📡 정보보안 전문가",
        "📐 시스템 설계자", "⚙️ 로봇 엔지니어", "💻 소프트웨어 아키텍트", "📘 정책 분석가"
    ],
    "INFP": [
        "✍️ 작가", "🧘 심리상담사", "🎨 일러스트레이터",
        "🎭 시나리오 작가", "📖 아동문학가", "💌 콘텐츠 크리에이터", "🪄 예술 치료사", "🎬 영화 감독",
        "📚 인문학 연구자", "📸 포토그래퍼", "🎼 작곡가", "🌿 환경운동가"
    ],
    "ESFP": [
        "🎭 배우", "🎉 이벤트 플래너", "💄 뷰티 크리에이터",
        "🎤 가수", "💃 댄서", "📷 모델", "📹 유튜버", "🛍 패션 스타일리스트",
        "🎡 테마파크 엔터테이너", "🎮 게임 스트리머", "🎙 라디오 DJ", "🎈 키즈 파티 디자이너"
    ],
    "ENTP": [
        "🚀 창업가", "📢 마케팅 전문가", "📝 기획자",
        "💼 비즈니스 컨설턴트", "📱 UX 디자이너", "💬 커뮤니케이션 전략가", "🎯 브랜딩 전문가",
        "🗣 토론 강사", "🧪 혁신 연구자", "🎮 게임 기획자", "📊 세일즈 매니저", "📍 프로젝트 매니저"
    ],
    # ... 다른 MBTI도 추가
}

# 이미지 경로 (각 MBTI에 맞는 이미지 사용)
mbti_images = {
    "INTJ": "images/intj.png",
    "INFP": "images/infp.png",
    "ESFP": "images/esfp.png",
    "ENTP": "images/entp.png",
    # ... 다른 MBTI도 추가
}

# 앱 제목
st.set_page_config(page_title="MBTI 진로 추천기 🧭", page_icon="🎨", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #FF69B4; font-size: 3em;'>
        🌟 MBTI로 알아보는 나의 미래 직업 🌟
    </h1>
    <p style='text-align: center; font-size: 1.2em;'>당신의 성격에 딱 맞는 직업을 찾아보세요! 💼✨</p>
""", unsafe_allow_html=True)

# 귀여운 사이드바 설정
st.sidebar.markdown("""
    <h3 style='color:#FFB6C1;'>🧩 당신의 MBTI는?</h3>
""", unsafe_allow_html=True)
selected_mbti = st.sidebar.selectbox("🔍 MBTI를 선택하세요:", list(mbti_careers.keys()))

# 메인 콘텐츠
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown(f"<h2 style='color: #9370DB;'>💖 당신의 MBTI는 <span style='color:#FF1493;'>{selected_mbti}</span>입니다!</h2>", unsafe_allow_html=True)
    image_path = mbti_images.get(selected_mbti, None)
    if image_path:
        image = Image.open(image_path)
        st.image(image, caption=f"{selected_mbti} 타입 🧬", use_column_width=True)

with col2:
    st.markdown("<h3 style='color:#FF8C00;'>✨ 추천 직업 리스트 ✨</h3>", unsafe_allow_html=True)
    recommendations = mbti_careers.get(selected_mbti, [])
    for job in recommendations:
        st.markdown(f"<div style='font-size: 1.5em; color: #2E8B57;'>🌟 {job}</div>", unsafe_allow_html=True)

# 하단 귀여운 인사말
st.markdown("""
    <div style='text-align:center; padding-top: 50px;'>
        <img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzZmZTZ4cWxud3o4M2k2emF5b25mcTV6am05YjRxaTR2OHZra3M3biZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qgQUggAC3Pfv687qPC/giphy.gif' width='300'>
        <h4 style='color:#FF69B4;'>🌈 너무 멋진 미래가 기다리고 있어요! 💫🌟</h4>
        <p style='color:#888;'>🎯 계속해서 당신만의 길을 탐색하세요 💼🚀</p>
    </div>
""", unsafe_allow_html=True)
