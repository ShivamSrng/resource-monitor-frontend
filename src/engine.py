import src.streamlit_application.dashboard as dashboard


class Engine:
    def __init__(self):
        self.dashboard = dashboard.Dashboard()

    def run(self):
        self.dashboard.run()