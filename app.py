from flask import Flask, render_template
from main import get_clothes_rec, get_rain_rec

app = Flask(__name__)

@app.route('/')
def index():
    rec, low, high = get_clothes_rec()
    prec = get_rain_rec()
    return render_template('index.html', rec=rec,
                                        low=low,
                                        high=high,
                                        prec=prec)

if __name__ == '__main__':
    app.run()
