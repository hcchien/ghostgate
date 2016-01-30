from resources.dbo import model_resource

class Post(model_resource):
    def __init__(self):
        super(Post, self).__init__()
        self._table = "posts"
