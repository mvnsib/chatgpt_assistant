import customtkinter as ctk


class mainWindow:
    root = ctk.CTk()
    root.geometry("750x450")
    root.title("Bruce Assistant App")

    title_label = ctk.CTkLabel(
        root, text="Bruce", font=ctk.CTkFont(size=30, weight="bold"))
    title_label.pack(padx=10, pady=(40, 20))

    frame = ctk.CTkScrollableFrame(root, width=500, height=200)
    frame.pack()

    root.mainloop()
