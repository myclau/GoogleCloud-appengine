# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import json
import random



class wheretogo(webapp2.RequestHandler):
    def get(self):
    	selectindex = random.randint(0,len(data['station'])-1)
        result = data['station'][selectindex]
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write("<html><body><h1>Where to go?</h1><p>")
        self.response.write(result)
        self.response.write("</p></body></html>")

        
        

with open('shantool/where2go/station.json') as f:
    data = json.load(f)
#selectindex = random.randint(0,len(data['station'])-1)
#result = data['station'][selectindex]


app = webapp2.WSGIApplication([
    ('/where2go', wheretogo),
], debug=True)
