#Uses openweatherapi to find the current temp for Wellington and Christchurch (Or 2 specified places).
#Could be expanded to include things like better weather, daily highs etc.
#For some reason when I do non-NZ places like Rome it returns 0.X degrees.

from api_extraction import *


def run_main(town1='Wellington', town2='Christchurch'):
    town1temp = weather_temp(town1)
    town2temp = weather_temp(town2)

    if town1temp > town2temp:
        print(town1, 'is warmer than', town2, 'by', round(town1temp - town2temp, 1), 'degrees')
    elif town1temp < town2temp:
        print(town2, 'is warmer than', town1, 'by', round(town2temp - town1temp, 1), 'degrees')
    elif town1temp == town2temp:
        print(town1, 'is the same as', town2, '.', round(town1temp, 1), 'degrees')
    else:
        print('Error')


if __name__ == '__main__':
    run_main(town2='Rangiora')
