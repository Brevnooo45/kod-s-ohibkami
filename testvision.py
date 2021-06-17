import pyttsx3
import speech_recognition as sr
import pyaudio


opts = [
    "что вы любите делать?", " Что вам нравится делать ?", "Чем вы увлеккаетесь в свободное время? ",
    "Чем вы хотите заниматсья?"
]

kyda = [
    "куда мне идти?", "В какой квантум мне идти?"
]

IT = [
    "мне нравится работать с компьютером", "писать код", "делать чат ботов", "работать с компьютерными сетями"
]

HI =[
    "Мне гравится работать с деревовом", "Мне нравится изготавливать какие либо вещи", "мне нравятся труды"
]
aero = [
    "Мне нравится летать на квадрокоптерах", "Мне нравится делать самолеты", "Самолёты"
]
robo =[
    "Мне нравится делать механизмы", "Мне нравится собирать лего", "Мне нравится делать роботов"
]
dizain = [
    "мне нравится рисовать", "Мне нравится исскуство ", "рисовать", "Моделировать фигуры"
]
geo = [
    "Мне нравится география", "мне нравится изучать местоположение"
]
eng = [
    "Мне нравится изучать энергию"
]
engine = pyttsx3.init()
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    audio = r.listen(source)

query = r.recognize_google(audio, language="ru-RU")

if query.lower() == kyda:
    engine.say(opts)
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        audio = r.listen(source)
    if query.lower() == IT:
        engine.say("Вам подходит IT Квантум")
    if query.lower() == HI:
        engine.say("Вам подходит Хай тек квантум")
    if query.lower() == aero:
        engine.say("Вам подходит Аеро квантум")
    if query.lower() == robo:
        engine.say("Вам подходит Робо квантум")
    if query.lower() == dizain:
        engine.say("Вам подходит Промдизайн")
    if query.lower() == geo:
        engine.say("Вам подходит Гео квантум")
    if query.lower() == eng:
        engine.say("Вам подходит Энерджи квантум")

