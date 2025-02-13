from weather.get_weather import getWeather
from gui.gui import gui


def main():
    weather = getWeather()
    app = gui(weather.get_weather)
    app.mainloop()


if __name__ == '__main__':
    main()