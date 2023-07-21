import os
import json

lang_type_str = {
    "cpp": {
        "int": ["int"],
        "double": ["double"],
        "char": ["char"],
        "bool": ["bool"],
        "string": ["string"],
        "any":["any"],
        "list": ["vector<", ">"],
        "dict": ["unordered_map<", ",", ">"],
    },
    "java": {
        "int": ["Integer"],
        "double": ["Double"],
        "char": ["Character"],
        "bool": ["Boolean"],
        "string": ["String"],
        "any":["Object"],
        "list": ["List<", ">"],
        "dict": ["HashMap<", ",", ">"],
    },
    "java_2": {
        "int": ["int"],
        "double": ["double"],
        "char": ["char"],
        "bool": ["boolean"],
        "string": ["String"],
        "any":["Object"],
        "dict": ["HashMap<", ",", ">"],
    },
    "csharp": {
        "int": ["int"],
        "double": ["double"],
        "char": ["char"],
        "bool": ["bool"],
        "string": ["string"],
        "any":["object"],
        "list": ["List<", ">"],
        "dict": ["Dictionary<", ",", ">"],
    },
    "csharp_2": {
        "int": ["int"],
        "double": ["double"],
        "char": ["char"],
        "bool": ["bool"],
        "string": ["string"],
        "any":["object"],
        "dict": ["Dictionary<", ",", ">"],
    }
}


def type_json2str(type_json_obj, lang):
    if lang in lang_type_str.keys():
        if isinstance(type_json_obj, str):
            # print(type_json_obj)
            return lang_type_str[lang][type_json_obj][0]
        if isinstance(type_json_obj, list):
            if lang != "java_2" and lang != "csharp_2":
                return (
                    lang_type_str[lang]["list"][0]
                    + type_json2str(type_json_obj[0], lang)
                    + lang_type_str[lang]["list"][1]
                )
            else:
             return (
                type_json2str(type_json_obj[0], lang)+"[]"
            )
        if isinstance(type_json_obj, dict):
            return (
                lang_type_str[lang]["dict"][0]
                + type_json2str(list(type_json_obj.keys())[0], lang)
                + lang_type_str[lang]["dict"][1]
                + type_json2str(list(type_json_obj.values())[0], lang)
                + lang_type_str[lang]["dict"][2]
            )
    return ""


def content_json2str(content_json_obj, type_json_obj, lang):
    if isinstance(content_json_obj, str):
        if type_json_obj == "int":
            return str(int(content_json_obj))
        if type_json_obj == "double":
            return str(float(content_json_obj))
        if type_json_obj == "bool":
            bool_str = content_json_obj
            if lang == "python":
                bool_str = bool_str[0].upper() + bool_str[1:]
            return bool_str
        if type_json_obj == "char":
            return "'" + json.dumps(content_json_obj)[1:-1] + "'"
        if type_json_obj == "string":
            if lang == "cpp":
                return "string("+json.dumps(content_json_obj)+")"
            else:
                return json.dumps(content_json_obj)
        if type_json_obj == "any":
            split_obj = content_json_obj.split("|ANY_TYPE_SEP|")
            if len(split_obj) != 2:
                print("error: any type parse failed")
                exit(0)
            content_obj = split_obj[0]
            type_obj = split_obj[1]
            return content_json2str(content_obj,type_obj,lang)
        print("error: unknown type")
        exit(0)
    if isinstance(content_json_obj, list):
        if lang == "cpp":
            list_str = "{"
            substrs = []
            for element in content_json_obj:
                substrs.append(content_json2str(element, type_json_obj[0], lang))
            list_str += ",".join(substrs)
            list_str += "}"
            return type_json2str(type_json_obj,lang) + list_str
        if lang == "java":
            list_str = "new ArrayList<>(Arrays.asList("
            substrs = []
            for element in content_json_obj:
                substrs.append(content_json2str(element, type_json_obj[0], lang))
            list_str += ",".join(substrs)
            list_str += "))"
            return list_str
        if lang == "csharp" or lang == "java_2" or lang == "csharp_2":
            list_str = "new "
            list_str += type_json2str(type_json_obj, lang)
            list_str += "{"
            substrs = []
            for element in content_json_obj:
                substrs.append(content_json2str(element, type_json_obj[0], lang))
            list_str += ",".join(substrs)
            list_str += "}"
            return list_str
        if lang == "javascript" or lang == "python" or lang == "php":
            list_str = "["
            substrs = []
            for element in content_json_obj:
                substrs.append(content_json2str(element, type_json_obj[0], lang))
            list_str += ",".join(substrs)
            list_str += "]"
            return list_str
    if isinstance(type_json_obj, dict):
        if lang == "cpp":
            dict_str = "{"
            substrs = []
            for key, value in content_json_obj.items():
                substr = "{"
                substr += content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += ","
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substr += "}"
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "}"
            return type_json2str(type_json_obj,lang) + dict_str
        if lang == "java" or lang == "java_2":
            dict_str = "new "
            dict_str += type_json2str(type_json_obj, lang)
            dict_str += "(Map.of("
            substrs = []
            for key, value in content_json_obj.items():
                substr = content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += ","
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "))"
            return dict_str
        if lang == "csharp" or lang == "csharp_2":
            dict_str = "new "
            dict_str += type_json2str(type_json_obj, lang)
            dict_str += "{"
            substrs = []
            for key, value in content_json_obj.items():
                substr = "{"
                substr += content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += ","
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substr += "}"
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "}"
            return dict_str
        if lang == "javascript":
            dict_str = "new Map(["
            substrs = []
            for key, value in content_json_obj.items():
                substr = "["
                substr += content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += ","
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substr += "]"
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "])"
            return dict_str
        if lang == "python":
            dict_str = "{"
            substrs = []
            for key, value in content_json_obj.items():
                substr = content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += ":"
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "}"
            return dict_str
        if lang == "php":
            dict_str = "["
            substrs = []
            for key, value in content_json_obj.items():
                substr = content_json2str(key, list(type_json_obj.keys())[0], lang)
                substr += "=>"
                substr += content_json2str(
                    value, list(type_json_obj.values())[0], lang
                )
                substrs.append(substr)
            dict_str += ",".join(substrs)
            dict_str += "]"
            return dict_str

