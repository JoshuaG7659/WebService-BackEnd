from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/app/v1/users/<id>',methods=["GET","POST"])
def user_action(id):
    print((request.method))
    if (request.method=="POST"):
        print("Guardado en la nube")
        return "Guardado"
    else:
        print("Recurso obtenido")
        return id
    

app.run(debug=True)