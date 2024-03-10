from src.streamlit_application.dashboard import Dashboard


class Engine:
    def __init__(self):
        self.dashboard = Dashboard()

    def run(self):
        self.dashboard.run()