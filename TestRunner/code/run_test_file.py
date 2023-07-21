import argparse
import os
import subprocess
import json
from utils import suffix, TestResult


def run_test_file(lang, dataset_name, question_name):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    test_dir = "../unit_tests/" + dataset_name + "/" + lang + "/" + question_name
    test_path = test_dir + "/test" + suffix(lang)

    ret_status = TestResult.CompilationFailed
    run_output = ""
    print("Running test file :" + test_path)
    try:
        if lang == "cpp":
            subprocess.run(["g++","-O2","-std=c++20", test_path, "-o", f"{test_dir}/out.o"])
            if os.path.exists(f"{test_dir}/out.o"):
                run_output = subprocess.check_output([f"{test_dir}/out.o"],timeout=5)
                os.remove(f"{test_dir}/out.o")
        elif lang == "java" or lang == "java_2":
            run_output = subprocess.check_output(["java", test_path],timeout=5)
        elif lang == "csharp" or lang == "csharp_2":
            run_output = subprocess.check_output(["dotnet-script", test_path],timeout=5)
        elif lang == "javascript":
            run_output = subprocess.check_output(["node", test_path],timeout=5)
        elif lang == "python":
            run_output = subprocess.check_output(["python3", test_path],timeout=5)
        elif lang == "php":
            run_output = subprocess.check_output(["php", test_path],timeout=5)
        elif lang == "ruby":
            run_output = subprocess.check_output(["ruby", test_path],timeout=5)
        elif lang == "go":
            run_output = subprocess.check_output(["go", "run", test_path],timeout=5)
    except:
        pass
    run_output = str(run_output)
    if run_output.find("All Passed!") != -1:
        ret_status = TestResult.AllPassed
    elif run_output.find("Compilation Passed!") != -1:
        ret_status = TestResult.CompilationPassed
    return ret_status
