from enum import Enum

lang_suffix = {"cpp": ".cc", "java": ".java", "csharp": ".cs", "javascript": ".js",
               "python": ".py", "php":".php","ruby":".rb","go":".go",
               "java_2":".java","csharp_2":".cs"}


class TestResult(Enum):
    AllPassed = 0
    CompilationPassed = 1
    CompilationFailed = 2


def suffix(lang):
    ret = lang_suffix.get(lang, "")
    return ret
