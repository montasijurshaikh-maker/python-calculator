import tkinter as tk
from tkinter import font
import math

# ============================================
#   🐍 Python Calculator App - Tkinter GUI
#   Bangla Comments দিয়ে বোঝানো হয়েছে
# ============================================

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Python Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#0d0d0d")

        # ক্যালকুলেটরের State
        self.expression = ""       # এখন পর্যন্ত যা লেখা হয়েছে
        self.result_shown = False  # Result দেখানো হয়েছে কিনা
        self.history = []          # হিস্ট্রি লিস্ট

        self.build_ui()

    # ============================================
    #   UI তৈরি করা
    # ============================================
    def build_ui(self):

        # Title Bar
        title_frame = tk.Frame(self.root, bg="#111", pady=8)
        title_frame.pack(fill="x")
        tk.Label(
            title_frame, text="🐍 Python Calculator",
            bg="#111", fg="#00ff41",
            font=("Courier New", 13, "bold")
        ).pack()

        # ডিসপ্লে এলাকা
        display_frame = tk.Frame(self.root, bg="#0d0d0d", padx=15, pady=10)
        display_frame.pack(fill="x")

        # ছোট Expression দেখানোর জায়গা
        self.expr_label = tk.Label(
            display_frame, text="",
            bg="#0d0d0d", fg="#2a4a2a",
            font=("Courier New", 11),
            anchor="e"
        )
        self.expr_label.pack(fill="x")

        # বড় Result দেখানোর জায়গা
        self.display_var = tk.StringVar(value="0")
        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            bg="#0d0d0d", fg="#00ff41",
            font=("Courier New", 36, "bold"),
            anchor="e",
            wraplength=340
        )
        self.display.pack(fill="x")

        # বিভাজক লাইন
        tk.Frame(self.root, bg="#1a3a1a", height=1).pack(fill="x", padx=15)

        # বাটন এলাকা
        btn_frame = tk.Frame(self.root, bg="#0d0d0d", padx=12, pady=12)
        btn_frame.pack()

        # বাটনের রং ও স্টাইল
        style = {
            "num":    {"bg":"#141f14", "fg":"#00dd00", "active":"#1a2a1a"},
            "op":     {"bg":"#1a1a0a", "fg":"#ffaa00", "active":"#2a2a1a"},
            "eq":     {"bg":"#006600", "fg":"#00ff00", "active":"#008800"},
            "clr":    {"bg":"#1a0a0a", "fg":"#ff5555", "active":"#2a1a1a"},
            "sci":    {"bg":"#0a1020", "fg":"#5599ff", "active":"#1a2030"},
            "hist":   {"bg":"#0a1a1a", "fg":"#44cccc", "active":"#1a2a2a"},
        }

        # বাটন লেআউট (text, action, style, colspan)
        buttons = [
            # Row 1 - Scientific
            ("sin",  "sin",  "sci", 1), ("cos",  "cos",  "sci", 1),
            ("tan",  "tan",  "sci", 1), ("√",    "sqrt", "sci", 1),

            # Row 2 - Scientific
            ("x²",   "sq",   "sci", 1), ("xʸ",   "**",   "op",  1),
            ("π",    "pi",   "sci", 1), ("(",    "(",    "op",  1),

            # Row 3
            ("C",    "C",    "clr", 1), ("⌫",   "back", "clr", 1),
            ("%",    "%",    "op",  1), ("÷",    "/",    "op",  1),

            # Row 4
            ("7",    "7",    "num", 1), ("8",    "8",    "num", 1),
            ("9",    "9",    "num", 1), ("×",    "*",    "op",  1),

            # Row 5
            ("4",    "4",    "num", 1), ("5",    "5",    "num", 1),
            ("6",    "6",    "num", 1), ("−",    "-",    "op",  1),

            # Row 6
            ("1",    "1",    "num", 1), ("2",    "2",    "num", 1),
            ("3",    "3",    "num", 1), ("+",    "+",    "op",  1),

            # Row 7
            ("±",    "neg",  "op",  1), ("0",    "0",    "num", 1),
            (".",    ".",    "num", 1), ("=",    "=",    "eq",  1),

            # Row 8 - History
            ("📋 History",  "history", "hist", 2),
            (")",    ")",    "op",  1),
            ("CE",   "CE",   "clr", 1),
        ]

        # বাটন তৈরি করা
        row, col = 0, 0
        for (text, action, stype, span) in buttons:
            s = style[stype]
            btn = tk.Button(
                btn_frame,
                text=text,
                width=5 * span,
                height=2,
                bg=s["bg"],
                fg=s["fg"],
                activebackground=s["active"],
                activeforeground=s["fg"],
                font=("Courier New", 13, "bold"),
                relief="flat",
                cursor="hand2",
                command=lambda a=action: self.press(a)
            )
            btn.grid(
                row=row, column=col,
                columnspan=span,
                padx=4, pady=4,
                sticky="nsew"
            )

            # Hover effect
            btn.bind("<Enter>", lambda e, b=btn, s=s: b.config(bg=s["active"]))
            btn.bind("<Leave>", lambda e, b=btn, s=s: b.config(bg=s["bg"]))

            col += span
            if col >= 4:
                col = 0
                row += 1

        # Keyboard সাপোর্ট
        self.root.bind("<Key>", self.key_press)
        self.root.focus_set()

    # ============================================
    #   বাটন Press হলে কী করবে
    # ============================================
    def press(self, action):

        # Clear সব
        if action == "C":
            self.expression = ""
            self.display_var.set("0")
            self.expr_label.config(text="")
            self.result_shown = False

        # শেষ অক্ষর মুছো
        elif action == "back":
            if self.result_shown:
                self.expression = ""
                self.display_var.set("0")
                self.result_shown = False
            else:
                self.expression = self.expression[:-1]
                self.display_var.set(self.expression or "0")

        # Current Entry মুছো
        elif action == "CE":
            self.expression = ""
            self.display_var.set("0")

        # = চাপলে হিসাব করো
        elif action == "=":
            self.calculate()

        # বর্গমূল
        elif action == "sqrt":
            try:
                val = float(eval(self.expression or "0"))
                if val < 0:
                    self.display_var.set("Error!")
                    self.expression = ""
                else:
                    result = math.sqrt(val)
                    result = self.format_result(result)
                    self.expr_label.config(text=f"√({self.expression}) =")
                    self.history.append(f"√({self.expression}) = {result}")
                    self.expression = str(result)
                    self.display_var.set(result)
                    self.result_shown = True
            except:
                self.display_var.set("Error!")
                self.expression = ""

        # বর্গ
        elif action == "sq":
            try:
                val = float(eval(self.expression or "0"))
                result = val ** 2
                result = self.format_result(result)
                self.expr_label.config(text=f"({self.expression})² =")
                self.history.append(f"({self.expression})² = {result}")
                self.expression = str(result)
                self.display_var.set(result)
                self.result_shown = True
            except:
                self.display_var.set("Error!")
                self.expression = ""

        # sin, cos, tan
        elif action in ("sin", "cos", "tan"):
            try:
                val = float(eval(self.expression or "0"))
                rad = math.radians(val)
                result = getattr(math, action)(rad)
                result = self.format_result(result)
                self.expr_label.config(text=f"{action}({self.expression}°) =")
                self.history.append(f"{action}({self.expression}°) = {result}")
                self.expression = str(result)
                self.display_var.set(result)
                self.result_shown = True
            except:
                self.display_var.set("Error!")
                self.expression = ""

        # π যোগ করো
        elif action == "pi":
            if self.result_shown:
                self.expression = str(math.pi)
                self.result_shown = False
            else:
                self.expression += str(math.pi)
            self.display_var.set(self.expression)

        # Negative/Positive টগল
        elif action == "neg":
            try:
                val = float(eval(self.expression or "0"))
                val = -val
                self.expression = str(self.format_result(val))
                self.display_var.set(self.expression)
            except:
                pass

        # History দেখাও
        elif action == "history":
            self.show_history()

        # সাধারণ Input (সংখ্যা বা অপারেটর)
        else:
            if self.result_shown and action not in ("+", "-", "*", "/", "**", "%"):
                self.expression = ""
                self.result_shown = False
            self.expression += action
            self.display_var.set(self.expression)
            self.expr_label.config(text="")

    # ============================================
    #   হিসাব করা
    # ============================================
    def calculate(self):
        if not self.expression:
            return
        try:
            expr_display = self.expression
            # eval দিয়ে হিসাব
            result = eval(self.expression)
            result = self.format_result(result)

            # হিস্ট্রিতে রাখো
            self.history.append(f"{expr_display} = {result}")
            if len(self.history) > 20:
                self.history.pop(0)

            self.expr_label.config(text=f"{expr_display} =")
            self.display_var.set(str(result))
            self.expression = str(result)
            self.result_shown = True

            # রেজাল্ট সবুজ করো
            self.display.config(fg="#00ff41")

        except ZeroDivisionError:
            self.display_var.set("÷ 0 Error!")
            self.expression = ""
            self.display.config(fg="#ff5555")
        except Exception:
            self.display_var.set("Error!")
            self.expression = ""
            self.display.config(fg="#ff5555")

        # ০.৫ সেকেন্ড পর রং ঠিক করো
        self.root.after(500, lambda: self.display.config(fg="#00ff41"))

    # ============================================
    #   ফলাফল ফরম্যাট করা
    # ============================================
    def format_result(self, result):
        if isinstance(result, float):
            if result == int(result):
                return int(result)
            return round(result, 10)
        return result

    # ============================================
    #   History Window
    # ============================================
    def show_history(self):
        win = tk.Toplevel(self.root)
        win.title("📋 Calculation History")
        win.configure(bg="#0d0d0d")
        win.geometry("320x400")
        win.resizable(False, False)

        tk.Label(
            win, text="📋 History",
            bg="#0d0d0d", fg="#44cccc",
            font=("Courier New", 14, "bold"),
            pady=10
        ).pack()

        tk.Frame(win, bg="#1a3a3a", height=1).pack(fill="x", padx=15)

        frame = tk.Frame(win, bg="#0d0d0d")
        frame.pack(fill="both", expand=True, padx=15, pady=10)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(
            frame,
            bg="#0a0d0a", fg="#00cc00",
            font=("Courier New", 11),
            selectbackground="#1a3a1a",
            relief="flat",
            yscrollcommand=scrollbar.set
        )
        listbox.pack(fill="both", expand=True)
        scrollbar.config(command=listbox.yview)

        if self.history:
            for item in reversed(self.history):
                listbox.insert("end", f"  {item}")
        else:
            listbox.insert("end", "  কোনো history নেই!")

        # History তে ক্লিক করলে ক্যালকুলেটরে বসবে
        def use_result(event):
            sel = listbox.curselection()
            if sel:
                item = listbox.get(sel[0]).strip()
                if "=" in item:
                    result = item.split("=")[-1].strip()
                    self.expression = result
                    self.display_var.set(result)
                    self.result_shown = True
                    win.destroy()

        listbox.bind("<Double-Button-1>", use_result)

        tk.Button(
            win, text="🗑️ Clear History",
            bg="#1a0a0a", fg="#ff5555",
            font=("Courier New", 11),
            relief="flat", cursor="hand2",
            command=lambda: [self.history.clear(), win.destroy()]
        ).pack(pady=10)

    # ============================================
    #   Keyboard সাপোর্ট
    # ============================================
    def key_press(self, event):
        key = event.char
        keysym = event.keysym

        if key in "0123456789.+-*/()%":
            self.press(key)
        elif key == "\r" or keysym == "Return":
            self.press("=")
        elif keysym == "BackSpace":
            self.press("back")
        elif keysym == "Escape":
            self.press("C")


# ============================================
#   Main — এখান থেকে প্রোগ্রাম শুরু হয়
# ============================================
if __name__ == "__main__":
    root = tk.Tk()

    # Window মাঝখানে রাখো
    window_width = 380
    window_height = 620
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - window_width) // 2
    y = (screen_h - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    app = Calculator(root)
    root.mainloop()