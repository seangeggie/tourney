# Will print all read events to stdout.
DEBUG = False

CHANNEL_NAME = "foosball"
RTM_READ_DELAY = 0.5 # seconds
COMMAND_REGEX = "!(\\w+)\\s*(.*)"

MORNING_ANNOUNCE_HOUR = 9
MIDDAY_ANNOUNCE_HOUR = 11
MIDDAY_ANNOUNCE_MINUTE = 50

POSITIVE_REACTIONS = ["+1", "the_horns", "metal", "raised_hands", "ok", "ok_hand"]
NEGATIVE_REACTIONS = ["-1", "middle_finger"]