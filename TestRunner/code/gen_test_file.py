import os
from itertools import takewhile
from utils import suffix

def replace_func_name(code):
    code_toks = code.split(' ')
    func_name = ""
    for i in range(len(code_toks)):
        if code_toks[i].strip() == "(":
            func_name = code_toks[i - 1]
            break
    for i in range(len(code_toks)):
        if code_toks[i].strip() == func_name:
            code_toks[i] = "testfunc"
    result = " ".join(code_toks)
    return result

def reformat_input(code,lang):
    if lang == "ruby" or lang == "go":
        return code.replace("NEW_LINE", "\n")
    elif lang == "php":
        return code.replace("$ ", "$")
    elif lang == "python":
        code_lines = [line.strip() for line in code.split("NEW_LINE")]
        new_code_lines = []
        indent_num = 0
        for line in code_lines:
            while line[0:6] == "INDENT" or line[0:6] == "DEDENT":
                if line[0:6] == "INDENT":
                    line = line[6:].strip()
                    indent_num += 1
                if line[0:6] == "DEDENT":
                    line = line[6:].strip()
                    indent_num -= 1
            line = " " * (4 * indent_num) + line
            new_code_lines.append(line)
        return "\n".join(new_code_lines)
    return code


def gen_test_file(lang, dataset_name, question_name, input):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    test_dir = (
        "../unit_tests/" + dataset_name + "/" + lang + "/" + question_name
    )
    template_path = test_dir + "/test_template" + suffix(lang)
    test_path = test_dir + "/test" + suffix(lang)

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
            if s_line.startswith("# Write the target function here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("# End here"):
                after = True
        else:
            if s_line.startswith("// Write the target function here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("// End here"):
                after = True
        if after:
            test_file_lines_after.append(line)

    test_file_lines = []
    for line in test_file_lines_before:
        test_file_lines.append(line)

    code = reformat_input(replace_func_name(input),lang)

    test_file_lines.append(" " * indent_space_num + code + "\n")

    for line in test_file_lines_after:
        test_file_lines.append(line)

    with open(test_path, "w", encoding="utf-8") as f:
        for line in test_file_lines:
            f.write(line)
        print("Test file generated :" + test_path)


def gen_test_file_no_format(lang, dataset_name, question_name, input):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    test_dir = (
        "../unit_tests/" + dataset_name + "/" + lang + "/" + question_name
    )
    template_path = test_dir + "/test_template" + suffix(lang)
    test_path = test_dir + "/test" + suffix(lang)

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
            if s_line.startswith("# Write the target function here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("# End here"):
                after = True
        else:
            if s_line.startswith("// Write the target function here"):
                before = False
                indent_space_num = len(list(takewhile(str.isspace, line)))
            if before == False and s_line.startswith("// End here"):
                after = True
        if after:
            test_file_lines_after.append(line)

    test_file_lines = []
    for line in test_file_lines_before:
        test_file_lines.append(line)

    code = replace_func_name(input)

    test_file_lines.append(" " * indent_space_num + code + "\n")

    for line in test_file_lines_after:
        test_file_lines.append(line)

    with open(test_path, "w", encoding="utf-8") as f:
        for line in test_file_lines:
            f.write(line)
        print("Test file generated :" + test_path)