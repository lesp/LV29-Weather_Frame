#Import modules
from gpiozero import LED, OutputDevice
import pyowm
import time

#Variables
#Stepper motor for the weather status
Sunny = LED(17)
Bluesky = LED(27)
Snow = LED(22)
Cloudy = LED(10)
Thunder = LED(9)
Shower = LED(11)
Rain = LED(5)
Fog = LED(6)

#Stepper motor for temperature
Temp_IN1 = OutputDevice(23)
Temp_IN2 = OutputDevice(24)
Temp_IN3 = OutputDevice(25)
Temp_IN4 = OutputDevice(8)
#Used to pulse the stepper motor, this is the optimum delay
delay = 0.01


def cw(steps,delay,stepper):
        if stepper == "Temp":
                for i in range(steps):
                        Temp_IN1.on()
                        Temp_IN2.off()
                        Temp_IN3.off()
                        Temp_IN4.off()
                        time.sleep(delay)
                        Temp_IN1.off()
                        Temp_IN2.on()
                        Temp_IN3.off()
                        Temp_IN4.off()
                        time.sleep(delay)
                        Temp_IN1.off()
                        Temp_IN2.off()
                        Temp_IN3.on()
                        Temp_IN4.off()
                        time.sleep(delay)                       
                        Temp_IN1.off()
                        Temp_IN2.off()
                        Temp_IN3.off()
                        Temp_IN4.on()
                        time.sleep(delay)

def ccw(steps,delay,stepper):
        if stepper == "Temp":
                for i in range(steps):
                        Temp_IN1.off()
                        Temp_IN2.off()
                        Temp_IN3.off()
                        Temp_IN4.on()
                        time.sleep(delay)
                        Temp_IN1.off()
                        Temp_IN2.off()
                        Temp_IN3.on()
                        Temp_IN4.off()
                        time.sleep(delay)
                        Temp_IN1.off()
                        Temp_IN2.on()
                        Temp_IN3.off()
                        Temp_IN4.off()
                        time.sleep(delay)                       
                        Temp_IN1.on()
                        Temp_IN2.off()
                        Temp_IN3.off()
                        Temp_IN4.off()
                        time.sleep(delay)

def get_weather(n):
        
#global reset_value
        owm = pyowm.OWM("YOUR SECRET KEY HERE")
        observation = owm.weather_at_place((n))
