

import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk

class AttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("학생 출석부 🌟")

        # 배경색 설정
        self.root.configure(bg='#f0f8ff')

        self.students = [
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

        self.attendance = {}

        # 날짜 선택기
        tk.Label(root, text="날짜 선택:", bg='#f0f8ff').grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        # 학생 출석 체크박스
        self.check_vars = []
        for index, student in enumerate(self.students):
            var = tk.BooleanVar()
            self.check_vars.append(var)
            tk.Checkbutton(root, text=f"{student['name']} ({student['id']})", variable=var, bg='#f0f8ff', font=('Arial', 12)).grid(row=index + 1, column=0, sticky='w')

        # 출석 저장 버튼
        tk.Button(root, text="출석 저장 📝", command=self.save_attendance, bg='lightgreen', font=('Arial', 12, 'bold')).grid(row=len(self.students) + 1, column=0, padx=5, pady=5)

        # 예쁜 이미지 추가
        self.add_image()

    def add_image(self):
        try:
            # 이미지 파일 경로를 입력하세요
            img = Image.open("your_image_path.png")  # 이미지 파일 경로
            img = img.resize((100, 100), Image.ANTIALIAS)
            self.image_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(self.root, image=self.image_tk, bg='#f0f8ff')
            img_label.grid(row=0, column=2, rowspan=len(self.students) + 2, padx=10, pady=10)

        except Exception as e:
            print(f"Error loading image: {e}")

    def save_attendance(self):
        date = self.date_entry.get()
        for index, student in enumerate(self.students):
            self.attendance[student['name']] = {
                "id": student['id'],
                "date": date,
                "present": self.check_vars[index].get()
            }

        attendance_records = "\n".join([
            f"{name}: {'출석' if info['present'] else '결석'}, 날짜: {info['date']}"
            for name, info in self.attendance.items()
        ])
        messagebox.showinfo("출석 체크", f"출석 기록이 저장되었습니다:\n{attendance_records}")

if __name__ == "__main__":
    root = tk.Tk()
    app = AttendanceApp(root)
    root.mainloop()
