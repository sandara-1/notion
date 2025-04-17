import streamlit as st
import pandas as pd
from datetime import datetime

# 학생 목록
students = [
    {"id": "10410", "name": "바롱꿍 😊"},
    {"id": "10411", "name": "윤옥수 🤗"},
    {"id": "10412", "name": "정기원 😊"},
    {"id": "10413", "name": "김가영 😄"},
    {"id": "10414", "name": "조윤주 👍"},
    {"id": "10415", "name": "윤수현 🌈"},
    {"id": "20410", "name": "최준엽 🎉"},
    {"id": "20411", "name": "김지훈 🦄"},
    {"id": "20412", "name": "오현지 🌻"},
    {"id": "20413", "name": "박수라 🌼"},
    {"id": "20414", "name": "정세원 😁"},
]

# 제목 설정
st.title("학생 출석부 🌟")

# 날짜 선택기
date = st.date_input("날짜 선택", datetime.today())

# 출석 체크 박스 표시
attendance_status = {}
for student in students:
    attendance_status[student['name']] = st.checkbox(f"{student['name']} ({student['id']})")

# 출석 저장 버튼
if st.button("출석 저장 📝"):
    attendance_records = {name: status for name, status in attendance_status.items()}
    # 출석 결과를 표시하기 위해 DataFrame으로 변환
    df = pd.DataFrame(attendance_records.items(), columns=["학생 이름", "출석 여부"])
    df["출석 여부"] = df["출석 여부"].apply(lambda x: "출석" if x else "결석")

    st.success("출석 기록이 저장되었습니다:")
    st.dataframe(df)  # 출석 결과를 테이블 형태로 출력