#Dictionary containg the weather codes used by OWM for certain weather conditions.
#For a full list go to http://bugs.openweathermap.org/projects/api/wiki/Weather_Condition_Codes
        codes = {
        211:"thunderstorm",
        313:"shower rain and drizzle",
        321:"shower drizzle",
        500:"light rain",
        503:"very heavy rain",
        521:"shower rain",
        601:"snow",
        741:"Fog",
        800:"sky is clear",
        801:"few clouds",
        802:"scattered clouds",
        803:"broken clouds",
        804:"overcast clouds",
        }
        w = observation.get_weather()
        a = w.get_temperature('celsius')
        a = int(a['temp'])
        b = w.get_weather_code()
        print(a)
        print(b)
        if a == -5:
                ccw(11,delay,"Temp")
                time.sleep(5)
                cw(11,delay,"Temp")
        elif a == -4:
                ccw(22,delay,"Temp")
                time.sleep(5)
                cw(22,delay,"Temp")
        elif a == -3:
                ccw(33,delay,"Temp")
                time.sleep(5)
                cw(33,delay,"Temp")
        elif a == -2:
                ccw(44,delay,"Temp")
                time.sleep(5)
                cw(44,delay,"Temp")
        elif a == -1:
                ccw(55,delay,"Temp")
                time.sleep(5)
                cw(55,delay,"Temp")
        elif a == 0:
                ccw(66,delay,"Temp")
                time.sleep(5)
                cw(66,delay,"Temp")
        elif a == 1:
                ccw(77,delay,"Temp")
                time.sleep(5)
                cw(77,delay,"Temp")
        elif a == 2:
                ccw(88,delay,"Temp")
                time.sleep(5)
                cw(88,delay,"Temp")
        elif a == 3:
                ccw(99,delay,"Temp")
                time.sleep(5)
                cw(99,delay,"Temp")
        elif a == 4:
                ccw(110,delay,"Temp")
                time.sleep(5)
                cw(110,delay,"Temp")
        elif a == 5:
                ccw(121,delay,"Temp")
                time.sleep(5)
                cw(121,delay,"Temp")
        elif a == 6:
                ccw(132,delay,"Temp")
                time.sleep(5)
                cw(132,delay,"Temp")
        elif a == 7:
                ccw(143,delay,"Temp")
                time.sleep(5)
                cw(143,delay,"Temp")
        elif a == 8:
                ccw(154,delay,"Temp")
                time.sleep(5)
                cw(154,delay,"Temp")
        elif a == 9:
                ccw(165,delay,"Temp")
                time.sleep(5)
                cw(165,delay,"Temp")
        elif a == 10:
                ccw(176,delay,"Temp")
                time.sleep(5)
                cw(176,delay,"Temp")
        elif a == 11:
                cw(187,delay,"Temp")
                time.sleep(5)
                cw(187,delay,"Temp")
        elif a == 12:
                ccw(198,delay,"Temp")
                time.sleep(5)
                cw(198,delay,"Temp")
        elif a == 13:
                ccw(209,delay,"Temp")
                time.sleep(5)
                cw(209,delay,"Temp")
        elif a == 14:
                ccw(220,delay,"Temp")
                time.sleep(5)
                cw(220,delay,"Temp")
        elif a == 15:
                ccw(231,delay,"Temp")
                time.sleep(5)
                cw(231,delay,"Temp")
        elif a == 16:
                ccw(242,delay,"Temp")
                time.sleep(5)
                cw(242,delay,"Temp")
        elif a == 17:
                ccw(253,delay,"Temp")
                time.sleep(5)
                cw(253,delay,"Temp")
        elif a == 18:
                ccw(264,delay,"Temp")
                time.sleep(5)
                cw(264,delay,"Temp")
        elif a == 19:
                ccw(275,delay,"Temp")
                time.sleep(5)
                cw(275,delay,"Temp")
        elif a == 20:
                ccw(286,delay,"Temp")
                time.sleep(5)
                cw(286,delay,"Temp")
        elif a == 21:
                ccw(297,delay,"Temp")
                time.sleep(5)
                cw(297,delay,"Temp")
        elif a == 22:
                ccw(308,delay,"Temp")
                time.sleep(5)
                cw(308,delay,"Temp")
        elif a == 23:
                ccw(319,delay,"Temp")
                time.sleep(5)
                cw(319,delay,"Temp")
        elif a == 24:
                ccw(330,delay,"Temp")
                time.sleep(5)
                cw(330,delay,"Temp")
        elif a == 25:
                ccw(341,delay,"Temp")
                time.sleep(5)
                cw(341,delay,"Temp")
        elif a == 26:
                ccw(352,delay,"Temp")
                time.sleep(5)
                cw(352,delay,"Temp")
        elif a == 27:
                ccw(363,delay,"Temp")
                time.sleep(5)
                cw(363,delay,"Temp")
        elif a == 28:
                ccw(374,delay,"Temp")
                time.sleep(5)
                cw(374,delay,"Temp")
        elif a == 29:
                ccw(385,delay,"Temp")
                time.sleep(5)
                cw(385,delay,"Temp")
        elif a == 30:
                ccw(396,delay,"Temp")
                time.sleep(5)
                cw(396,delay,"Temp")
        elif a == 31:
                ccw(407,delay,"Temp")
                time.sleep(5)
                cw(407,delay,"Temp")
        elif a == 32:
                ccw(418,delay,"Temp")
                time.sleep(5)
                cw(418,delay,"Temp")
        elif a == 33:
                ccw(429,delay,"Temp")
                time.sleep(5)
                cw(429,delay,"Temp")
        elif a == 34:
                ccw(440,delay,"Temp")
                time.sleep(5)
                cw(440,delay,"Temp")
        elif a == 35:
                ccw(451,delay,"Temp")
                time.sleep(5)
                cw(451,delay,"Temp")
        elif a == 36:
                ccw(462,delay,"Temp")
                time.sleep(5)
                cw(462,delay,"Temp")
        elif a == 37:
                ccw(473,delay,"Temp")
                time.sleep(5)
                cw(473,delay,"Temp")
        elif a == 38:
                ccw(484,delay,"Temp")
                time.sleep(5)
                cw(484,delay,"Temp")
        elif a == 39:
                ccw(495,delay,"Temp")
                time.sleep(5)
                cw(495,delay,"Temp")
        elif a == 40:
                ccw(506,delay,"Temp")
                time.sleep(5)
                cw(506,delay,"Temp")
        else:
                time.sleep(5)
#Control the LEDS for the weather
        if b == 211:
                Thunder.on()
                time.sleep(5)
                Thunder.off()
        elif b == 313:
                Shower.on()
                time.sleep(5)
                Shower.off()
        elif b == 321:
                Shower.on()
                time.sleep(5)
                Shower.off()
        elif b == -500:
                Rain.on()
                time.sleep(5)
                Rain.off()
        elif b == 503:
                Rain.on()
                time.sleep(5)
                Rain.off()    
        elif b == 521:
                Shower.on()
                time.sleep(5)
                Shower.off()            
        elif b == 601:
                Snow.on()
                time.sleep(5)
                Snow.off()
        elif b == 741:
                Fog.on()
                time.sleep(5)
                Fog.off()
        elif b == 800:
                Bluesky.on()
                time.sleep(5)
                Bluesky.off()
        elif b == 801:
                Cloudy.on()
                time.sleep(5)
                Cloudy.off()
        elif b == 802:
                Cloudy.on()
                time.sleep(5)
                Cloudy.off()
        elif b == 803:
                Cloudy.on()
                time.sleep(5)
                Cloudy.off()
        elif b == 804:
                Cloudy.on()
                time.sleep(5)
                Cloudy.off()
        else:
                Sunny.on()
                time.sleep(5)
                Sunny.off()

while True:
        get_weather("Blackpool, UK")
        time.sleep(5)
