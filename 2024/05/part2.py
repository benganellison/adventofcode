#! /usr/bin/env python
from timeit import repeat
def fix_manual(manual, rules):
    fixed = False
    for page_no in range(len(manual)):
        page = manual[page_no]
        for rule in rules.get(page, []):
            if rule in manual and manual.index(rule) < page_no:
                manual.remove(rule)
                manual.insert(page_no, rule)
                fixed = True
    if fixed:
        return fix_manual(manual, rules)
    return manual


def main():
    result = 0
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()


    rules = {}
    for rule in input.split("\n\n")[0].split("\n"):
        first, second = rule.split("|")
        if first not in rules:
            rules[first] = [second]
        else:
            rules[first].append(second)

    manuals = [manual.split(",") for manual in input.split("\n\n")[1].split("\n")]

    # print(rules)
    # print(manuals)
    for manual in manuals:
        # print(manual)
        manual_safe = is_manual_safe(rules, manual)
        if not manual_safe:
            # print("manual not safe")
            manual = fix_manual(manual, rules)
            # print("manual safe")
            # print(manual, manual[int(len(manual) / 2)])
            result += int(manual[int(len(manual) / 2)])

    # print("final result: ", result)

def is_manual_safe(rules, manual):
    manual_safe = True
    for page_no in range(len(manual)):
        page = manual[page_no]
        for rule in rules.get(page, []):
            if rule not in manual:
                continue
            elif manual.index(rule) < page_no:
                    # print("not in order", manual.index(rule), page_no)
                manual_safe = False
                break
            else:
                    # print("in order", manual.index(rule), page_no)
                pass
    return manual_safe


if __name__ == "__main__":

    result_new = repeat(main, number=1, repeat=100)

    def print_statistics(results, label):
        min_result = min(results)
        max_result = max(results)
        avg_result = sum(results) / len(results)
        std_dev = (sum((x - avg_result) ** 2 for x in results) / len(results)) ** 0.5
        print(
            f"{label} Min: {min_result:.5f}, Max: {max_result:.5f}, Avg: {avg_result:.5f}, Std Dev: {std_dev:.5f}"
        )

    print_statistics(result_new, "New")
