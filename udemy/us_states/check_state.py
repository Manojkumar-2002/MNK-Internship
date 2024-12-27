import pandas as pd

class StateChecker:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None
        self.load_csv()

    def load_csv(self):
        try:
            self.df = pd.read_csv(self.csv_file)
        except FileNotFoundError:
            print("CSV file not found!")
            self.df = None

    def check_state_in_csv(self, state_name):
        if self.df is not None:
            if state_name.lower() in self.df.state.str.lower().values:
                return True
        return False

    def get_state_coordinates(self, state_name):
        if self.df is not None:
            state_data = self.df[self.df['state'].str.lower() == state_name.lower()]
            if not state_data.empty:
                return state_data.iloc[0]['x'], state_data.iloc[0]['y']
        return None

    def load_states_coordinates(self):
        df = pd.read_csv(self.csv_file)
        state_coordinates = {row['state'].lower(): (row['x'], row['y']) for _, row in df.iterrows()}
        return state_coordinates
