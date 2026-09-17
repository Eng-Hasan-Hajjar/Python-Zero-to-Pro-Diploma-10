import tkinter as tk
from tkinter import messagebox
import random


# ==========================================
# أسماء الطلاب ونقاطهم
# ==========================================

scores = {
    "اريج": 0,
    "ياسمين": 0,
    "يونس": 0,
    "زهراء": 0,
    "كيندا": 0,
    "مجد": 0,
    "رامي": 0
}


# الطالب المختار حالياً
current_student = None


# ==========================================
# اختيار طالب عشوائي
# ==========================================

def choose_student():

    global current_student

    # نحصل على أسماء الطلاب من الـ dictionary
    students = list(scores.keys())

    if len(students) == 0:

        result_label.config(
            text="لا يوجد طلاب"
        )

        return

    # اختيار اسم عشوائي
    current_student = random.choice(students)

    # إظهار الاسم
    result_label.config(
        text=current_student
    )

    # إظهار نقاط الطالب
    current_score_label.config(
        text=f"نقاط الطالب: {scores[current_student]}"
    )


# ==========================================
# إجابة صحيحة
# ==========================================

def correct_answer():

    global current_student

    if current_student is None:

        messagebox.showwarning(
            "تنبيه",
            "اختر طالباً أولاً"
        )

        return

    # إضافة نقطة
    scores[current_student] += 1

    # تحديث نقاط الطالب
    current_score_label.config(
        text=f"نقاط الطالب: {scores[current_student]}"
    )

    # تحديث جدول النقاط
    update_scores()


# ==========================================
# إجابة خاطئة
# ==========================================

def wrong_answer():

    global current_student

    if current_student is None:

        messagebox.showwarning(
            "تنبيه",
            "اختر طالباً أولاً"
        )

        return

    # خصم نقطة
    scores[current_student] -= 1

    # تحديث نقاط الطالب
    current_score_label.config(
        text=f"نقاط الطالب: {scores[current_student]}"
    )

    # تحديث جدول النقاط
    update_scores()


# ==========================================
# إضافة طالب جديد
# ==========================================

def add_student():

    name = student_entry.get().strip()

    # الاسم فارغ
    if name == "":

        messagebox.showwarning(
            "تنبيه",
            "اكتب اسم الطالب"
        )

        return

    # الطالب موجود
    if name in scores:

        messagebox.showwarning(
            "تنبيه",
            "هذا الطالب موجود بالفعل"
        )

        return

    # إضافة الطالب ونقاطه تبدأ من صفر
    scores[name] = 0

    # تنظيف مربع الكتابة
    student_entry.delete(
        0,
        tk.END
    )

    # تحديث القائمة
    update_scores()


# ==========================================
# حذف طالب
# ==========================================

def delete_student():

    global current_student

    selected = scores_listbox.curselection()

    if not selected:

        messagebox.showwarning(
            "تنبيه",
            "اختر طالباً من القائمة"
        )

        return

    index = selected[0]

    # نحصل على الاسم حسب رقم العنصر
    student_name = list(scores.keys())[index]

    # حذف الطالب
    del scores[student_name]

    # إذا كان الطالب المحذوف هو الطالب الحالي
    if current_student == student_name:

        current_student = None

        result_label.config(
            text="؟"
        )

        current_score_label.config(
            text="نقاط الطالب: 0"
        )

    update_scores()


# ==========================================
# تحديث جدول النقاط
# ==========================================

def update_scores():

    scores_listbox.delete(
        0,
        tk.END
    )

    # المرور على الطلاب والنقاط
    for student, points in scores.items():

        scores_listbox.insert(
            tk.END,
            f"{student}  |  النقاط: {points}"
        )

    # عدد الطلاب
    count_label.config(
        text=f"عدد الطلاب: {len(scores)}"
    )


# ==========================================
# تصفير جميع النقاط
# ==========================================

def reset_scores():

    answer = messagebox.askyesno(
        "تصفير النقاط",
        "هل تريد تصفير نقاط جميع الطلاب؟"
    )

    if answer:

        # تصفير كل الطلاب
        for student in scores:

            scores[student] = 0

        update_scores()

        if current_student is not None:

            current_score_label.config(
                text="نقاط الطالب: 0"
            )


# ==========================================
# إضافة الطالب عند الضغط Enter
# ==========================================

def press_enter(event):

    add_student()


# ==========================================
# النافذة الرئيسية
# ==========================================

window = tk.Tk()

window.title(
    "نظام الطلاب والنقاط"
)

window.geometry(
    "550x760"
)

window.resizable(
    False,
    False
)

window.configure(
    bg="#141e30"
)


# ==========================================
# العنوان
# ==========================================

