"""
Used to parse a markdown file for keywords or phrases
returns a list of words and sentences
"""
import sys


class MarkDownParser:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

        # This will return a list to be used in the FileScanner
        self.list_to_return = []

    def remove_chars(self, char):
        item_counter = 0
        for item in self.list_to_return:
            if item.__contains__(f"{char}"):
                item = item.replace(f"{char}", "")
                self.list_to_return[item_counter] = item
            item_counter += 1

    def parse_file(self):
        try:
            with open(self.path_to_file, "r") as md_file:
                self.list_to_return = md_file.readlines()
                md_file.close()
        except:
            print("Not able to import file. Exiting...")
            sys.exit()

        # Gets rid of \n and \t in list
        item_counter = 0
        for item in self.list_to_return:
            if item == "\n":
                self.list_to_return.pop(item_counter)
            item_counter += 1

        self.remove_chars("\n")
        self.remove_chars("\t")

        return self.list_to_return
