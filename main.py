#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import random

def rand_fortune():
    fortunes = ["To avoid criticism, do nothing, say nothing, be nothing", "Error 404: Fortune not found", "Optimist believe we live in the best of worlds and pessimists fear this is true.", "Of all our human resources, the most precious is the desire to improve"]
    index = random.randint(0,3)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = rand_fortune()
        final_fortune_sent = "<p>"'Your fortune is: ' + fortune + "</p>"

        lucky_num = random.randint(1,100)
        num_sent = 'Your lucky number: ' + str(lucky_num)
        final_num_sent = "<p>" + num_sent + "</p>"

        another_cookie = "<p><a href='.'><button>another cookie please</button></a></p>"

        da_cookie = header + final_fortune_sent + final_num_sent + another_cookie
        self.response.write(da_cookie)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