# def full_json2str(content_json_obj, type_json_obj, lang="cpp"):
#     if isinstance(content_json_obj, str):
#         return content_json2str(content_json_obj,type_json_obj,lang)
#     else:
#         return type_json2str(type_json_obj,lang)+content_json2str(content_json_obj,type_json_obj,lang)

add_total_sentence={
    "cpp":"total += 1;\n",
    "java":"total += 1;\n",
    "java_2":"total += 1;\n",
    "csharp":"total += 1;\n",
    "csharp_2":"total += 1;\n",
    "python":"total += 1\n",
    "javascript":"total += 1;\n",
    "php":"$total += 1;\n"
}

assign_ret_sentence={
    "cpp":["ret = ",";\n"],
    "java":["ret = ",";\n"],
    "java_2":["ret = ",";\n"],
    "csharp":["ret = ",";\n"],
    "csharp_2":["ret = ",";\n"],
    "python":["ret = ","\n"],
    "javascript":["ret = ",";\n"],
    "php":["$ret = ",";\n"]
}

add_count_sentence={
    "cpp":"count += ret ? 1 : 0;\n",
    "java":"count += ret ? 1 : 0;\n",
    "java_2":"count += ret ? 1 : 0;\n",
    "csharp":"count += ret ? 1 : 0;\n",
    "csharp_2":"count += ret ? 1 : 0;\n",
    "python":"count += 1 if ret else 0\n",
    "javascript":"count += ret ? 1 : 0;\n",
    "php":"$count += $ret ? 1 : 0;\n"
}

equivalent_funcname={
    "cpp":"AreEquivalent",
    "java":"areEquivalent",
    "java_2":"areEquivalent",
    "csharp":"AreEquivalent",
    "csharp_2":"AreEquivalent",
    "python":"are_equivalent",
    "javascript":"areEquivalent",
    "php":"areEquivalent"
}

def json_to_test_lines(question,lang):
    params_type = question["paramsType"]
    return_type = question["returnType"]
    name = "testfunc"
    tests = question["tests"]
    test_strs = []    
    for test in tests:
        test_strs.append(add_total_sentence[lang])
        test_str = assign_ret_sentence[lang][0]
        test_str += equivalent_funcname[lang] + "("
        test_str += name + "("
        params = test["params"]
        expected_return = test["return"]
        substrs = []
        for param, param_type in zip(params, params_type):
            substrs.append(content_json2str(param, param_type, lang))
        test_str += ",".join(substrs)
        test_str += ")"
        test_str += ","
        test_str += content_json2str(expected_return, return_type, lang)
        test_str += ")" + assign_ret_sentence[lang][1]
        test_strs.append(test_str)
        test_strs.append(add_count_sentence[lang])
    return test_strs

if __name__ == "__main__":
    # lang = "cpp"
    # lang = "java"
    # lang = "csharp"
    # lang = "python"
    # lang = "javascript"
    lang = "python"
    with open("../config/ListQueries.json", "r", encoding="utf-8") as f:
        cfg_json = json.load(f)
    questions = cfg_json["questions"]
    for question in questions:
        for line in json_to_test_lines(question,lang):
            print(line)
        # print(json_to_test(question,lang))

# type_json = json.loads('{ "int": [{ "char": "string" }] }')

# content_json = json.loads('{"1":[{"c":"char","i":"int"},{"f":"file","t":"text"}],"2":[{"c":"char","i":"int"},{"f":"file","t":"text"}]}')

# # type_json = json.loads('["int"]')
# # print(type_json2str(type_json, "cpp"))
# # print(type_json2str(type_json, "java"))
# # print(type_json2str(type_json, "csharp"))
# print(content_json)
