from datetime import datetime as time


class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = time.now().strftime("%Y-%m-%d %H:%M:%S")
        self.updated_at = time.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_info(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def edit(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = time.now().strftime("%Y-%m-%d %H:%M:%S")
