#!/usr/bin/env python3
"""
The main file that will handle the input for the file scanner and provide the output
"""
import sys
from FileScanner import FileScanner
from MarkDownParser import MarkDownParser


def display_text(text, level):
    if level == 1:
        print(f"\n[ERROR] {text}")
    elif level == 2:
        print(f"\n[-] {text}")
    elif level == 3:
        print(f"\n[+] {text}")
    else:
        print(f"\n[!] {text}")


if __name__ == "__main__":

    try:
        base_directory = sys.argv[1]
        path_to_md_file = sys.argv[2]

    except IndexError:
        base_directory = None
        path_to_md_file = None
        pass

    word_list = []

    if base_directory is None:
        display_text("Base directory not found", 2)
        base_directory = input("Please enter the full file path to your obsidian folder: ")

    if path_to_md_file is None:
        display_text("MD file not found", 2)
        path_to_md_file = input("Please enter the full file path to your md file to parse: ")

    mdp = MarkDownParser(path_to_md_file)

    word_list = mdp.parse_file()
    print(word_list)

    fs = FileScanner(base_directory, word_list)
