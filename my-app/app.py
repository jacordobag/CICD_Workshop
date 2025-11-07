from flask import Flask, render_template, jsonify
import datetime
 
app = Flask(__name__)
 
@app.route('/')
def sample_page():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)
 
@app.route('/my-app')
def my_app():
    year = datetime.datetime.now().year
    return render_template('index.html', year=year)
 
@app.route('/healthcheck')
def health_check():
    return jsonify({'health_status': 'OK'})
 
if __name__ == '__main__':
    # Habilita debug para recargar automáticamente y escuchar en todas las interfaces
    app.run(host='0.0.0.0', port=8081, debug=True)