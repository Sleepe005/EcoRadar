from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Метеостанция
class station():
    # Инициализируем новую метеостанцию
    def __init__(self, x, y, norm_value, scale):
        self.value = 0
        self.x = x
        self.y = y
        self.gas_x = x
        self.gas_y = y
        self.norm_value = norm_value
        self.scale = scale
    
    # Получили новое значение (Создали новое газовое облако)
    def new_value(self, value, smap):
        self.value = value
        newGasCloud = gasCloud(self.x, self.y, value, self.scale, self.norm_value)
        return newGasCloud.create_new_gas_cloud(value, smap)

# Газовое облако
class gasCloud():
    # Инициализируем газовое облако
    def __init__(self, x_center, y_center, value, scale, norm_value):
        self.x_center = x_center
        self.y_center = y_center
        self.value = value
        self.scale = scale
        self.norm_value = norm_value

    # Создаём новое газовое облако
    def create_new_gas_cloud(self, value, smap):
        if value > self.norm_value:
            self.value = value

            cloud_size = int(((self.scale[0]*self.scale[1]*(value-self.norm_value))/100)**0.5)
            
            for x in range(self.x_center - cloud_size, self.x_center + cloud_size):
                for y in range(self.y_center - cloud_size, self.y_center + cloud_size):
                    if x >= 0 and y >= 0:
                        try:
                            smap[x][y].new_val(value)
                        except:
                            continue
            # Газовое облако пораждает новые облака исходя из напровления, скорости ветра, степени превышения показателей
            try:
                move_y_center = self.y_center + cloud_size*smap[self.x_center][self.y_center].wind_vertical_direction
                move_x_center = self.x_center + cloud_size*smap[self.x_center][self.y_center].wind_horizontal_direction

                newGasCloud = gasCloud(move_x_center, move_y_center, value-(100*70)/value, self.scale, self.norm_value)
                newGasCloud.create_new_gas_cloud(value-(100*10)/value, smap)
            except:
                return smap

            return smap 

# Объявляем класс квадрата территории
class square():
    # Инициализируем каждый квадрат карты
    def __init__(self, val = 0, wind_speed = 0, wind_vertical_direction = 0, wind_horizontal_direction = 0):
        self.val = val
        self.sta = None
        self.wind_speed = wind_speed
        self.wind_vertical_direction = wind_vertical_direction
        self.wind_horizontal_direction = wind_horizontal_direction
    
    def new_val(self, val):
        self.val = val
    
    def set_station(self, sta):
        self.sta = sta
    
# Генерируем карту
scale = (500, 500) # Размеры карты
spectralmap = [[square(val=0,wind_speed=0,wind_vertical_direction=1,wind_horizontal_direction=1) for i in range(scale[0])] for j in range(scale[1])]

# Создаём метеостанции
stations = [station(123, 287, 100, (10, 10)), station(35, 44, 100, (10, 10))]
for sta in stations:
    spectralmap[sta.x][sta.y].set_station(sta)

# Меняем значения
# TODO: Тут получаем с сервера инфу о получении нового значения с метеостанции
new_meteo_value, meteo_x, meteo_y = 200, 10, 10 
spectralmap = stations[0].new_value(200, spectralmap)
spectralmap = stations[1].new_value(150, spectralmap)

# Отрисовываем карту
heatmap_smap = [[spectralmap[i][j].val for i in range(scale[0])] for j in range(scale[1])]
sns.heatmap(heatmap_smap, cmap="coolwarm")
plt.show()
