import tkinter as tk
from tkinter import messagebox
import random
import json
import os


# =========================================================
# اسم ملف حفظ البيانات
# =========================================================

DATA_FILE = "students_data.json"


# =========================================================
# الطلاب الافتراضيون
# سيتم استخدامهم فقط أول مرة
# =========================================================

default_students = {
    "أريج": 0,
    "ياسمين": 0,
    "يونس": 0,
    "زهراء": 0,
    "كيندا": 0,
    "مجد": 0
}


# =========================================================
# تحميل البيانات من الملف
# =========================================================

def load_data():

    # إذا كان الملف موجوداً
    if os.path.exists(DATA_FILE):

        try:

            with open(
                DATA_FILE,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

                return data

        except:

            messagebox.showwarning(
                "تنبيه",
                "حدث خطأ أثناء قراءة ملف البيانات."
            )


    # إذا لم يكن الملف موجوداً
    # نعيد نسخة من الطلاب الافتراضيين

    return default_students.copy()


# =========================================================
# حفظ البيانات في الملف
# =========================================================

def save_data():

    try:

        with open(
            DATA_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                students,
                file,
                ensure_ascii=False,
                indent=4
            )

    except Exception as error:

        messagebox.showerror(
            "خطأ",
            f"لم يتم حفظ البيانات:\n{error}"
        )


# =========================================================
# تحميل الطلاب
# =========================================================

students = load_data()


# الطالب المختار حالياً
selected_student = None


# =========================================================
# اختيار طالب عشوائي
# =========================================================

def choose_random_student():

    global selected_student


    if len(students) == 0:

        messagebox.showwarning(
            "تنبيه",
            "لا يوجد طلاب في القائمة!"
        )

        return


    # اختيار اسم عشوائي
    selected_student = random.choice(
        list(students.keys())
    )


    # عرض الاسم
    student_label.config(
        text=selected_student
    )


    # عرض الرصيد
    score_label.config(
        text=f"الرصيد الحالي: {students[selected_student]} نقطة"
    )


    status_label.config(
        text=f"🎯 تم اختيار {selected_student} - اطرح السؤال"
    )


# =========================================================
# إجابة صحيحة
# =========================================================

def correct_answer():

    global selected_student


    if selected_student is None:

        messagebox.showwarning(
            "تنبيه",
            "يجب اختيار طالب أولاً."
        )

        return


    # إضافة نقطة
    students[selected_student] += 1


    # -----------------------------------------
    # حفظ النقطة مباشرة في الملف
    # -----------------------------------------

    save_data()


    # تحديث الرصيد
    score_label.config(
        text=f"الرصيد الحالي: {students[selected_student]} نقطة"
    )


    status_label.config(
        text=(
            f"✅ إجابة صحيحة - "
            f"{selected_student} حصل على نقطة"
        )
    )


    # تحديث ترتيب الطلاب
    update_scoreboard()


# =========================================================
# إجابة خاطئة
# =========================================================

def wrong_answer():

    global selected_student


    if selected_student is None:

        messagebox.showwarning(
            "تنبيه",
            "يجب اختيار طالب أولاً."
        )

        return


    status_label.config(
        text=(
            f"❌ إجابة خاطئة - "
            f"لم يحصل {selected_student} على نقطة"
        )
    )


# =========================================================
# تحديث جدول ترتيب الطلاب
# =========================================================

def update_scoreboard():

    # حذف العناصر القديمة
    scoreboard_listbox.delete(
        0,
        tk.END
    )


    # ترتيب الطلاب من الأعلى نقاطاً
    sorted_students = sorted(
        students.items(),
        key=lambda student: student[1],
        reverse=True
    )


    # عرض الطلاب
    for name, score in sorted_students:

        scoreboard_listbox.insert(
            tk.END,
            f"{name}          ⭐ {score}"
        )


# =========================================================
# إضافة طالب
# =========================================================

def add_student():

    name = name_entry.get().strip()


    if name == "":

        messagebox.showwarning(
            "تنبيه",
            "اكتب اسم الطالب."
        )

        return


    if name in students:

        messagebox.showinfo(
            "معلومة",
            "هذا الطالب موجود مسبقاً."
        )

        return


    # إضافة الطالب
    students[name] = 0


    # حفظ التعديل
    save_data()


    # تحديث الجدول
    update_scoreboard()


    # مسح الحقل
    name_entry.delete(
        0,
        tk.END
    )


    status_label.config(
        text=f"✅ تمت إضافة الطالب: {name}"
    )


# =========================================================
# حذف طالب
# =========================================================

def delete_student():

    global selected_student


    selected = scoreboard_listbox.curselection()


    if not selected:

        messagebox.showwarning(
            "تنبيه",
            "اختر طالباً من القائمة أولاً."
        )

        return


    index = selected[0]


    sorted_students = sorted(
        students.items(),
        key=lambda student: student[1],
        reverse=True
    )


    student_name = sorted_students[index][0]


    answer = messagebox.askyesno(
        "تأكيد الحذف",
        f"هل تريد حذف الطالب {student_name}؟"
    )


    if answer:

        # حذف الطالب
        del students[student_name]


        # حفظ التعديل
        save_data()


        # إذا كان هو الطالب المختار
        if selected_student == student_name:

            selected_student = None

            student_label.config(
                text="؟"
            )

            score_label.config(
                text="الرصيد الحالي: 0 نقطة"
            )


        update_scoreboard()


        status_label.config(
            text=f"🗑 تم حذف الطالب: {student_name}"
        )


# =========================================================
# تصفير جميع النقاط
# =========================================================

def reset_scores():

    global selected_student


    answer = messagebox.askyesno(
        "تأكيد",
        "هل أنت متأكد من تصفير نقاط جميع الطلاب؟"
    )


    if not answer:

        return


    # تصفير جميع الطلاب
    for student in students:

        students[student] = 0


    # حفظ النتيجة
    save_data()


    # تحديث الجدول
    update_scoreboard()


    # تحديث رصيد الطالب الحالي
    if selected_student is not None:

        score_label.config(
            text="الرصيد الحالي: 0 نقطة"
        )


    status_label.config(
        text="🔄 تم تصفير جميع النقاط"
    )


# =========================================================
# الضغط على Enter لإضافة طالب
# =========================================================

def enter_pressed(event):

    add_student()


# =========================================================
# عند إغلاق البرنامج
# =========================================================

def close_program():

    # حفظ البيانات قبل الإغلاق
    save_data()

    root.destroy()


# =========================================================
# إنشاء النافذة
# =========================================================

root = tk.Tk()


root.title(
    "نظام اختيار الطلاب والنقاط"
)


root.geometry(
    "760x750"
)


root.resizable(
    False,
    False
)


root.configure(
    bg="#f1f5f9"
)


# عند الضغط على X
root.protocol(
    "WM_DELETE_WINDOW",
    close_program
)


# =========================================================
# رأس البرنامج
# =========================================================

header = tk.Frame(
    root,
    bg="#1e293b",
    height=100
)


header.pack(
    fill="x"
)


header.pack_propagate(
    False
)


title = tk.Label(
    header,
    text="🎓 نظام اختيار الطلاب والنقاط",
    font=(
        "Arial",
        24,
        "bold"
    ),
    bg="#1e293b",
    fg="white"
)


title.pack(
    pady=(20, 5)
)


subtitle = tk.Label(
    header,
    text="Random Student & Score System",
    font=(
        "Arial",
        11
    ),
    bg="#1e293b",
    fg="#cbd5e1"
)


subtitle.pack()


# =========================================================
# الطالب المختار
# =========================================================

student_frame = tk.Frame(
    root,
    bg="white"
)


student_frame.pack(
    fill="x",
    padx=30,
    pady=(20, 10)
)


tk.Label(
    student_frame,
    text="الطالب المختار",
    font=(
        "Arial",
        14,
        "bold"
    ),
    bg="white",
    fg="#64748b"
).pack(
    pady=(15, 5)
)


student_label = tk.Label(
    student_frame,
    text="؟",
    font=(
        "Arial",
        34,
        "bold"
    ),
    bg="white",
    fg="#2563eb"
)


student_label.pack(
    pady=5
)


score_label = tk.Label(
    student_frame,
    text="الرصيد الحالي: 0 نقطة",
    font=(
        "Arial",
        14,
        "bold"
    ),
    bg="white",
    fg="#475569"
)


score_label.pack(
    pady=(0, 15)
)


# =========================================================
# زر اختيار الطالب
# =========================================================

choose_button = tk.Button(
    root,
    text="🎲 اختر طالباً عشوائياً",
    command=choose_random_student,
    font=(
        "Arial",
        16,
        "bold"
    ),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    cursor="hand2",
    relief="flat"
)


choose_button.pack(
    fill="x",
    padx=30,
    pady=5,
    ipady=12
)


# =========================================================
# أزرار الإجابة
# =========================================================

answer_frame = tk.Frame(
    root,
    bg="#f1f5f9"
)


answer_frame.pack(
    fill="x",
    padx=30,
    pady=10
)


correct_button = tk.Button(
    answer_frame,
    text="✅ إجابة صحيحة +1",
    command=correct_answer,
    font=(
        "Arial",
        14,
        "bold"
    ),
    bg="#16a34a",
    fg="white",
    activebackground="#15803d",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)


correct_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 5),
    ipady=10
)


