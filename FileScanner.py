"""
This class is going to take a list of words and phrases and scan a folder looking for those words
It will return a list of places where these words are found
"""
from multiprocessing.pool import ThreadPool


class FileScanner:
    def __init__(self, base_directory, word_list):
        self.base_directory = base_directory
        self.word_list = word_list

        # Will return a dict of the file name and then the line where the string was found
        self.found_location = {}

    def find_word(self):
        # This will have the logic to find the word or phrase desired
        pass

    def process_list(self):
        # This will take the words inputted and make strings to scan for
        pass
