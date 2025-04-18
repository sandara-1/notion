import streamlit as st
import pandas as pd
import os

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

# 설정할 날짜 목록
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
st.title("동아리 방송부 결석 체크 🌟")

# 파일 이름 정의
attendance_file = "attendance_records.csv"

# 날짜 선택하기
selected_date = st.selectbox("날짜 선택", date_options)

# 출석 체크 박스 표시 및 특기사항 입력
attendance_status = {}
special_notes = {}

# 날짜가 선택될 때마다 입력 필드를 초기화
if selected_date not in st.session_state:
    st.session_state[selected_date] = {}

# 학생별 출석 체크 및 특기사항 입력
for student in students:
    # 출석 체크박스 생성
    attendance_status[student['name']] = st.checkbox(f"{student['name']} ({student['id']})",
                                                     value=st.session_state[selected_date].get(student['name'], False))

    # 특기사항 입력 필드
    special_note_key = f"{student['name']}_note"
    special_notes[special_note_key] = st.text_input(f"특기사항 ({student['name']})",
                                                     value=st.session_state[selected_date].get(special_note_key, ""),
                                                     key=special_note_key)  # 특정 키를 설정하여 일관성을 유지

# 출석 저장 버튼
if st.button("출석 저장 📝"):
    # 출석 상태 기록
    attendance_records = {name: status for name, status in attendance_status.items()}

    # 출석 결과로 DataFrame 생성
    df = pd.DataFrame(attendance_records.items(), columns=["학생 이름", "출석 여부"])
    df["출석 여부"] = df["출석 여부"].apply(lambda x: "출석" if x else "결석")  # 결과를 적절하게 표시

    # 특기사항을 DataFrame에 추가
    df["특기사항"] = [special_notes[f"{student['name']}_note"] for student in students]  # 특기사항 수집
    df["날짜"] = selected_date  # 날짜 추가

    # 파일이 이미 존재하고 형식이 잘못된 경우 파일 삭제
    if os.path.isfile(attendance_file):
        try:
            previous_records = pd.read_csv(attendance_file)
        except pd.errors.ParserError:
            os.remove(attendance_file)  # 잘못된 CSV 파일 삭제

    # 파일에 데이터 저장
    df.to_csv(attendance_file, mode='w', index=False)

    # 세션 상태에 각각의 출석 기록과 특기사항 저장
    st.session_state[selected_date] = {}
    for student in students:
        st.session_state[selected_date][student['name']] = attendance_status[student['name']]
        st.session_state[selected_date][f"{student['name']}_note"] = special_notes[f"{student['name']}_note"]

    st.success(f"{selected_date} 출석 기록이 저장되었습니다.")

# 저장된 출석 기록을 선택하기 위한 날짜 선택
if os.path.isfile(attendance_file):
    st.subheader("이전 출석 기록 보기")

    # 날짜 선택 옵션을 추가
    previous_dates = pd.read_csv(attendance_file)["날짜"].unique()
    selected_previous_date = st.selectbox("날짜 선택", previous_dates)

    # 선택한 날짜의 출석 기록을 필터링
    records_for_date = pd.read_csv(attendance_file)
    records_for_date = records_for_date[records_for_date["날짜"] == selected_previous_date]
    st.dataframe(records_for_date)  # 선택한 날짜의 출석 기록을 데이터프레임으로 보여주기
else:
    st.warning("현재 저장된 출석 기록이 없습니다.")
