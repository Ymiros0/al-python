class Event:
	__name = "Event"

	def __init__(self, id, data, dispatcher):
		self.ID = id
		self.Data = data
		self.Dispatcher = dispatcher

