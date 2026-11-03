#Project: The Secure Massenger (symmetric Encryption tool)
#Author:Abdullah Hossam Shaban Kamel 
#Date : jan,2026
#Description:
#     Inspired by historical 'massengers' and the need for data privacy,
#     this script implements a custom Affine Cipher.
#     it uses modular Arthmetic to transform next into secure Code.
# Technical Logic
#          - Uses Modular Multiplicative Inverse for decryption.
#          - Configurable (e.g. , Mod 50 for English titel's and Characters).
#          - Designed for lightweight, secure massage exchange. 
#==============================================================================================================
import customtkinter as ctk

# إعدادات المظهر العام
ctk.set_appearance_mode("Dark")

ctk.set_default_color_theme("dark-blue")

class ModernAffineApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Secure Messenger // Affine Protocol")

        self.geometry("600x580")

        self.minsize(450, 480) # أقل حجم ممكن للنافذة عشان ما تبوظش
        
        # خلفية النافذة الداكنة
        self.configure(fg_color=("#0b0f19", "#07090e"))

        # جدول الرموز الخاص بك (50 عنصر)
        self.Dect = {
            "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
            "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26," ":27,
            "!":28,":":29,"%":30,"$":31,"<":32,">":33,";":34,".":35,"\\":36,"=":37,"+":38,"*":39,"#":40,"}":41,
            "?":42,"|":43,"(":44,")":45,"^":46,"_":47,"-":48,"/":49,"@":50
        }
        self.inve_Dect = {v:k for k,v in self.Dect.items()}

        # تكوين الشبكة الرئيسية للنافذة عشان تتمدد مع التكبير والتصغير
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # الحاوية الرئيسية (Glassmorphic Container) تتمدد مع تغيير حجم النافذة
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color=("#111827", "#0d1322"), 
            corner_radius=20, 
            border_width=1, 
            border_color="#1f293d"
        )
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

        # ضبط أبعاد الشبكة داخل الـ Frame الرئيسي
        self.main_frame.grid_rowconfigure(3, weight=1) # صف النتيجة هو اللي يتمدد رأسياً
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # 1. العنوان الرئيسي
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="🛡️ SECURE AFFINE PROTOCOL", 
            font=("Consolas", 18, "bold"),
            text_color="#38bdf8"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(30, 20), sticky="n")

        # 2. إدخال النص
        self.input_label = ctk.CTkLabel(self.main_frame, text="Enter your message:", font=("Arial", 13, "bold"), text_color="#94a3b8")
        self.input_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=35)
        
        self.input_entry = ctk.CTkEntry(
            self.main_frame, 
            height=45, 
            corner_radius=10,
            fg_color="#090d16",
            border_color="#334155",
            text_color="#f8fafc",
            placeholder_text="Type your message here..."
        )
        self.input_entry.grid(row=2, column=0, columnspan=2, sticky="ew", padx=35, pady=(5, 15))

        # 3. أزرار التحكم (تشفير وفك تشفير) - متجاوبة
        self.encrypt_btn = ctk.CTkButton(
            self.main_frame, 
            text="🔒 Encrypt Data", 
            command=self.encrypt_text, 
            height=42,
            corner_radius=10,
            fg_color="#0284c7",
            hover_color="#0369a1",
            font=("Arial", 13, "bold")
        )
        self.encrypt_btn.grid(row=3, column=0, sticky="ew", padx=(35, 10), pady=10)

        self.decrypt_btn = ctk.CTkButton(
            self.main_frame, 
            text="🔓 Decrypt Data", 
            command=self.decrypt_text, 
            height=42,
            corner_radius=10,
            fg_color="#1e293b",
            hover_color="#334155",
            text_color="#f8fafc",
            font=("Arial", 13, "bold"),
            border_width=1,
            border_color="#475569"
        )
        self.decrypt_btn.grid(row=3, column=1, sticky="ew", padx=(10, 35), pady=10)

        # 4. إخراج النتيجة (تتخذ مساحة مرنة عند تكبير الشاشة)
        self.output_label = ctk.CTkLabel(self.main_frame, text="Result Output:", font=("Arial", 13, "bold"), text_color="#94a3b8")
        self.output_label.grid(row=4, column=0, columnspan=2, sticky="w", padx=35, pady=(15, 0))
        
        self.output_textbox = ctk.CTkTextbox(
            self.main_frame, 
            corner_radius=10,
            fg_color="#090d16",
            border_color="#334155",
            text_color="#38bdf8",
            font=("Consolas", 14)
        )
        self.output_textbox.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=35, pady=(5, 30))
        self.output_textbox.configure(state="disabled")

    def encrypt_text(self):

        message = self.input_entry.get().lower()

        encr_massage = ""

        for i in message:

            if i in self.Dect:

                x = self.Dect[i]

                f_x = x * 3 % 50  

                if f_x in self.inve_Dect:

                    encr_massage += self.inve_Dect[f_x]
        
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("1.0", encr_massage)
        self.output_textbox.configure(state="disabled")

    def decrypt_text(self):

        encr_massage = self.input_entry.get().lower()

        orgnal_text = ""

        for i in encr_massage:

            if i in self.Dect:

                back = self.Dect[i] * 17 % 50  

                if back in self.inve_Dect:

                    orgnal_text += self.inve_Dect[back]
        
        self.output_textbox.configure(state="normal")
        self.output_textbox.delete("1.0", "end")
        self.output_textbox.insert("1.0", orgnal_text)
        self.output_textbox.configure(state="disabled")

if __name__ == "__main__":

    app = ModernAffineApp()

    app.mainloop()


