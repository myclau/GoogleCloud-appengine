from . import default


@default.route('/')
def default_get():
    return '''<h1>Test Flask Lab</h1>
<p>Avaliable endpoints:</p>
<p>/where2go</p>'''