wrong_button = tk.Button(
    answer_frame,
    text="❌ إجابة خاطئة",
    command=wrong_answer,
    font=(
        "Arial",
        14,
        "bold"
    ),
    bg="#dc2626",
    fg="white",
    activebackground="#b91c1c",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)


wrong_button.pack(
    side="right",
    fill="x",
    expand=True,
    padx=(5, 0),
    ipady=10
)


# =========================================================
# إضافة طالب
# =========================================================

add_frame = tk.Frame(
    root,
    bg="#f1f5f9"
)


add_frame.pack(
    fill="x",
    padx=30,
    pady=5
)


name_entry = tk.Entry(
    add_frame,
    font=(
        "Arial",
        14
    ),
    justify="center"
)


name_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8
)


name_entry.bind(
    "<Return>",
    enter_pressed
)


add_button = tk.Button(
    add_frame,
    text="➕ إضافة طالب",
    command=add_student,
    font=(
        "Arial",
        12,
        "bold"
    ),
    bg="#0284c7",
    fg="white",
    relief="flat",
    cursor="hand2"
)


add_button.pack(
    side="right",
    padx=(10, 0),
    ipady=7,
    ipadx=10
)


# =========================================================
# عنوان الترتيب
# =========================================================

scoreboard_title = tk.Label(
    root,
    text="🏆 ترتيب الطلاب",
    font=(
        "Arial",
        17,
        "bold"
    ),
    bg="#f1f5f9",
    fg="#1e293b"
)


