import streamlit as st
import folium
from streamlit_folium import st_folium
from fastkml import kml

# 페이지 설정
st.set_page_config(page_title="마라톤 안내 🏁", layout="wide")

# 제목
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='font-size: 3em; color: #16A34A;'>🏁 마라톤 코스 & 화장실 위치</h1>
        <p style='font-size: 1.2em; color: #4B5563;'>준비된 주자라면 코스도, 편의시설도 미리 확인해요!</p>
    </div>
""", unsafe_allow_html=True)

# 지도 초기화
m = folium.Map(location=[36.448, 127.092], zoom_start=12)

# 마라톤 코스 불러오기 (KML 파일)
kml_path = "/mnt/data/마라톤코스.kml"
try:
    with open(kml_path, "rt", encoding="utf-8") as f:
        k = kml.KML()
        k.from_string(f.read())
        features = list(k.features())
        for f1 in features:
            for f2 in f1.features():
                if hasattr(f2, 'geometry'):
                    coords = f2.geometry.coords
                    polyline_coords = [[lat, lon] for lon, lat in coords]
                    folium.PolyLine(polyline_coords, color="blue", weight=5, tooltip="🏃 마라톤 코스").add_to(m)
except Exception as e:
    st.error(f"❌ 마라톤 코스 로딩 오류: {e}")

# 화장실 마커
toilets = [
    {"name": "여의도 공원 화장실", "address": "서울 영등포구 여의공원로 120", "lat": 37.5264, "lon": 126.9245},
    {"name": "한강공원 이촌지구 화장실", "address": "서울 용산구 이촌로72길 62", "lat": 37.5187, "lon": 126.9735},
    {"name": "뚝섬 한강공원 화장실", "address": "서울 광진구 자양동 435", "lat": 37.5316, "lon": 127.0672},
    {"name": "반포 한강공원 화장실", "address": "서울 서초구 신반포로11길 40", "lat": 37.5109, "lon": 126.9955}
]
for toilet in toilets:
    folium.Marker(
        [toilet["lat"], toilet["lon"]],
        tooltip=toilet["name"],
        popup=f"<b>{toilet['name']}</b><br>{toilet['address']}",
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_folium(m, width=800, height=600)
