import customtkinter as ctk
from weather.get_weather import getWeather


class gui(ctk.CTk):

    def __init__(self, get_weather):
        super().__init__()

        self.get_weather = get_weather

        self.title('Weather')
        self.geometry('350x250')

        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('blue')

        self.label = ctk.CTkLabel(self, text='Enter location', font=('Arial', 14))
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, font=('Arial', 14))
        self.entry.pack(pady=5)

        self.weather_label = ctk.CTkLabel(self, text='', font=('Arial', 14))
        self.weather_label.pack(pady=10)

        self.button = ctk.CTkButton(self, text='Get Weather', command=self.pass_location, font=('Arial', 14))
        self.button.pack(pady=10)

        # So enter submits data in entry box
        self.bind('<Return>', lambda event: self.pass_location())

    def pass_location(self):
        '''
        Wrapper function for get_weather after a reference to it is stored in the class
        '''
        gw = getWeather()
        location = self.entry.get()
        if location:
            api_repsonse = self.get_weather(location)
            name, region, country, text, icon, temp_f, feelslike_f, wind_mph, temp_c, feelslike_c, wind_kph = gw.parse_weather(api_repsonse)
            if api_repsonse:
                formatted_weather = f'Temp: {temp_f}\N{DEGREE SIGN}F\nFeels like: {feelslike_f}\N{DEGREE SIGN}F\nCondition: {text}'
                self.weather_label.configure(text=formatted_weather)
            else:
                self.weather_label.configure('Error no proper data to display')
        else:
            self.weather_label.configure('No location given')
        


if __name__ == '__main__':
    app = gui()
    app.mainloop()

