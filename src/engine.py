from src.streamlit_application.dashboard import Dashboard


class Engine:
	"""
	The Engine class serializes the Dashboard class. It is the main class of the program.
	"""
	

	def __init__(self) -> None:
		"""
		The constructor of the Engine class. It creates an instance of the Dashboard class.

		Returns:
		- None
		"""
		
		self.dashboard = Dashboard()

	
	def run(self) -> None:
		"""
		The function seraializes the run function of the Dashboard class.

		Returns:
		- None
		"""
		
		self.dashboard.run()