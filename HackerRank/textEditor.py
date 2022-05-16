class TextEditor:

    __slots__ = ["string", "last_action", "undo_key"]

    def __init__(self):
        self.string = ""
        self.last_action = []
        self.undo_key = False

    def delete(self, count):
        len_to_remove = len(self.string) - count
        if len_to_remove > 0:
            if not self.undo_key:
                self.last_action.append(("1", self.string[len_to_remove:]))
            self.string = self.string[:len_to_remove]
        else:
            if not self.undo_key:
                self.last_action.append(("1", self.string))
            self.string = ""

    def append(self, str):
        self.string += str
        if not self.undo_key:
            self.last_action.append(("2", len(str)))

    def print_letter(self, index):
        print(self.string[index - 1])

    def process_lines(self, line):
        commands = line.split(" ")
        self.perform_command(commands)

    def undo(self):
        commands = self.last_action.pop()
        self.undo_key = True
        self.perform_command(commands)
        self.undo_key = False

    def perform_command(self, commands):
        if commands[0] == "1":
            self.append(commands[1])
        elif commands[0] == "2":
            self.delete(int(commands[1]))
        elif commands[0] == "3":
            self.print_letter(int(commands[1]))
        elif commands[0] == "4":
            self.undo()


text_editor = TextEditor()
text_editor.perform_command(["1", "abc"])
text_editor.perform_command(["3", "3"])
text_editor.perform_command(["2", "3"])
text_editor.perform_command(["1", "xy"])
text_editor.perform_command(["3", "2"])
text_editor.perform_command(["4"])
text_editor.perform_command(["4"])
text_editor.perform_command(["3", "1"])
