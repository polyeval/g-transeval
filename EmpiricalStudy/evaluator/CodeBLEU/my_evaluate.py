import os

from code_bleu import _code_bleu_single_sentence

def main():
    target_folder = "../../test_target/target/"
    folders = ["../../test_target/transcoder-results/", "../../test_target/transcoder-st-results/",
               "../../test_target/codet5-results/", "../../test_target/codet5-1000-results/",
               "../../test_target/codet5-500-results/", "../../test_target/codet5-200-results/",
               "../../test_target/codet5-100-results/", "../../test_target/codebert-results/",
               "../../test_target/simple-copy/"]

    folders = ["../../test_target/codet5-200-results/", "../../test_target/codet5-100-results/",
               "../../test_target/codebert-results/", "../../test_target/simple-copy/"]

    langs = {"cpp.txt": "cpp", "cs.txt": "c_sharp", "java.txt": "java", "js.txt": "javascript", "py.txt": "python"}

    for folder in folders:
        filenames = os.listdir(folder)
        for filename in filenames:
            source_filename = folder + filename
            lang_file = filename.split("2")[1]
            target_filename = target_folder + lang_file
            lang = langs[lang_file]
            src_codes = []
            tgt_codes = []
            with open(source_filename, 'r', encoding='utf-8') as f:
                for line in f:
                    src_codes.append(line.strip().replace("_", "").lower())
            with open(target_filename, 'r', encoding='utf-8') as f:
                for line in f:
                    tgt_codes.append(line.strip().replace("_", "").lower())

            assert len(src_codes) == 400
            assert len(tgt_codes) == 400

            src_leveled_codes = [[], [], [], []]
            tgt_leveled_codes = [[], [], [], []]

            src_leveled_codes[0] = src_codes[:125]
            src_leveled_codes[1] = src_codes[125:250]
            src_leveled_codes[2] = src_codes[250:375]
            src_leveled_codes[3] = src_codes[375:]
            tgt_leveled_codes[0] = tgt_codes[:125]
            tgt_leveled_codes[1] = tgt_codes[125:250]
            tgt_leveled_codes[2] = tgt_codes[250:375]
            tgt_leveled_codes[3] = tgt_codes[375:]

            level_dict = {"l1": 0, "l2": 1, "l3": 2, "l4": 3}
            for level in ["l1", "l2", "l3", "l4"]:
                pres = src_leveled_codes[level_dict[level]]
                refs = tgt_leveled_codes[level_dict[level]]
                length = len(refs)
                code_bleu_score = 0
                for i in range(length):
                    code_bleu_score += _code_bleu_single_sentence(refs[i], pres[i], lang)
                code_bleu_score = round(code_bleu_score / length * 100, 2)
                print(f"{folder}{filename} {level} : CodeBLEU: {code_bleu_score}")
    # refs = [x.strip() for x in open(args.references, 'r', encoding='utf-8').readlines()]
    # pres = [x.strip() for x in open(args.predictions, 'r', encoding='utf-8').readlines()]
    #
    # assert len(refs) == len(pres)
    #
    # length = len(refs)
    # count = 0
    # for i in range(length):
    #     r = refs[i]
    #     p = pres[i]
    #     if r == p:
    #         count += 1
    # acc = round(count / length * 100, 2)
    #
    # bleu_score = round(_bleu(args.references, args.predictions), 2)

def main2():
    parent_folder = "../../test_target_leveled/l3"

    target_folder = parent_folder + "/target/"

    folders = [parent_folder + "/codebert/", parent_folder + "/codet5/",
               parent_folder + "/naive-copy/", parent_folder + "./transcoder/", parent_folder + "/transcoder-st/"]

    langs = {"cpp.txt": "cpp", "cs.txt": "c_sharp", "java.txt": "java", "js.txt": "javascript", "py.txt": "python"}

    for folder in folders:
        filenames = os.listdir(folder)
        for filename in filenames:
            source_filename = folder + filename
            print(filename, flush=True)
            lang_file = filename.split("2")[1]
            target_filename = target_folder + lang_file
            lang = langs[lang_file]
            src_codes = []
            tgt_codes = []
            with open(source_filename, 'r', encoding='utf-8') as f:
                for line in f:
                    src_codes.append(line.strip().replace("_", "").lower())
            with open(target_filename, 'r', encoding='utf-8') as f:
                for line in f:
                    tgt_codes.append(line.strip().replace("_", "").lower())

            assert len(src_codes) == len(tgt_codes)

            pres = src_codes
            refs = tgt_codes
            length = len(refs)
            count = 0
            code_bleu_score = 0
            for i in range(length):
                r = refs[i].split()
                p = pres[i].split()
                code_bleu_score += _code_bleu_single_sentence(refs[i], pres[i], lang)
            code_bleu_score = round(code_bleu_score / length * 100, 2)
            print(f"{folder}{filename} : CodeBLEU: {code_bleu_score}")
if __name__ == '__main__':
    main2()
