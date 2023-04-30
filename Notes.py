from Note import Note
import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Notes:
    def __init__(self, filename):
        self.filename = os.path.join(__location__, filename)
        self.notes = []
        self.load()

    def load(self):
        if (os.path.exists(self.filename)):
            with open(self.filename, 'r') as f:
                try:
                    notes_data = json.load(f)
                    self.notes = [Note(n['id'], n['title'], n['body'])
                                  for n in notes_data]
                except:
                    self.notes = []
            f.close()

    def save(self):
        if (self.notes != []):
            with open(self.filename, 'w') as f:
                notes_data = [note.get_info() for note in self.notes]
                json.dump(notes_data, f)
            f.close()

    def add(self, title, body):
        note = Note(len(self.notes) + 1, title, body)
        self.notes.append(note)

    def read(self, id):
        for note in self.notes:
            if note.id == id:
                return note.get_info()
        return None

    def edit(self, id, title, body):
        for note in self.notes:
            if note.id == id:
                note.edit(title, body)
                return
        raise ValueError(f'Note with id {id} not found')

    def delete(self, id):
        for note in self.notes:
            if note.id == id:
                self.notes.remove(note)
                return
        raise ValueError(f'Note with id {id} not found')
