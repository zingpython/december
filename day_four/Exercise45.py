
class Bucket:

	def __init__(self, name, max_volume, current_volume):
		self.name = name
		self.max_volume = max_volume
		self.current_volume = current_volume

	def getName(self):
		return self.name

	def getMaxVolume(self):
		return self.max_volume

	def setMaxVolume(self, max_volume):
		self.max_volume = max_volume

	def getCurrentVolume(self):
		return self.current_volume

	def setCurrentVolume(self, current_volume):
		self.current_volume = current_volume

	def transfer(self, from_bucket):
		space = self.max_volume - self.current_volume

		available_volume = from_bucket.getCurrentVolume()

		if space <= available_volume:
			#Only transfer the space available
			self.current_volume = self.current_volume + space
			
			from_bucket.setCurrentVolume( available_volume - space )

		elif space > available_volume:
			#Transfer the entire contents of from_bucket
			self.current_volume = self.current_volume + available_volume

			from_bucket.setCurrentVolume( 0.0 )

	