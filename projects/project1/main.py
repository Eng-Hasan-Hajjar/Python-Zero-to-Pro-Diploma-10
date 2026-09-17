import tkinter as tk
from tkinter import messagebox
import random


# ==========================================
# قائمة الطلاب الافتراضية
# يمكنك تعديلها مباشرة من هنا أيضاً
# ==========================================
students = [
    "أريج",
    "ياسمين",
    "يونس",
    "زهراء",
    "كيندا",
    "مجد"
]


# ==========================================
# اختيار طالب عشوائي
# ==========================================
def choose_random_student():
    if not students:
        messagebox.showwarning(
            "تنبيه",
            "لا يوجد طلاب في القائمة!"
        )
        return

    selected_student = random.choice(students)

    result_label.config(
        text=selected_student
    )

    status_label.config(
        text=f"🎉 تم اختيار الطالب/الطالبة: {selected_student}"
    )


# ==========================================
# إضافة طالب
# ==========================================
def add_student():
    name = name_entry.get().strip()

    if not name:
        messagebox.showwarning(
            "تنبيه",
            "الرجاء كتابة اسم الطالب."
        )
        return

    if name in students:
        messagebox.showinfo(
            "معلومة",
            "هذا الاسم موجود مسبقاً."
        )
        return

    students.append(name)

    students_listbox.insert(
        tk.END,
        name
    )

    name_entry.delete(
        0,
        tk.END
    )

    update_student_count()

    status_label.config(
        text=f"✅ تم إضافة: {name}"
    )


# ==========================================
# حذف طالب
# ==========================================
def delete_student():
    selected = students_listbox.curselection()

    if not selected:
        messagebox.showwarning(
            "تنبيه",
            "اختر اسماً من القائمة أولاً."
        )
        return

    index = selected[0]
    name = students_listbox.get(index)

    answer = messagebox.askyesno(
        "تأكيد الحذف",
        f"هل تريد حذف {name}؟"
    )

    if answer:
        students_listbox.delete(index)

        if name in students:
            students.remove(name)

        update_student_count()

        status_label.config(
            text=f"🗑 تم حذف: {name}"
        )


# ==========================================
# تحديث عدد الطلاب
# ==========================================
def update_student_count():
    count_label.config(
        text=f"عدد الطلاب: {len(students)}"
    )


# ==========================================
# الضغط على Enter لإضافة الاسم
# ==========================================
def press_enter(event):
    add_student()


# ==========================================
# إنشاء النافذة الرئيسية
# ==========================================
root = tk.Tk()

root.title("اختيار طالب عشوائي")

root.geometry("700x650")

root.resizable(False, False)

root.configure(
    bg="#f1f5f9"
)


# ==========================================
# العنوان الرئيسي
# ==========================================
header_frame = tk.Frame(
    root,
    bg="#1e293b",
    height=100
)

header_frame.pack(
    fill="x"
)

header_frame.pack_propagate(False)


title_label = tk.Label(
    header_frame,
    text="🎓 اختيار طالب عشوائي",
    font=(
        "Arial",
        24,
        "bold"
    ),
    bg="#1e293b",
    fg="white"
)

title_label.pack(
    pady=(20, 5)
)


subtitle_label = tk.Label(
    header_frame,
    text="Random Student Picker",
    font=(
        "Arial",
        11
    ),
    bg="#1e293b",
    fg="#cbd5e1"
)

subtitle_label.pack()


# ==========================================
# منطقة النتيجة
# ==========================================
result_frame = tk.Frame(
    root,
    bg="white",
    bd=0
)

result_frame.pack(
    fill="x",
    padx=30,
    pady=(25, 10)
)


result_title = tk.Label(
    result_frame,
    text="الطالب المختار",
    font=(
        "Arial",
        14,
        "bold"
    ),
    bg="white",
    fg="#64748b"
)

result_title.pack(
    pady=(15, 5)
)


