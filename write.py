import tkinter as tk
from tkinter import scrolledtext
import arabic_reshaper
from bidi.algorithm import get_display
import datetime

# --- قواميس الصفوف ---
dict_row_1 = {
    '`': 'ذ', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', 
    '6': '6', '7': '7', '8': '8', '9': '9', '0': '0', '-': '-', '=': '=',
    '~': 'ّ', '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', 
    '^': '^', '&': '&', '*': '*', '(': '(', ')': ')', '_': '_', '+': '+'
}

dict_row_2 = {
    'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 
    'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د', '\\': '\\',
    'Q': 'َ', 'W': 'ً', 'E': 'ُ', 'R': 'ٌ', 'T': 'لإ', 'Y': 'إ', 
    'U': '‘', 'I': '÷', 'O': '×', 'P': '؛', '{': '<', '}': '>', '|': '|', 'm': 'ة'
}

dict_row_3 = {
    'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا', 
    'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ك', "'": 'ط',
    'A': 'ِ', 'S': 'ٍ', 'D': 'أ', 'F': 'ـ', 'G': '،', 'H': '/', 
    'J': 'ُ', 'K': 'ً', 'L': 'َ', ':': ':', '"': '"'
}

dict_row_4 = {
    'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 
    ',': 'و', '.': 'ز', '/': 'ظ', '?': '؟',
    'Z': '~', 'X': 'ْ', 'C': '}', 'V': '{', 'B': 'لآ', 
    'N': ',', 'M': 'و', '<': '؟', '>': '؟'
}

en_to_ar_dict = {}
en_to_ar_dict.update(dict_row_1)
en_to_ar_dict.update(dict_row_2)
en_to_ar_dict.update(dict_row_3)
en_to_ar_dict.update(dict_row_4)

ar_to_en_dict = {v: k for k, v in en_to_ar_dict.items()}

# --- دالة الترجمة ومعالجة النصوص ---
def translate_text():
    input_str = entry_box.get("1.0", tk.END).strip()
    if not input_str:
        return
    
    store = ""
    for i in input_str:
        if i in en_to_ar_dict:
            store += en_to_ar_dict[i]
        elif i in ar_to_en_dict:
            store += ar_to_en_dict[i]
        else:
            store += i

    # معالجة النص لو الناتج عربي لضمان عرضه متصلاً
    if any('\u0600' <= c <= '\u06ff' for c in store):
        reshaped_text = arabic_reshaper.reshape(store)
        final_output = get_display(reshaped_text)
        # جعل الناتج محاذاة لليمين لو النص عربي
        output_box.tag_configure("align", justify="right")
    else:
        final_output = store
        # جعل الناتج محاذاة لليسار لو النص إنجليزي
        output_box.tag_configure("align", justify="left")

    # عرض النتيجة في مربع الإخراج
    output_box.config(state=tk.NORMAL)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, final_output, "align")
    output_box.config(state=tk.DISABLED)

    # إضافة سجل النشاط المؤقت (بالإنجليزية لتجنب مشاكل العرض)
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    log_text = f"[{current_time}] Text translated successfully.\n"
    
    history_box.config(state=tk.NORMAL)
    history_box.insert(tk.END, log_text)
    history_box.see(tk.END)
    history_box.config(state=tk.DISABLED)

# --- إعداد الواجهة الرسومية باللغة الإنجليزية ---
root = tk.Tk()
root.title("Keyboard  Translator")
root.geometry("600x700")
root.configure(bg="#2b2b2b")

# عنوان البرنامج
title_label = tk.Label(root, text="Keyboard Translator", font=("Times New Roman", 14, "bold"), fg="#ffffff", bg="#2b2b2b")
title_label.pack(pady=10)

# مربع إدخال النص
tk.Label(root, text="Enter Text Here:", fg="#aaaaaa", bg="#2b2b2b", anchor="w").pack(fill="x", padx=20)
entry_box = tk.Text(root, height=4, font=("Times New Roman", 12), bg="#3c3f41", fg="#ffffff", insertbackground="white")
entry_box.pack(fill="x", padx=20, pady=5)

# زر الترجمة
translate_btn = tk.Button(root, text="Translate & Process", font=("Times New Roman", 11, "bold"), bg="#4CAF50", fg="white", command=translate_text)
translate_btn.pack(pady=10)

# مربع الناتج
tk.Label(root, text="Result:", fg="#aaaaaa", bg="#2b2b2b", anchor="w").pack(fill="x", padx=20)
output_box = tk.Text(root, height=4, font=("Times New Roman", 12), bg="#3c3f41", fg="#ffffff", insertbackground="white")
output_box.pack(fill="x", padx=20, pady=5)

# سجل النشاط المؤقت
tk.Label(root, text="Activity Log:", fg="#aaaaaa", bg="#2b2b2b", anchor="w").pack(fill="x", padx=20)
history_box = scrolledtext.ScrolledText(root, height=6, font=("Consolas", 10), bg="#1e1e1e", fg="#00ff00")
history_box.pack(fill="x", padx=20, pady=5)

# تشغيل التطبيق
root.mainloop()