title_label = tk.Label(
    window,
    text="نظام اختيار الطلاب والنقاط",
    font=("Arial", 23, "bold"),
    bg="#141e30",
    fg="white"
)

title_label.pack(
    pady=(25, 5)
)


description_label = tk.Label(
    window,
    text="اختر طالباً عشوائياً ثم سجل إجابته",
    font=("Arial", 12),
    bg="#141e30",
    fg="#cccccc"
)

description_label.pack(
    pady=(0, 15)
)


# ==========================================
# مكان ظهور الطالب
# ==========================================

result_frame = tk.Frame(
    window,
    bg="#243b55",
    width=430,
    height=145
)

result_frame.pack(
    pady=10
)

result_frame.pack_propagate(
    False
)


student_title = tk.Label(
    result_frame,
    text="الطالب المختار",
    font=("Arial", 12),
    bg="#243b55",
    fg="#cccccc"
)

student_title.pack(
    pady=(15, 3)
)


result_label = tk.Label(
    result_frame,
    text="؟",
    font=("Arial", 31, "bold"),
    bg="#243b55",
    fg="#00e5ff"
)

result_label.pack()


current_score_label = tk.Label(
    result_frame,
    text="نقاط الطالب: 0",
    font=("Arial", 13, "bold"),
    bg="#243b55",
    fg="white"
)

current_score_label.pack(
    pady=5
)


# ==========================================
# اختيار طالب
# ==========================================

choose_button = tk.Button(
    window,
    text="🎲 اختر طالباً عشوائياً",
    command=choose_student,
    font=("Arial", 14, "bold"),
    bg="#00bcd4",
    fg="white",
    activebackground="#0097a7",
    width=30,
    height=2,
    border=0,
    cursor="hand2"
)

choose_button.pack(
    pady=15
)


# ==========================================
# أزرار الإجابة
# ==========================================

answer_frame = tk.Frame(
    window,
    bg="#141e30"
)

answer_frame.pack(
    pady=5
)


correct_button = tk.Button(
    answer_frame,
    text="✅ إجابة صحيحة +1",
    command=correct_answer,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    width=18,
    height=2,
    border=0,
    cursor="hand2"
)

correct_button.grid(
    row=0,
    column=0,
    padx=5
)


wrong_button = tk.Button(
    answer_frame,
    text="❌ إجابة خاطئة -1",
    command=wrong_answer,
    font=("Arial", 12, "bold"),
    bg="#f44336",
    fg="white",
    width=18,
    height=2,
    border=0,
    cursor="hand2"
)

wrong_button.grid(
    row=0,
    column=1,
    padx=5
)


# ==========================================
# إضافة طالب
# ==========================================

student_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=28,
    justify="center"
)

student_entry.pack(
    pady=(20, 5)
)

student_entry.bind(
    "<Return>",
    press_enter
)


add_button = tk.Button(
    window,
    text="➕ إضافة طالب",
    command=add_student,
    font=("Arial", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=20,
    border=0,
    cursor="hand2"
)

add_button.pack(
    pady=5
)


# ==========================================
# قائمة الطلاب ونقاطهم
# ==========================================

scores_title = tk.Label(
    window,
    text="🏆 سجل النقاط",
    font=("Arial", 16, "bold"),
    bg="#141e30",
    fg="white"
)

scores_title.pack(
    pady=(15, 5)
)


scores_listbox = tk.Listbox(
    window,
    font=("Arial", 13),
    width=35,
    height=8,
    justify="center",
    selectbackground="#00bcd4"
)

scores_listbox.pack(
    pady=5
)


# ==========================================
# حذف طالب
# ==========================================

delete_button = tk.Button(
    window,
    text="🗑 حذف الطالب المحدد",
    command=delete_student,
    font=("Arial", 10, "bold"),
    bg="#ff5722",
    fg="white",
    width=20,
    border=0,
    cursor="hand2"
)

delete_button.pack(
    pady=5
)


# ==========================================
# تصفير النقاط
# ==========================================

reset_button = tk.Button(
    window,
    text="تصفير جميع النقاط",
    command=reset_scores,
    font=("Arial", 10),
    bg="#555555",
    fg="white",
    width=20,
    border=0,
    cursor="hand2"
)

reset_button.pack(
    pady=5
)


# ==========================================
# عدد الطلاب
# ==========================================

count_label = tk.Label(
    window,
    text="",
    font=("Arial", 11),
    bg="#141e30",
    fg="#cccccc"
)

count_label.pack(
    pady=5
)


# ==========================================
# عرض القائمة أول مرة
# ==========================================

update_scores()


# ==========================================
# تشغيل البرنامج
# ==========================================

window.mainloop()