scoreboard_title.pack(
    pady=(15, 5)
)


# =========================================================
# قائمة الطلاب والنقاط
# =========================================================

scoreboard_listbox = tk.Listbox(
    root,
    font=(
        "Arial",
        14
    ),
    justify="center",
    bg="white",
    fg="#1e293b",
    selectbackground="#2563eb",
    selectforeground="white",
    height=8,
    bd=0,
    highlightthickness=0
)


scoreboard_listbox.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=5
)


# =========================================================
# أزرار الإدارة
# =========================================================

control_frame = tk.Frame(
    root,
    bg="#f1f5f9"
)


control_frame.pack(
    fill="x",
    padx=30,
    pady=5
)


delete_button = tk.Button(
    control_frame,
    text="🗑 حذف الطالب",
    command=delete_student,
    font=(
        "Arial",
        11,
        "bold"
    ),
    bg="#64748b",
    fg="white",
    relief="flat",
    cursor="hand2"
)


delete_button.pack(
    side="left",
    fill="x",
    expand=True,
    padx=(0, 5),
    ipady=7
)


reset_button = tk.Button(
    control_frame,
    text="🔄 تصفير جميع النقاط",
    command=reset_scores,
    font=(
        "Arial",
        11,
        "bold"
    ),
    bg="#f59e0b",
    fg="white",
    relief="flat",
    cursor="hand2"
)


reset_button.pack(
    side="right",
    fill="x",
    expand=True,
    padx=(5, 0),
    ipady=7
)


# =========================================================
# شريط الحالة
# =========================================================

status_label = tk.Label(
    root,
    text="جاهز 🎯 اختر طالباً للبدء",
    font=(
        "Arial",
        11
    ),
    bg="#e2e8f0",
    fg="#475569"
)


status_label.pack(
    fill="x",
    ipady=8
)


# =========================================================
# عرض بيانات الطلاب المحفوظة
# =========================================================

update_scoreboard()


# =========================================================
# تشغيل البرنامج
# =========================================================

root.mainloop()