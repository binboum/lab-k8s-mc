from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def lab():
    return """<html>
   <head>
      <title>LAB K8S</title>
      <link rel="shortcut icon" href="https://www.monaco-telecom.mc/templates/gantry/favicon.ico">
   </head>
   <body align="center">
      <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Logo-MT.png"> 
      <p>Version : 1.0.0</p>
      <p>Hostname : {hostname}</p>
   </body>
</html>""".format(hostname=os.getenv('HOSTNAME'))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
