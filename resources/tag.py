from resources.dbo import model_resource

class Tag(model_resource):
    def __init__(self):
        super(Tag, self).__init__()
        self._table = "tags"
