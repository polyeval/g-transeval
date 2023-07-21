import os
import subprocess
import json

if __name__ == "__main__":
    langs = ["cpp", "java", "python", "javascript","csharp"]
    suffix = {"cpp":"cc","java":"java","python":"py","javascript":"js","csharp":"cs"}
    levels  = ["l1","l2","l3","l4"]

    for lang in langs:
        with open(fr"../gold_answer/all/test.{suffix[lang]}","r",encoding="utf-8") as f:
            codes = []
            for line in f:
                codes.append(line)
        codes_levels = []
        codes_levels.append(codes[:125])
        codes_levels.append(codes[125:250])
        codes_levels.append(codes[250:375])
        codes_levels.append(codes[375:])
        for level, codes_level in enumerate(codes_levels):
            level += 1
            path = f"../gold_answer/l{level}"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"../gold_answer/l{level}/test.{suffix[lang]}","w",encoding="utf-8") as f:
                for line in codes_level:
                    f.write(line)

    for level in levels:
        for lang in langs:
            params = ["python","run.py", "--gen_template", "--gen_test", "--run_test"]
            params += ["--lang", lang]
            params += ["--unit_test_config",f"../config/{level}.json"]
            params += ["--test_file",f"../gold_answer/{level}/test.{suffix[lang]}"]
            params += ["--out_name", f"../results/gold/{level}-{lang}.json"]
            proc = subprocess.Popen(params)