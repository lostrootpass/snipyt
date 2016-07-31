#!/usr/bin/env python

import web
        
urls = (
    '/', 'index',
	'/([a-zA-Z0-9\-_]+)\/?([0-9]+),?((?<=,)[0-9]+)?\/?((?<=\/)[01]{1})?/', 'player',
)
app = web.application(urls, globals())
templates = web.template.render("templates")

class player:
	def GET(self, id, start, end, loop):
		return templates.base(templates, templates.player(templates, id, start, end, loop))
	
class index:        
    def GET(self):
		return templates.base(templates, templates.index(templates))

if __name__ == "__main__":
    app.run()
