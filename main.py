import os
from flask import Flask
from tortoise.do_tts import mainFun

app = Flask(__name__)

@app.route("/")
def query():
    try:
        mainFun("[I am so angry,] I went to the park and threw a ball", "random", "ultra_fast")
        return {"message": "Conversion successfully", "audio_files": 'saved_files'}
    except Exception as error:
        return {"message": f"something went wrong. {error}"}
    finally:
        print('')