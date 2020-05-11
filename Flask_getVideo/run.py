from flask import Flask,render_template
import multiprocessing
import capture as cap
app=Flask(__name__)


def capCam(time=100):
    cap.runCapture(time)

@app.route('/',methods=['GEt'])
def index():
    p1=multiprocessing.Process(target=capCam)
    p1.start()
    return 'Hello World'
















    





app.run(host='0.0.0.0',port=5000)
