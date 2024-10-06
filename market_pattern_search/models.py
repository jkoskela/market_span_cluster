from collections import namedtuple


# A match with start and end timestamps and a score.
# The score is a float value representing the distance, so smaller is better.
MatchModel = namedtuple('MatchModel', ['start', 'end', 'score'])

# The matched slice of the dataframe along with a projection.
# The projection start should usually be immediately following the match_end.
# TODO separate and define the projection, and rename this type
Projection = namedtuple('Projection', ['window', 'projection_start', 'match_end'])