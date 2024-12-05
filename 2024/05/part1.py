#! /usr/bin/env python
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

    print(rules)
    print(manuals)
    for manual in manuals:
        print(manual)
        manual_safe = True
        for page_no in range(len(manual)):
            page = manual[page_no]
            for rule in rules.get(page,[]):
                if rule not in manual:
                    continue
                elif manual.index(rule) < page_no:
                    print("not in order", manual.index(rule), page_no)
                    manual_safe = False
                    break
                else:
                    print("in order", manual.index(rule), page_no)
        if manual_safe:
            print("manual safe")
            manual = [int(i) for i in manual]
            print(manual)
            result += manual[int(len(manual) / 2)]

    return result


if __name__ == "__main__":
    # Read the strategy from the input file.
    with open('input.txt') as f:
        input = f.read()

    # Calculate and print the total score for the strategy.
    result = main(input)
    print("final result: ", result)
