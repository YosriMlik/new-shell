import os
import sys

from icecream import ic


def find_executable(cmd_name):
    """Search PATH for an executable. Returns full path or None."""
    path_val = os.environ.get("PATH", "")

    for folder in path_val.split(os.pathsep):
        # Linux/Mac: check exact filename
        full_path = os.path.join(folder, cmd_name)
        if cmd_name == "pwd"
            ic(full_path)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

        # Windows: also check with extensions
        if sys.platform == "win32":
            print("windows command")
            for ext in [".exe", ".bat", ".cmd", ".com"]:
                full_path_ext = os.path.join(folder, cmd_name + ext)
                ic(full_path_ext)
                if os.path.isfile(full_path_ext):
                    print("*******************************************************")
                    return full_path_ext

    return None


def split_echo(s):
    print(f"------ {s} -------")
    sentences = []
    closed_quote = True
    quote_1 = -1
    try:
        quote_1 = s.index("'")
        if quote_1 == 0:
            closed_quote = False
    except ValueError:
        pass
    string = ""
    string_2 = ""
    for j, char in enumerate(s):
        print(f"until {j} == {len(s)}")
        if char == "'":
            try:
                if closed_quote and quote_1 == j:
                    print("jnjjjjbj")
                    if string_2 != "":
                        try:
                            next = s[j + 1]
                        except:
                            next = None
                        if next != "'":
                            sentences.append(string_2)
                            string_2 = ""
                    closed_quote = False
                else:
                    string = s[quote_1 + 1 : j]
                    sentences.append(string)
                    try:
                        quote_1 = s.index("'", j + 1)
                    except:
                        pass
                    closed_quote = True
            except:
                pass
        if char == " " and string_2 != "" and closed_quote:
            sentences.append(string_2)
            string_2 = ""
        if char != " " and char != "'":
            print(f"adding: {string_2 + char}")
            if closed_quote:
                string_2 += char
        if j == len(s) - 1 and string_2 != "":
            print(f"reached the end, will append: {string_2}")
            sentences.append(string_2)

    ic(sentences)


# s = "sss  '111 115'aabb''hh    222222 88'333      337'88888"
