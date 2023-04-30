from Notes import Notes


class NotesApp:
	def __init__(self, notes):
		self.notes = notes 

	def start(self):
		while True:
			print('Доступные команды: add, read, edit, delete, list, quit')
			command = input('Введите команду (add/read/edit/delete/list/quit): ')
			match command:
				case 'add':
					title = input('Введите заголовок: ')
					body = input('Введите текст заметки: ')
					self.notes.add(title, body)
					print('Заметка успешно добавлена')
				case 'read':
					id = int(input('Введите ID заметки: '))
					note = self.notes.read(id)
					if note:
						print(note)
					else:
						print(f'Заметка с ID {id} не найдена')
				case 'edit':
					id = int(input('Введите ID заметки: '))
					title = input('Введите новый заголовок: ')
					body = input('Введите новый текст заметки: ')
					try:
						self.notes.edit(id, title, body)
						print(f'Заметка с ID {id} успешно изменена')
					except ValueError as e:
						print(str(e))
				case 'delete':
					id = int(input('Введите ID заметки: '))
					try:
						self.notes.delete(id)
						print(f'Заметка с ID {id} успешно удалена')
					except ValueError as e:
						print(str(e))
				case 'list':
					if (self.notes.notes == []):
						print("Список пуст")
					else:
						for note in self.notes.notes:
							print(note.get_info())
				case 'quit':
					self.notes.save()
					break
				case _:
					print('Некорректная команда')
