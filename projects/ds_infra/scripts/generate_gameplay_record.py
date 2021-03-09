"""Generate gameplay record
Generates the testing dataset for mock interview. The output
CSV contains 2 cols game_id and dates where the game_id is
the name of the game and dates are the dates a user downloads
the game.
"""

import datetime
import random
import pandas as pd
from typing import List
from tqdm import tqdm

def get_game_names() -> List[str]:
    return [
        'starcraft', 'pokemon', 'CS', 'Dota', 'Warcraft', 'Overwatch',
        'Tank World', 'Super Mario', 'Sonic', 'NBA', 'FIFA', 'Hitman',
        'Final Fantasy', 'X Man', 'Bleach', 'Dragonball', 'Goku', 'Naruto',
        'Itachi'
    ]


def get_random_game(games: List[str]) -> str:
    return games[random.randrange(len(games))]


def get_random_game_ids(games: List[str], cnt: int) -> List[str]:
    return [get_random_game(games) for _ in tqdm(range(cnt))]


def random_date_between(start_date: datetime.date, end_date: datetime.date,
                        cnt: int) -> List[str]:
    random_dates = []
    for _ in tqdm(range(cnt)):
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + \
            datetime.timedelta(days=random_number_of_days)
        random_dates.append(random_date.strftime('%m-%d-%Y %H:%M:%S'))
    return random_dates


def main() -> None:
    print('Start generating game records.')
    games = get_game_names()
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=5)
    record_cnt = 10000
    game_ids = get_random_game_ids(games, record_cnt)
    use_dates = random_date_between(start_date, end_date, record_cnt)
    df = pd.DataFrame()
    df['game_id'] = game_ids
    df['dates'] = use_dates
    df.to_csv('output.csv')


if __name__ == '__main__':
    main()
