import pandas as pd
import os
import bcrypt

json_file = 'data.json'
if os.path.exists(json_file):
    df = pd.read_json(json_file)
    df.loc[df["website"] == "face", ["email", "password"]] = ["manoj", 123456]
    facebook_data = df.loc[df["website"] == "facebook"]
    # print("Data where website is 'facebook':\n", facebook_data)

    new_entry = pd.DataFrame([{"website": "hii", "email": "manoj2", "password": 12345}])
    df = pd.concat([df,new_entry])
    # print("Dataframe")
    # print(df)
    # print("new entry",new_entry)
    print(df.iloc[:0,:0])

else:
    df = pd.DataFrame(columns=["website", "email", "password"])
# print(df["website"])
# for i in df[df["website"]=="facebook"]:
#     print(i)

custom_salt = bcrypt.gensalt(rounds=14)
print(custom_salt)
hashed_pass = bcrypt.hashpw(b"my password",custom_salt)
print(hashed_pass)
password = hashed_pass.decode("utf-8")
print(password)
