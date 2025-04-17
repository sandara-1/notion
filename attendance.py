import streamlit as st
import pandas as pd

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

# 설정할 날짜 목록(선택할 날짜)
date_options = [
    '2025-05-01',
    '2025-05-02',
    '2025-05-03',
    '2025-05-04',
    '2025-05-05',
    '2025-05-06',
    '2025-05-07',
    '2025-05-08',
    '2025-05-09'
]

# 제목 설정
st.title("학생 출석부 🌟")

# 날짜 선택하기
selected_date = st.selectbox("날짜 선택", date_options)

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

    st.success(f"{selected_date} 출석 기록이 저장되었습니다:")
    st.dataframe(df)  # 출석 결과를 테이블 형태로 출력
