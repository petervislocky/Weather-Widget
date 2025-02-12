import customtkinter as ctk


class gui(ctk.CTk):

    def __init__(self, get_weather):
        super().__init__()

        self.title = 'Weather'
        self.geometry('400x300')

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.label = ctk.CTkLabel(self, text='Enter location', font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.entry.pack(pady=5)

        self.weather_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.weather_label.pack(pady=10)

        self.button = ctk.CTkButton(self, text='Get Weather', command=get_weather, font=('Arial', 14))
        self.button.pack(pady=10)


if __name__ == '__main__':
    app = gui()
    app.mainloop()

