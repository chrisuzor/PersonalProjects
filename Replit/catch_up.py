import json


class CatchUp:
    __slots__ = ["stale", "latest", "actions", "current"]

    def __init__(self, stale, latest, actions):
        self.stale = stale
        self.latest = latest
        self.actions = json.loads(actions)
        self.current = len(stale)

    def is_valid(self):
        for action in self.actions:
            if action["op"] == "skip":
                if not self.skip(action["count"]):
                    return "false, skip past end"
            elif action["op"] == "delete":
                if not self.delete(action["count"]):
                    return "false, delete past end"
            elif action["op"] == "insert":
                self.insert(action["chars"])
        return "true"

    def skip(self, count):
        if count > self.current:
            return False
        self.current -= count
        return True

    def delete(self, count):
        if count > self.current:
            return False
        self.current -= count
        return True

    def insert(self, char):
        count = len(char)
        self.current += count


cacth_up = CatchUp(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]',
)

cacth_up2 = CatchUp(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]',
)

cacth_up3 = CatchUp(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "We use operational transformations to keep everyone in a multiplayer repl in sync.",
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]',
)

cacth_up4 = CatchUp(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations.",
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]',
)

cacth_up5 = CatchUp(
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.",
    "[]",
)


print(cacth_up.is_valid())
print(cacth_up2.is_valid())
print(cacth_up3.is_valid())
print(cacth_up4.is_valid())
print(cacth_up5.is_valid())
