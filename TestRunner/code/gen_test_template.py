import argparse
import os
import json
from itertools import takewhile
from utils import suffix
from json_to_unittest import json_to_test_lines

def gen_test_template(lang, dataset_name, question, name):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    template_path = "../template/template" + suffix(lang)
    test_dir = "../unit_tests/" + dataset_name + "/" + lang + "/" + name
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    test_path = test_dir + "/test_template" + suffix(lang)

    file_lines = []
    with open(template_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            file_lines.append(line)

    before = True
    after = False
    test_file_lines_before = []
    test_file_lines_after = []

    indent_space_num = 0

    for line in file_lines:
        if before:
            test_file_lines_before.append(line)
        s_line = line.strip()
        if lang == "python" or lang == "ruby":
            if s_line.startswith("# Write the unit tests here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("# End here"):
                after = True
        else:
            if s_line.startswith("// Write the unit tests here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("// End here"):
                after = True
        if after:
            test_file_lines_after.append(line)

    test_file_lines = []
    for line in test_file_lines_before:
        test_file_lines.append(line)

    tests_lines = json_to_test_lines(question, lang)
    for line in tests_lines:
        test_file_lines.append(" " * indent_space_num + line)

    for line in test_file_lines_after:
        test_file_lines.append(line)

    with open(test_path, "w", encoding="utf-8") as f:
        for line in test_file_lines:
            f.write(line)
        print("Test template generated :" + test_path)