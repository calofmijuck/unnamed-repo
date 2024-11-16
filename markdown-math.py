"""
I don't remember what this code does...
It probably indents display math equations so that they match the indentation.
"""

import sys

MATH_REPLACEMENT = [
    ("\\left|", "\\lvert "),
    ("\\right|", "\\rvert "),
    ("\\{", "\\lbrace "),
    ("\\}", "\\rbrace "),
]


def check_if_list(line: str) -> bool:
    def is_ordered_list(line: str) -> bool:
        list_dot = line.find(". ")
        try:
            list_number = line[:list_dot]
            return int(list_number) > 0
        except:
            return False

    def is_unordered_list(line: str) -> bool:
        return line.strip().startswith("- ")

    return is_ordered_list(line) or is_unordered_list(line)


# only called when the line is a list
def calculate_depth(line: str) -> int:
    def count_consecutive_from_start(line: str, pattern: str) -> int:
        count = 0
        while True:
            if line.startswith(pattern):
                count += 1
                line = line[len(pattern):]
            else:
                return count

    return 1 + max(count_consecutive_from_start(line, "\t"), count_consecutive_from_start(line, "  "))


def process_block_equations(split_lines: list[str], nested_depth: int) -> list[str]:
    result_lines = []
    for idx, line in enumerate(split_lines):
        # not equation
        if idx % 2 == 0:
            result_lines.append(line.strip())
        # equation
        else:
            result_lines.append("$$" + line.strip() + "$$")

    # if list, add a tab
    tab_first = "\t" * (nested_depth - 1)
    tab_rest = "\t" * nested_depth
    return [tab_first + result_lines[0]] + [(tab_rest + line) for line in result_lines[1:]]


def print_to_file(out, results: list[str]):
    for line in results:
        # skip empty lines
        if len(line.strip()) == 0:
            continue

        out.write(line)
        out.write("\n\n")


def preprocess(lines: list[str]) -> list[str]:
    joined_lines = "".join(lines)
    for (from_pattern, to_pattern) in MATH_REPLACEMENT:
        joined_lines = joined_lines.replace(from_pattern, to_pattern)

    split_lines = joined_lines.split("$$")

    result = []
    for idx, line in enumerate(split_lines):

        if idx % 2 == 0:
            result.append(line)
        else:
            line = line.replace("\n", "")
            result.append("$$" + line + "$$")

    result = "".join(result)
    result = result.split("\n")
    return result


def split_frontmatter(lines: list[str]) -> tuple[list[str], list[str]]:
    if lines[0] == "---":
        idx = lines[1:].index("---") + 1
        return lines[:idx], lines[idx:]
    else:
        return [], lines


def print_frontmatter(out, frontmatter: list[str]):
    if len(frontmatter) == 0:
        return

    for line in frontmatter:
        out.write(line)
        out.write("\n")


def main(filename: str):
    print(f"[INFO] converting: {filename}...")

    f = open(filename, "r", encoding="utf-8")
    out = open(f"new-{filename}", "w", encoding="utf-8")

    lines = preprocess(f.readlines())

    # handling frontmatter
    frontmatter, content = split_frontmatter(lines)
    print_frontmatter(out, frontmatter)

    results = []
    for _, line in enumerate(content):
        # calculate nested depths for lists
        nested_depth = calculate_depth(line) if check_if_list(line) else 0

        line = line.strip()

        # check for block equations
        split_lines = line.split("$$")
        if len(split_lines) != 1:
            result_lines = process_block_equations(split_lines, nested_depth)
            results.extend(result_lines)
        else:
            tab = "\t" * (nested_depth - 1)
            results.append(tab + line)

    print_to_file(out, results)


if __name__ == "__main__":
    main(sys.argv[1])
