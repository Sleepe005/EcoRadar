import cv2 as cv
import matplotlib.pyplot as plt

# Читаем картинку
img = cv.imread("test.PNG")

# Переводим в HSV
# img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Делаем спектральную карту

# Разбиваем на каналы
b,g,r = cv.split(img)
ng = g

# Меняем тон всей карты
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        b[i][j] = 255

# Получение занчений с сервера....
# TODO: реализовать получение данных с сервера
# Для тестов
dataFromServer = 30 # пример пришедших данных
marks = [[[35,110],[70,145]]] #пример пришедших данных

normal = 10
sensivity = 10
dev = (dataFromServer//normal)*sensivity


# Меняем тон нужного учатска
# Зелёный
for i in range(marks[0][0][0]-dev*2, marks[0][1][0]+dev*2):
    for j in range(marks[0][0][1]-dev*2, marks[0][1][1]+dev*2):
        g[j][i] = 200
        b[j][i] = 0
# Красный
for i in range(marks[0][0][0]-dev, marks[0][1][0]+dev):
    for j in range(marks[0][0][1]-dev, marks[0][1][1]+dev):
        g[j][i] = ng[j][i]
        b[j][i] = 0
        r[j][i] = 255

# Собираем назад
img = cv.merge((r,g,b))
# Переводим из BGR в RGB
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Рисуем квадрат, где стоит датчик
cv.rectangle(img, (marks[0][0][0],marks[0][0][1]), (marks[0][1][0],marks[0][1][1]), (0,0,0), -100)

# Выводим полученную карту
cv.imshow("Test",img)
cv.waitKey(0)
cv.destroyAllWindows()
# plt.show()




