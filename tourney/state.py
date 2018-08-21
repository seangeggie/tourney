import os
import json

from .constants import DATA_PATH

class State:
  __instance = None

  def __init__(self):
    if not State.__instance:
      self.reset()
      try:
        self.load()
      except Exception as ex:
        print("State file could not load: {}".format(self.file_path()))
        print(ex)

      State.__instance = self

  @staticmethod
  def get():
    if not State.__instance:
      return State()
    return State.__instance

  def set_bot_id(self, bot_id):
    self.__bot_id = bot_id

  def bot_id(self):
    return self.__bot_id

  def set_channel_id(self, channel_id):
    self.__channel_id = channel_id

  def channel_id(self):
    return self.__channel_id

  def set_participants(self, participants):
    self.__participants = participants

  def add_participant(self, participant):
    self.__participants.append(participant)

  def remove_participant(self, participant):
    self.__participants.remove(participant)

  def participants(self):
    return self.__participants

  def set_morning_announce(self, ts):
    self.__morning_announce = ts

  def morning_announce(self):
    return self.__morning_announce

  def set_reminder_announce(self, ts):
    self.__reminder_announce = ts

  def reminder_announce(self):
    return self.__reminder_announce

  def set_midday_announce(self, midday_announce):
    self.__midday_announce = midday_announce

  def midday_announce(self):
    return self.__midday_announce

  def set_teams(self, teams):
    self.__teams = teams

  def teams(self):
    return self.__teams

  def set_unrecorded_matches(self, unrecorded_matches):
    self.__unrecorded_matches = unrecorded_matches

  def unrecorded_matches(self):
    return self.__unrecorded_matches

  def file_path(self):
    return os.path.expanduser("{}/state.json".format(DATA_PATH))

  def reset(self):
    self.__bot_id = None
    self.__channel_id = None
    self.__participants = []
    self.__morning_announce = None
    self.__reminder_announce = None
    self.__midday_announce = False
    self.__teams = []
    self.__unrecorded_matches = []

  def save(self):
    data = {
      "bot_id": self.bot_id(),
      "channel_id": self.channel_id(),
      "participants": self.participants(),
      "morning_announce": self.morning_announce(),
      "reminder_announce": self.reminder_announce(),
      "midday_announce": self.midday_announce(),
      "teams": self.teams(),
      "unrecorded_matches": self.unrecorded_matches()
    }
    os.makedirs(os.path.dirname(self.file_path()), exist_ok=True)
    with open(self.file_path(), "w+") as fp:
      json.dump(data, fp, indent=2)

  def load(self):
    with open(self.file_path(), "r") as fp:
      data = json.load(fp)
      if "bot_id" in data:
        self.set_bot_id(data["bot_id"])
      if "channel_id" in data:
        self.set_channel_id(data["channel_id"])
      if "participants" in data:
        self.set_participants(data["participants"])
      if "morning_announce" in data:
        self.set_morning_announce(data["morning_announce"])
      if "reminder_announce" in data:
        self.set_reminder_announce(data["reminder_announce"])
      if "midday_announce" in data:
        self.set_midday_announce(data["midday_announce"])
      if "teams" in data:
        self.set_teams(data["teams"])
      if "unrecorded_matches" in data:
        self.set_unrecorded_matches(data["unrecorded_matches"])
