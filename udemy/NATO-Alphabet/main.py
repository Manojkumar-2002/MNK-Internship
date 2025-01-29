import json
import pandas as pd

class Main:
    def __init__(self, json_file):
        self.json_file = json_file
        self.nato_df = self.load_nato_alphabet()
        
    def load_nato_alphabet(self):
        try:
            with open(self.json_file, 'r') as file:
                nato_data = json.load(file)
            df = pd.DataFrame(list(nato_data.items()), columns=['Letter', 'NATO Word'])
            return df
        except FileNotFoundError:
            print(f"Error: The file {self.json_file} was not found.")
            return pd.DataFrame()
        except json.JSONDecodeError:
            print("Error: The JSON file is not properly formatted.")
            return pd.DataFrame()

    def convert_to_nato(self, text):
        if self.nato_df.empty:
            print("Error: NATO alphabet data not available.")
            return
        text = text.upper()
        nato_translation = []

        for char in text:
            if char == " ":
                nato_translation.append("(space)")
            elif char.isalpha():
                nato_word = self.nato_df.loc[self.nato_df['Letter'] == char, 'NATO Word'].values
                if nato_word:
                    nato_translation.append(nato_word[0])

        print("NATO Phonetic Alphabet Translation:")
        print(" ".join(nato_translation))

    def get_user_input_and_convert(self):
        text = input("Enter a word or phrase: ")
        self.convert_to_nato(text)

if __name__ == "__main__":
    converter = Main('nato_alphabet.json')
    converter.get_user_input_and_convert()
