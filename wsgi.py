import cherrypy

class Responder(object):

    @cherrypy.expose
    def index(self):
        return "Hello World!"

application = cherrypy.tree.mount(Responder())
