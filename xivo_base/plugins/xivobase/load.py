from xivo_admin import BasePlugin
from views import xivobase

class XiVOBase(BasePlugin):
    def load(self, app):
        print "Loading..."
        app.register_blueprint(xivobase)
