import customtkinter as ctk


class gui:

    def __init__(self, root):
        self.root = root
        self.root.title = 'Weather'
        self.root.geometry('400x300')

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('blue')

        self.label = ctk.CTkLabel(root, text='Enter location', font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(root, font=('Arial', 14))
        self.entry.pack(pady=5)

        self.weather_label = ctk.CTkLabel(root, text='', font=('Arial', 14))
        self.weather_label.pack(pady=10)

        self.button = ctk.CTkButton(root, text='Get Weather', command=self.get_weather, font=('Arial', 14))
        self.button.pack(pady=10)

    def get_weather(self):
        city = self.entry.get()
        self.weather_label.configure(text=f'Weather in {city} is fucking beautiful bruv')   # Test as placeholder

if __name__ == '__main__':
    root = ctk.CTk()
    app = gui(root)
    root.mainloop()

