from resources.dbo import model_resource

class User(model_resource):
    def __init__(self):
        super(User, self).__init__()
        self._table = "users"
