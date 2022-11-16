# pip install -U Flask Authlib requests
# pip install mysql-connector-python
import os, math

from flask import Flask, redirect, url_for, session, jsonify, request, make_response
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS
from mysql_connector import cursor, cnx

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")
app.config.from_object('config')
CORS(app)


oauth  = OAuth(app)
google = oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def auth():
    token = oauth.google.authorize_access_token()
    session['user'] = token['userinfo']
    return redirect('/status')


@app.route('/status')
def status():
    user = session.get('user')
    data = f'{user["email"]}/{user["name"]}'
    response = make_response(redirect('http://127.0.0.1:8081/home/dashboard'))
    response.set_cookie('session_app_user', data)
    return response
   


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('http://127.0.0.1:8081/')


@app.route('/users', methods=["GET"])
def users():
    try:
        comando_count = f'SELECT count(*) FROM users'
        cursor.execute(comando_count)
        resultado_count = cursor.fetchall()
        qtd = resultado_count[0][0]
        max = math.ceil(qtd / 10)
        offset = (int(request.args['page']) -1) * 10

        if int(request.args['page']) > max:
          return jsonify(status=False)

        next = int(max - int(request.args['page'])) + 1
        previous = int(max - int(request.args['page'])) - 1

        if int(max - int(request.args['page'])) == 0:
            next = int(max - int(request.args['page']))  
            previous = int(max - int(request.args['page'])) + 1
        
        comando = f'SELECT email, name FROM users ORDER BY id DESC LIMIT 10 OFFSET {offset}'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        return jsonify(results=resultado,next=next,previous=previous)
    except:
        return jsonify(status=False)


@app.route('/app/login', methods=["POST"])
def app_login():
    password = request.form.get('password')
    email    = request.form.get('email')

    try:
        comando = f'SELECT * FROM users WHERE email="{email}"'
        cursor.execute(comando)
        resultado = cursor.fetchone()

        if resultado[2] != password:
            return jsonify(status=False)

        return jsonify(status=True,email=resultado[1],name=resultado[3])
    except:
        return jsonify(status=False)
   

@app.route('/app/create', methods=["POST"])
def app_create():
    name     = request.form.get('name')
    password = request.form.get('password')
    email    = request.form.get('email')
    try:
        comando = f'INSERT INTO users (email, password, name) VALUES ("{email}", "{password}", "{name}")'
        cursor.execute(comando)
        cnx.commit()
        return jsonify(status=True)
    except:
        return jsonify(status=False)
    
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="3000")