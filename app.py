from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return send_from_directory('static', 'video.mp4')

if __name__ == '__main__':
    app.run(debug=True)
