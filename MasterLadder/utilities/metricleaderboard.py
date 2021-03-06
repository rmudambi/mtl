from typing import NamedTuple

GAME_COUNT = 'Game Count'
PERCENTAGE = '%'
WINS = 'Wins'
DAYS = 'Days'
RATING = 'Rating'


class __LeaderboardMetrics(NamedTuple):
    MOST_GAMES_PLAYED: str = "Most Games Played"
    BEST_WIN_RATE: str = "Best Win Rate"
    BEST_RATING = "Best Rating"
    MOST_WINS: str = "Most Wins"
    FIRST_RANK_STREAK: str = "First Rank on MTL (Streak)"
    TOP5_STREAK: str = "Top 5 Rank on MTL (Streak)"
    TOP10_STREAK: str = "Top 10 Rank on MTL (Streak)"
    LONGEST_RANKED_STREAK: str = "Longest Ranked (Streak)"
    FIRST_RANK_TOTAL: str = "First Rank on MTL (Total)"
    TOP5_TOTAL: str = "Top 5 Rank on MTL (Total)"
    TOP10_TOTAL: str = "Top 10 Rank on MTL (Total)"
    LONGEST_RANKED_TOTAL: str = "Longest Ranked (Total)"
    FIRST_RANK_ACTIVE: str = "First Rank on MTL (Active)"
    TOP5_ACTIVE: str = "Top 5 Rank on MTL (Active)"
    TOP10_ACTIVE: str = "Top 10 Rank on MTL (Active)"
    LONGEST_RANKED_ACTIVE: str = "Longest Ranked (Active)"
    LONGEST_WIN_STREAK: str = "Longest Win Streak"


LEADERBOARD_METRICS = __LeaderboardMetrics()


class MetricLeaderboardMetadata:
    def __init__(self, metric_name: str, metric_unit: str, build_leaderboard: callable, build_arg: int = None):
        self.metric_name = metric_name
        self.metric_unit = metric_unit
        self.build_leaderboard = build_leaderboard
        self.build_arg = build_arg
