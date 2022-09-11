#!/usr/bin/env python3
import json
import re
import pandas as pd

# Opening JSON file
with open('data/input-example-users.json', 'r') as JSON:
    rstudio_users_nested_dict = json.load(JSON)

# Validate username it is not an email address using regex
def valid_email(email):
  return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))


# Filter out 'results' from the dictionary into a new list
list_rstudio_users_dict = rstudio_users_nested_dict["results"]
print("DEBUG: Print 'results' which is a list:\n" + str(list_rstudio_users_dict) + "\n")

# Convert dictionary into list of users and filter out locked out users
unlocked_usernames = [x['username'] for x in list_rstudio_users_dict if ( x['locked'] is not True )]
print("DEBUG: List of unlocked users:\n" + str(unlocked_usernames) + "\n")

# Fitle out emails that are emails
nonemail_usernames = []
for username in unlocked_usernames:
    if valid_email(username) is False:
        nonemail_usernames.append(username)

print(str("DEBUG: List of unlocked users that are not email addresses:\n" + str(nonemail_usernames)) + "\n")

######


# Pandas example with DataFrame
df = pd.DataFrame(list_rstudio_users_dict, columns = ['username','user_role','email','active_time'])

print(df)
print (df.info())

# PExport to a CSV file
df.to_csv('data/output-example-filtered-users.cvs', encoding='utf-8', index=False)


