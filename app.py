from flask import Flask, render_template
import socket

app = Flask(__name__)
HOST = "172.20.10.2"
PORT = 12345

def leer_sensor():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = s.recv(1024).decode().strip()
            print("RECIBIDO:", data)
            ejeX, ejeY = data.split(',')
            ejeX = float(ejeX.replace('X:', ''))
            ejeY = float(ejeY.replace('Y:', ''))
            return ejeX, ejeY

    except Exception as e:
        print("ERROR:", e)
        return 0, 0


@app.route('/')
def index():
    ejeY, ejeX = leer_sensor()
    return render_template(
        'index.html',
        ejeX=ejeX,
        ejeY=ejeY
    )


@app.route('/flechas')
def flechas():
    ejeX, ejeY = leer_sensor()
    return render_template('flechas.html', ejeX=ejeX, ejeY=ejeY)
    
@app.route('/leds')
def leds():
    ejeX, ejeY = leer_sensor()
    return render_template('leds.html', ejeX=ejeX, ejeY=ejeY)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
