from flask import Flask, jsonify, request
import tweepy

import mysql.connector

connection = mysql.connector.connect(user='root', password='adminroot',
                              host='127.0.0.1',
                              database='PRUEBA')

app = Flask(__name__)

auth = tweepy.OAuthHandler("S8WH0kA1pl10TYefROTCd4hbb", "EDH4CMjriRmlkqKDtNYNZiYNyk8mIa0Hq437FBIYtKTwhXA9c9")
auth.set_access_token("1533245440761679873-Z50i6rMd0Dy7stKuU37KFSpvlEi8iU", "xJqyspTvnLSBmrJL6py8QKQWevHOahST5wmlgHm6dU1Ak")


ap2i = tweepy.API(auth)

try:
    ap2i.verify_credentials()
    print("Autenticacion establecida")
except:
    print("Error durante la autenticacion")


@app.route('/user', methods=['POST'])

def getFromUserTwitter():
  
    user = ap2i.get_user(screen_name=request.json['userName'])
    userd= {'name': user.name, 'userName' :request.json['userName'] , 'description':user.description, 'location': user.location}
    try:
        if (len(userd['description'])==0):  
            userd['description']= 'N/A'
        if(len(userd['location'])==0):
            userd['location'] = 'N/A'

        cursor = connection.cursor()
        query = f"INSERT INTO users (UserName, Name, Location, Description)VALUES ('{userd['userName']}','{userd['name']}','{userd['location']}','{userd['description']}')"
        cursor.execute(query)
        connection.commit()
    except:
        print('No se agregó, porque ya se ha guardado el usuario')
      
   
    return jsonify({'userData': userd})

@app.route('/user', methods=['GET'])

def getUsers():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    results= cursor.fetchall()

    users=[]  
    for curUser in results:
        
        user = {'name': curUser[2], 'userName':curUser[1], 'Description': curUser[4],'Location': curUser[3]}
        users.append(user)

    return jsonify({'UserData': users})

@app.route('/user/<idUser>', methods=['GET'])

def getOneUser(idUser):
    try:
        
        cursor = connection.cursor()
        sql1= f"SELECT * FROM users WHERE idUsers= {idUser}"
        cursor. execute(sql1)
        currUser= cursor.fetchall()
        user = {'name': currUser[0][2], 'userName':currUser[0][1],'description':currUser[0][4], 'location': currUser[0][3]}
        connection.commit()
        
        return jsonify({'userData': user})
    
    except:
        
        return jsonify({'ERR': "Usuario no encontrado"})    

@app.route('/user/<idUser>', methods=['PUT'])
def updateUser(idUser):     
    sqlUpd=""
    try:    
        for key in request.json:
            value = request.json[key]
            sqlUpd += f"{key} = '{value}',"
            
        cursor = connection.cursor()
        sql = f"""UPDATE users SET {sqlUpd[:-1]}
        WHERE idusers = '{idUser}' """                        
        cursor.execute(sql)
        connection.commit()       
             
        return jsonify({'Mensaje' : "usuario actualizado"})
    
    except:
        
        return jsonify({'Mensaje' : "No se pudo actualizar el usuario"})
    

@app.route('/user/<idUser>', methods=['DELETE'])

def Delete(idUser):
    try:
        
        cursor = connection.cursor()
        sql1= f"SELECT * FROM users WHERE idusers= {idUser}"
        cursor. execute(sql1)
        currUser= cursor.fetchall()
        user = {'name': currUser[0][2], 'userName': currUser[0][1],'description':currUser[0][4], 'location': currUser[0][3]}
        sql= f"Delete FROM users WHERE idusers = {idUser}"
        cursor. execute(sql)
        connection.commit()
        
        return jsonify({'userData': user})
    
    except:
        
        return jsonify({'ERR': 'Error al borrar'})
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)