import streamlit as st
import folium
from streamlit_folium import st_folium
from fastkml import kml

# Streamlit 설정
st.set_page_config(page_title="마라톤 코스 안내 🏃‍♂️", page_icon="🏁", layout="wide")

# 타이틀
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3.2em; color: #16A34A;'>🏁 마라톤 코스 & 화장실 위치 안내 🗺️</h1>
        <p style='font-size: 1.2em; color: #4B5563;'>코스 경로와 가까운 화장실 위치를 미리 확인하고 준비하세요!</p>
    </div>
""", unsafe_allow_html=True)

# 마라톤 화장실 위치 데이터
toilets = [
    {"name": "여의도 공원 화장실", "address": "서울 영등포구 여의공원로 120", "lat": 37.5264, "lon": 126.9245},
    {"name": "한강공원 이촌지구 화장실", "address": "서울 용산구 이촌로72길 62", "lat": 37.5187, "lon": 126.9735},
    {"name": "뚝섬 한강공원 화장실", "address": "서울 광진구 자양동 435", "lat": 37.5316, "lon": 127.0672},
    {"name": "반포 한강공원 화장실", "address": "서울 서초구 신반포로11길 40", "lat": 37.5109, "lon": 126.9955}
]

# 지도 초기 위치
m = folium.Map(location=[37.52, 126.95], zoom_start=12)

# 화장실 위치 마커 추가
for toilet in toilets:
    folium.Marker(
        [toilet["lat"], toilet["lon"]],
        tooltip=toilet["name"],
        popup=f"<b>{toilet['name']}</b><br>{toilet['address']}"
    ).add_to(m)

# 마라톤 코스 (KML 파일 읽기 및 추가)
kml_path = "/mnt/data/마라톤코스.kml"
try:
    with open(kml_path, "rt", encoding="utf-8") as f:
        k = kml.KML()
        k.from_string(f.read())
        features = list(k.features())
        for feature in features:
            for sub_feature in feature.features():
                if hasattr(sub_feature, 'geometry'):
                    coords = sub_feature.geometry.coords[:]
                    coords = [[lat, lon] for lon, lat in coords]  # KML은 (lon, lat)
                    folium.PolyLine(coords, color="blue", weight=5, tooltip="🏃 마라톤 코스").add_to(m)
except Exception as e:
    st.error(f"🚫 마라톤 코스를 불러오는 데 문제가 발생했습니다: {e}")

# 지도 출력
st.markdown("""
    <div style='margin-top: 40px;'>
        <h3 style='color:#10B981;'>🗺️ 지도 보기</h3>
    </div>
""", unsafe_allow_html=True)

st_data = st_folium(m, width=800, height=600)
