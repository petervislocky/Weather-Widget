import customtkinter as ctk
from weather.get_weather import getWeather


class gui(ctk.CTk):

    def __init__(self, get_weather):
        super().__init__()

        # passing reference to get_weather func
        self.get_weather = get_weather

        self.title('Weather')
        self.geometry('350x250')

        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('blue')

        # main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=0)
        
        # location entry box
        self.entry = ctk.CTkEntry(self.main_frame, font=('Arial', 14))
        self.entry.grid(row=0, column=0 ,padx=(10,5), sticky='n')

        # 'Enter location' label
        self.label = ctk.CTkLabel(self.main_frame, text='Enter location', font=('Arial', 14))
        self.label.grid(row=1, column=0, columnspan=2, pady=10)

        # metric checkbox
        self.checkbox_status = ctk.BooleanVar()
        self.checkbox = ctk.CTkCheckBox(
                                        self.main_frame,
                                        text='Metric',
                                        variable=self.checkbox_status,
                                        font=('Arial', 12),
                                        checkbox_width=16,
                                        checkbox_height=16,
                                        border_width=1
                                        )
        self.checkbox.grid(row=0, column=1, padx=(5,0), sticky='e')

        # label that displays weather data once returned
        self.weather_label = ctk.CTkLabel(self.main_frame, text='', font=('Arial', 14))
        self.weather_label.grid(row=1, column=0, columnspan=2, pady=10, sticky='n')

        # 'Get weather' button
        self.button = ctk.CTkButton(self.main_frame, text='Get Weather', command=self.pass_location, font=('Arial', 14))
        self.button.grid(row=2, column=0, columnspan=2, pady=10)

        # allows pressing enter to submit data in entry box
        self.bind('<Return>', lambda event: self.pass_location())

    def pass_location(self):
        '''
        Wrapper function for get_weather after a reference to it is stored in the class
        '''
        gw = getWeather()
        location = self.entry.get()
        use_metric = self.checkbox_status.get()
        if location:
            api_repsonse = self.get_weather(location)
            name, region, country, text, icon, temp_f, feelslike_f, wind_mph, temp_c, feelslike_c, wind_kph = gw.parse_weather(api_repsonse)
            if api_repsonse:
                if use_metric:
                    formatted_weather = f'Temp: {temp_c}\N{DEGREE SIGN}C\nFeels like: {feelslike_c}\N{DEGREE SIGN}C\nCondition: {text}'
                else:
                    formatted_weather = f'Temp: {temp_f}\N{DEGREE SIGN}F\nFeels like: {feelslike_f}\N{DEGREE SIGN}F\nCondition: {text}'
                self.weather_label.configure(text=formatted_weather)
            else:
                self.weather_label.configure('Error no proper data to display')
        else:
            self.weather_label.configure('No location given')
        


if __name__ == '__main__':
    app = gui()
    app.mainloop()

