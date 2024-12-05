#! /usr/bin/env python
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


def main(input):
    result = 0

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
            manual = [int(i) for i in manual]
            # print(manual, manual[int(len(manual) / 2)])
            result += manual[int(len(manual) / 2)]

    return result

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
    # Read the strategy from the input file.
    with open("input.txt") as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