result_label = tk.Label(
    result_frame,
    text="؟",
    font=(
        "Arial",
        32,
        "bold"
    ),
    bg="white",
    fg="#2563eb",
    height=2
)

result_label.pack()


# ==========================================
# زر الاختيار
# ==========================================
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
    relief="flat",
    height=2
)

choose_button.pack(
    fill="x",
    padx=30,
    pady=10
)


# ==========================================
# إطار إدارة الطلاب
# ==========================================
management_frame = tk.Frame(
    root,
    bg="#f1f5f9"
)

management_frame.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=10
)


management_title = tk.Label(
    management_frame,
    text="إدارة أسماء الطلاب",
    font=(
        "Arial",
        16,
        "bold"
    ),
    bg="#f1f5f9",
    fg="#1e293b"
)

management_title.pack(
    pady=(5, 10)
)


# ==========================================
# حقل إضافة اسم
# ==========================================
input_frame = tk.Frame(
    management_frame,
    bg="#f1f5f9"
)

input_frame.pack(
    fill="x",
    pady=5
)


name_entry = tk.Entry(
    input_frame,
    font=(
        "Arial",
        14
    ),
    justify="center",
    bd=1,
    relief="solid"
)

name_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=8
)


add_button = tk.Button(
    input_frame,
    text="➕ إضافة",
    command=add_student,
    font=(
        "Arial",
        12,
        "bold"
    ),
    bg="#16a34a",
    fg="white",
    activebackground="#15803d",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    width=10
)

add_button.pack(
    side="right",
    padx=(10, 0),
    ipady=6
)


# الضغط على Enter
name_entry.bind(
    "<Return>",
    press_enter
)


# ==========================================
# عدد الطلاب
# ==========================================
count_label = tk.Label(
    management_frame,
    text="",
    font=(
        "Arial",
        11,
        "bold"
    ),
    bg="#f1f5f9",
    fg="#64748b"
)

count_label.pack(
    pady=5
)


# ==========================================
# قائمة الطلاب
# ==========================================
list_frame = tk.Frame(
    management_frame,
    bg="white"
)

list_frame.pack(
    fill="both",
    expand=True,
    pady=5
)


scrollbar = tk.Scrollbar(
    list_frame
)

scrollbar.pack(
    side="right",
    fill="y"
)


students_listbox = tk.Listbox(
    list_frame,
    font=(
        "Arial",
        14
    ),
    justify="center",
    selectbackground="#2563eb",
    selectforeground="white",
    bg="white",
    fg="#1e293b",
    bd=0,
    highlightthickness=0,
    yscrollcommand=scrollbar.set
)

students_listbox.pack(
    side="left",
    fill="both",
    expand=True,
    padx=5,
    pady=5
)


scrollbar.config(
    command=students_listbox.yview
)


# إضافة الطلاب الافتراضيين
for student in students:
    students_listbox.insert(
        tk.END,
        student
    )


# ==========================================
# زر الحذف
# ==========================================
delete_button = tk.Button(
    management_frame,
    text="🗑 حذف الاسم المحدد",
    command=delete_student,
    font=(
        "Arial",
        12,
        "bold"
    ),
    bg="#dc2626",
    fg="white",
    activebackground="#b91c1c",
    activeforeground="white",
    relief="flat",
    cursor="hand2"
)

delete_button.pack(
    fill="x",
    pady=8,
    ipady=7
)


# ==========================================
# شريط الحالة
# ==========================================
status_label = tk.Label(
    root,
    text="جاهز للاختيار 🎯",
    font=(
        "Arial",
        11
    ),
    bg="#e2e8f0",
    fg="#475569",
    anchor="center"
)

status_label.pack(
    fill="x",
    ipady=8
)


# تحديث العداد
update_student_count()


# وضع المؤشر في حقل الاسم
name_entry.focus()


# ==========================================
# تشغيل البرنامج
# ==========================================
root.mainloop()