import requests
from bs4 import BeautifulSoup
import unicodedata


def normalize(str):
    return unicodedata.normalize( 'NFKC', str)


def scrape_batters():
    batters = {}
    r = requests.get('http://baseball.yahoo.co.jp/npb/stats/batter?series=1')
    soup = BeautifulSoup(r.text, "html.parser")
    batters = []
    for player_idx, player in enumerate(soup.find_all('tr')):
        if player_idx < 2 or player_idx > len(soup.find_all('tr')) - 2: continue
        player_col = player.find_all('td')
        batter = {}
        batter['name'] = normalize(player_col[1].string)
        batter['team'] = normalize(player_col[2].string)
        batter['ave']  = normalize(player_col[3].string)
        batter['game'] = normalize(player_col[4].string)
        batter['plate_appearance'] = normalize(player_col[5].string)
        batter['at_bats'] = normalize(player_col[6].string)
        batter['hits'] = normalize(player_col[7].string)
        batter['_2b']  = normalize(player_col[8].string)
        batter['_3b']  = normalize(player_col[9].string)
        batter['homerun'] = normalize(player_col[10].string)
        batter['total_bases'] = normalize(player_col[11].string)
        batter['rbi'] = normalize(player_col[12].string)
        batter['runs_scored'] = normalize(player_col[13].string)
        batter['strikeouts'] = normalize(player_col[14].string)
        batter['bb'] = normalize(player_col[15].string)
        batter['db'] = normalize(player_col[16].string)
        batter['sh'] = normalize(player_col[17].string)
        batter['sf'] = normalize(player_col[18].string)
        batter['sb'] = normalize(player_col[19].string)
        batter['obp'] = normalize(player_col[20].string)
        batter['slg'] = normalize(player_col[21].string)
        batter['risp'] = normalize(player_col[22].string)
        batter['double_play'] = normalize(player_col[23].string)
        batter['error'] = normalize(player_col[24].string)
        batters.append(batter)
    return batters
