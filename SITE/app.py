from flask import Flask, request, render_template, Response
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)


@app.route('/upload_music', methods=['POST'])
def upload_music():
    if request.method == 'POST':
        music_file = request.files['music']
        music_file.save('/file.mp3')

        subprocess.run(["python", "C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/SITE/PY/main_playrec.py"])
        return 'Python script executed successfully'

    return 'Method Not Allowed', 405


@app.route('/clear_cache', methods=['POST'])
def clear_cache():
    os.system('C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/SITE/PY/clear_cache.py')
    return 'Cache cleared successfully'



@app.route('/sse')
def sse():
    def generate():
        yield 'data: Hello\n\n'

    return Response(generate(), content_type='text/event-stream')


@app.route('/execute_python', methods=['POST'])
def execute_python():
    subprocess.run(["python", "C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/SITE/PY/main_playrec.py"])
    return 'Python script executed successfully'


@app.route('/execute_python_txt', methods=['POST'])
def execute_python_txt():
    subprocess.run(["python", "C:/Users/asus/OneDrive/Desktop/VS/PYTHON/MINOR/SITE/PY/main_only_text.py"])
    return 'Python script executed successfully'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
