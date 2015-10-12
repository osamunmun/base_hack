import requests
from bs4 import BeautifulSoup
import unicodedata
import ipdb


def normalize(str):
    return unicodedata.normalize( 'NFKC', str)


if __name__ == '__main__':
    r = requests.get('http://baseball.yahoo.co.jp/npb/stats/batter?series=1')
    soup = BeautifulSoup(r.text, "html.parser")

    for player_idx, player in enumerate(soup.find_all('tr')):
        if player_idx < 2 or player_idx > len(soup.find_all('tr')) - 2: continue
        player_col = player.find_all('td')
        name = normalize(player_col[1].string)
        team = normalize(player_col[2].string)
        ave  = normalize(player_col[3].string)
        game = normalize(player_col[4].string)
        plate_appearance = normalize(player_col[5].string)
        at_bats = normalize(player_col[6].string)
        hits = normalize(player_col[7].string)
        _2b  = normalize(player_col[8].string)
        _3b  = normalize(player_col[9].string)
        homerun = normalize(player_col[10].string)
        total_bases = normalize(player_col[11].string)
        rbi = normalize(player_col[12].string)
        runs_scored = normalize(player_col[13].string)
        strikeouts = normalize(player_col[14].string)
        bb = normalize(player_col[15].string)
        db = normalize(player_col[16].string)
        sh = normalize(player_col[17].string)
        sf = normalize(player_col[18].string)
        sb = normalize(player_col[19].string)
        obp = normalize(player_col[20].string)
        slg = normalize(player_col[21].string)
        risp = normalize(player_col[22].string)
        double_play = normalize(player_col[23].string)
        error = normalize(player_col[24].string)
        print(name, team, ave, risp)
