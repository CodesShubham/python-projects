import speech_recognition as sr
import os


def say(text):
    os.system(f"say {text}")


