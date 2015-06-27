import web

urls = (
    '/', 'index'
)

class index:
    def GET(self):
        return "Hello, Machine! Your Flag08: 12d30f3cf3b6c9502dc9c2d0cd30e6cc. You MaY Find SomeThing Useful!"
        #Oh,And your Flag13: e42715c0931d7c62f4408d66ad8a0018

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
