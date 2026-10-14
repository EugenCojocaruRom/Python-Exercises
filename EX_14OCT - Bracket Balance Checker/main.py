#Print header and separator
print("<-- Bracket Balance Checker -->")
print("-------------------------------")

#Create function for checking the brackets
def check_brackets(text):
    bracket_pairs = {")": "(", "]": "[", "}": "{"}
    closers = {"(": ")", "[": "]", "{": "}"}
    brackets_stack = []
    #Loop over the text
    for i, ch in enumerate(text):
        if ch in "([{":
            brackets_stack.append((ch, i))
        elif ch in bracket_pairs:
            if not brackets_stack:
                return f"Unexpected '{ch}' at position {i}"
            last_opener, last_pos = brackets_stack.pop()
            if last_opener != bracket_pairs[ch]:
                return f"Mismatch: expected '{closers[last_opener]}' but found '{ch}' at position {i}"
    if brackets_stack:
        opener, pos = brackets_stack[0]
        return f"Unclosed '{opener}' at position {pos}"
    return "Balanced"

#Have a list of strings containing brackets
tests = [
    "(a + b) * [c - d]",
    "{[()]}",
    "(]",
    "((3 + 4)",
    "x + y)",
    "",
    "x + (y"
]

#Create dictionary to store the results
results = {t: check_brackets(t) for t in tests}

#Filter the strings that are balanced
balanced = [t for t, message in results.items() if message == "Balanced"]
print("Balanced strings:")
for t in balanced:
    print(" -", t, "->", results[t])

#Filter the strings that are not balanced
not_balanced = [t for t, message in results.items() if message != "Balanced"]
print("\nNot balanced strings:")
for t in not_balanced:
    print(" -", t, "->", results[t])

#Print summary
print("\n=== SUMMARY ===")
print(f"Not balanced strings: {len(not_balanced)}")
print(f"Balanced strings: {len(tests) - len(not_balanced)}")
