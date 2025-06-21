import streamlit as st
import random

# Streamlit 설정
st.set_page_config(page_title="MBTI 직업 추천 💼✨", page_icon="🧩", layout="wide")

# 제목 및 설명
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3.5em; color: #8B5CF6;'>🎀 MBTI 직업 추천기 🎀</h1>
        <p style='font-size: 1.2em; color: #666;'>나의 성격에 딱 맞는 직업은 뭘까? 🧁🎈</p>
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

# 하단 인사말
st.markdown("""
    <div style='text-align: center; margin-top: 50px;'>
        <img src='https://media.giphy.com/media/xT0GqeSlGSRQut4Zuo/giphy.gif' width='200'>
        <h4 style='color:#8B5CF6;'>🌈 꿈을 향해 한 걸음씩 나아가 볼까요? ✨</h4>
        <p style='color:#666;'>모든 MBTI는 멋진 미래를 만들어갈 수 있어요! 🚀</p>
    </div>
""", unsafe_allow_html=True)
