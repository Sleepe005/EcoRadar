#include <Servo.h>
#include <SoftwareSerial.h>
#include <TinyGPS.h>
#include <GprsModem.h>

// Объект GPS
TinyGPS gps;

// Создаём програмные UART порты
SoftwareSerial gpsSerial(9, 10);
SoftwareSerial wifiSerial(11, 12);
SoftwareSerial gprsSerial(20, 21);


// Создаём объект GPRS
GprsModem GPRSModem(gprsSerial, 13);
GprsClient GPRSClient(gprsSerial);

// Создаём объекты моторов
Servo FrontRightMotor;

// Устанавливаем пины подключения моторов
int FRMPin = 3;
Servo FrontLeftMotor;
int FLMPin = 4;
Servo BehindRightMotor;
int BRMPin = 5;
Servo BegindLeftMotor;
int BLMPin = 6;

// Переменные для хранения скорости моторов
int FRMSpeed, FLMSpeed, BRMSpeed, BLMSpeed = 0;

// Пин подключения джойстика высоты
int HeightYPin = 7;

// Пин подключения джойстика позиции
int PositionXPin = 8;

// Переменные для хранения занчений широты и долготы
long lat, lon;

// Переменные пароля и имени WIFI сети
String WifiName = "LIN";
String WifiPass = "79918052";

void setup() {
  // Устанавливаем пропускные способности модулей
  Serial.begin(9600);
  gpsSerial.begin(9600);
  wifiSerial.begin(115200);
  GPRSClient.begin();

  // Инициализируем моторы
  FrontRightMotor.attach(FRMPin);
  FrontLeftMotor.attach(FLMPin);
  BehindRightMotor.attach(BRMPin);
  BegindLeftMotor.attach(BLMPin);

  // Подключаемся к WIFI
}

void loop() {
  // Получаем значения широты и долготы по GPS
  bool newGpsData = readgps();
  if (newGpsData) {
    gps.get_position(&lat, &lon);
  }

  // Получаем значение высоты
  int Y = analogRead(HeightYPin);
  // Получаем значени позиции
  int X = analogRead(PositionXPin);

  //   Код взлёта дрона

  
  // Подключаемся к серверу
  char host[] = "";  // Адрес
  int port = 80;     // Порт
  GPRSClient.connect(host, port);
  // Отправляем информацию на сервер
  GPRSClient.println("");  // Запрос
  GPRSClient.println((String) "Host: " + host);
  GPRSClient.println("Connection: close");
  GPRSClient.println();
  // Получаем ответ
  String dataFromServer = (String)GPRSClient.read();
}

bool readgps() {
  while (gpsSerial.available()) {
    int b = gpsSerial.read();
    //в библиотеке TinyGPS имеется ошибка: не обрабатываются данные с \r и \n
    if ('\r' != b) {
      if (gps.encode(b))
        return true;
    }
  }
  return false;
}
