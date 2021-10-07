from . import where2go
import json
import random
import os
scriptpath = os.path.dirname(os.path.realpath(__file__))
jsonfile = os.path.join(scriptpath,"station.json")

@where2go.route('/where2go')
def where2go_get():
    with open(jsonfile, encoding="utf8") as f:
        data = json.load(f)
    selectindex = random.randint(0,len(data['station'])-1)
    result = data['station'][selectindex]
    return '<html><body><h1>Where to go?</h1><p>'+result+'</p></body></html>'