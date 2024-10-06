from collections import namedtuple
from dataclasses import dataclass
from datetime import datetime

from pandas import DataFrame

# A match with start and end timestamps and a score.
# The score is a float value representing the distance, so smaller is better.
MatchModel = namedtuple('MatchModel', ['start', 'end', 'score'])


# Contains the matched price data and the data immediately following. The data following the match may be historical
# data, or it may be generated data (a real projection). But we refer to them both as projections. The projection start
# should usually be immediately following the match_end.
@dataclass
class WindowMatch:
    window: DataFrame
    match_end: datetime
    projection_start: datetime
    score: float = -1
