"""
Used to parse a markdown file for keywords or phrases
returns a list of words and sentences
"""


class MarkDownParser:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

        # This will return a list to be used in the FileScanner
        self.list_to_return: list

    def parse_file(self):
        pass
