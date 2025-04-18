import streamlit as st
import pandas as pd

# 학생 목록
students = [
    {"id": "10410", "name": "박문찬 😊"},
    {"id": "10414", "name": "윤수호 🤗"},
    {"id": "10417", "name": "이제찬 😊"},
    {"id": "10421", "name": "정지우 😄"},
    {"id": "10715", "name": "윤  건 👍"},
    {"id": "10804", "name": "김건우 🌈"},
    {"id": "11226", "name": "조민우 🎉"},
    {"id": "11317", "name": "윤서준 🦄"},
    {"id": "20310", "name": "김하람 🌻"},
    {"id": "20328", "name": "최준영 🌼"},
    {"id": "20614", "name": "오태윤 😄"},
    {"id": "20909", "name": "김준경 🌼"},
    {"id": "21018", "name": "안영진 🌻"},
    {"id": "21024", "name": "이동현 🦄"},
    {"id": "21113", "name": "남승범 🎉"},
    {"id": "21205", "name": "김도하 🌈"},
]

# 설정할 날짜 목록(선택할 날짜)
date_options = [
    '2025-05-02 (금) 6, 7교시',
    '2025-07-04 (금) 6, 7교시 ',
    '2025-08-22 (금) 6, 7교시',
    '2025-09-12 (금) 6, 7교시',
    '2025-10-17 (금) 6, 7교시',
    '2025-12-19 (금) 6, 7교시',
    '2025-12-23 (화) 경희제준비',
    '2025-12-24 (수) 경희제',
    '2025-12-26 (금) 평가'
]

# 제목 설정
st.title("동아리 방송부 결석체크 🌟")

# 날짜 선택하기
selected_date = st.selectbox("날짜 선택", date_options)

# 출석 체크 박스 표시
attendance_status = {}
for student in students:
    attendance_status[student['name']] = st.checkbox(f"{student['name']} ({student['id']})")

# 특기사항 입력
if 'special_notes' not in st.session_state:
    st.session_state.special_notes = {}

# 선택한 날짜에 해당하는 특기사항 관리
special_note_key = f"special_note_{selected_date}"
special_notes = st.text_area("특기사항", st.session_state.special_notes.get(special_note_key, "여기에 특기사항을 입력하세요..."))


# 출석 저장 버튼
if st.button("결석 저장 📝"):
    # 출석 상태 기록
    attendance_records = {name: status for name, status in attendance_status.items()}

    # 출석 결과를 표시하기 위해 DataFrame으로 변환
    df = pd.DataFrame(attendance_records.items(), columns=["학생 이름", "결석 여부"])
    df["결석 여부"] = df["결석 여부"].apply(lambda x: "✖️" if x else "⭕")  # 올바른 열 이름 사용

    # 특기사항을 DataFrame에 추가
    df["특기사항"] = special_notes


    # 특기사항과 출석 기록을 세션 상태에 저장
    st.session_state.special_notes[special_note_key] = special_notes
    if 'attendance_records' not in st.session_state:
        st.session_state.attendance_records = {}

    # 날짜별 출석 결과를 저장
    st.session_state.attendance_records[selected_date] = df

    st.success(f"{selected_date} 출석 기록이 저장되었습니다.")

# 저장된 출석 기록이 있다면 보여주기
if 'attendance_records' in st.session_state:
    for date, records in st.session_state.attendance_records.items():
        st.subheader(f"{date} 출석 기록")
        st.dataframe(records)  # 출석 결과를 테이블 형태로 출력
