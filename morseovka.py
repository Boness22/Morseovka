import morseovka_znak

class Morseovka:
	def __init__(self,zprava):
		self.zprava = zprava

	def kodovani(self):
		zprava1 = ""
		nova_zprava = list(self.zprava)
		for pismeno in nova_zprava:
			if pismeno == " ":
				continue
			for znak in morseovka_znak.Morseovy_znaky:
				if pismeno == znak[0]:
					zprava1 += znak[1] +" "
		print(f"kodovana zprava: {zprava1}")	

	def dekodovani(self):
		zprava2 = ""
		nova_zprava = self.zprava.split()
		for pismeno in nova_zprava:
			if pismeno == "":
				zprava2 += " "
			for znak in morseovka_znak.Morseovy_znaky:
				if pismeno == znak[1]:
					zprava2 += znak[0] 
		print(f"Dekodovana zprava: {zprava2}")

	def m_znaky(self):
		pass


morseovka_d = Morseovka(".... --- ...- -. -. --- -. .- ... . .-. ... .. -... -... ")
morseovka_d.dekodovani()
morseovka_k = Morseovka("HOVNNO NASERSIBB")
morseovka_k.kodovani()

