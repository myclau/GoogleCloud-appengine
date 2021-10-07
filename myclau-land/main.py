from flask import Flask
from api.default import default
from api.where2go import where2go

app = Flask(__name__)


app.register_blueprint(default)
app.register_blueprint(where2go)

if __name__ == "__main__":
    #print(app.url_map)
    app.run()