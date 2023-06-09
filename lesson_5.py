class Person :
	def __init__(self,name,surname,age):
		self.name = name
		self.surname = surname
		self.age = age
		def education(self):
			return f'{self.name} - {self.surname} - {self.age}'
		def isSwimming(self):
			result = None
			if self.age < 15:
				result = f'{self.name} не умеет плавать'
			else:
				result = f'{self.name} умеет плавать'
			return result
adxam = Person(name='Adxam',surname='Kazakhov', age=15)
print(f'The person is{adxam.education}, и {adxam.isSwimming}')
ernazar = Person(name='Ernazar',surname='Jumaniyazov', age=13)
print(f'The person is{ernazar.education}, и {ernazar.isSwimming}')
alibek = Person(name='Alibek',surname='Djoldasov', age=13)
print(f'The person is{alibek.education}, и {alibek.isSwimming}')