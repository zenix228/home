class flat:
    def __init__(self,room,kitchen,floor):
        self.room = room
        self.kitchen = kitchen
        self.floor = floor
    def live(self):
        if self.room > 1:
            result = ('You can live')
		else:
            result = ('You can not live')
		return result
    def haveKitchen(self):
        if self.kitchen == 'yes':
			print('you can cook')
		else:
			print('you can not cook')
timur = flat(room=5,kitchen='yes',floor=2)
print(timur)