from typing import List, NamedTuple


class SplitResult(NamedTuple):
    sentences: List[str]


def split_echo(s) -> str:
    sentences = []
    try:
        quote_1 = s.index("'")
        if quote_1 == 0:
            closed_quote = False
        else:
            closed_quote = True
        string = ""
        string_2 = ""
        for j, char in enumerate(s):
            if char == "'":
                if closed_quote and quote_1 == j:
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
            if char == " " and string_2 != "" and closed_quote:
                sentences.append(string_2)
                string_2 = ""
            if char != " " and char != "'":
                if closed_quote:
                    string_2 += char
            if j == len(s) - 1 and string_2 != "":
                sentences.append(string_2)
    except ValueError:
        pass
    return " ".join(sentences)


# s = "sss  '111 115'aabb''hh    222222 88'333      337'88888"
s = "hello    world"
y = split_echo(s)
print(y)
print(s)
