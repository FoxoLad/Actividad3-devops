printf 'from flask import Flask\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    
return "<h1>Pipeline CI/CD funcionando correctamente</h1>"\n\nif __name__ == "__main__":\n    
app.run(host="0.0.0.0", port=5000)\n' > app/app.py
