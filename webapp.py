# Web app for generating mazes.

import os.path
import tornado.ioloop
import tornado.web
import mazegen

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html', maze=mazegen.generate_maze(10, 12))

application = tornado.web.Application(
    [
        (r'/', MainHandler)
    ],
    template_path=os.path.join(os.path.dirname(__file__), 'templates'),
)

if __name__ == '__main__':
    application.listen(8888)
    print "Server running on port 8888"
    tornado.ioloop.IOLoop.instance().start()
