import pandas as pd

class Highscore:
    def __init__(self):
        try:
            self.df = pd.read_csv("high_scorers.csv")
            self.leaderboard = pd.read_csv("high_scorers.csv")
        except FileNotFoundError as e:
            self.leaderboard = pd.DataFrame(columns=["users","scores"])
            self.df = pd.DataFrame(columns=["users", "scores"])

        if not self.df.empty:
            self.user,self.score = self.df.iloc[-1].to_list()
            self.score = int(self.score)
        else:
            self.user, self.score = "No one",0


    def get_high_score(self):
        return [self.user,self.score]


    def set_high_score(self,user,score):
        if score > self.score:
            new_high_score = [{
                "users":user,
                "scores":score
            }]
            df = pd.concat([self.df,pd.DataFrame(new_high_score)],ignore_index=True)
            df.to_csv("high_scorers.csv",index=False)

    def get_leaderboard(self):
        return self.leaderboard.iloc[-5:][::-1].to_dict(orient="records")


high = Highscore()
high.get_leaderboard()




