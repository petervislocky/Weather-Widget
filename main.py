from weather.get_weather import getWeather
from gui.gui import gui


def main():
    #TODO fix this by creating a wrapper function in gui class and store a reference to get_weather rather than calling it right here where it expects a param
    location = input('Enter location >> ')
    weather = getWeather()
    app = gui(weather.get_weather(location))
    app.mainloop()


if __name__ == '__main__':
    main()