from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.espncricinfo.com/series/county-championship-division-one-2023-1347099/stats")
espn_web_page = response.text

soup = BeautifulSoup(espn_web_page, 'html.parser')

player_name_tags = soup.find_all(class_="ds-text-title-xs ds-font-bold")
player_names = []

scores_name_tags = soup.find_all(class_="ds-text-title-l ds-font-bold")
scores = []

for tag in player_name_tags:
    name = tag.getText()
    player_names.append(name)

for score_tag in scores_name_tags:
    score = score_tag.getText()
    scores.append(score)


cricket_dict = {
    "Players":player_names,
    "Scores":scores,
}

data = pd.DataFrame(cricket_dict)
print(data)
