# Compares dictionary key to list index
code_snippets = {
    "dictionary_snippet": {
        "code": "numbers = {}\nnumbers[0] = -5\nnumbers[1] = 10.5",
        "explanation": "Dictionaries allow it to assign values to new keys. 0 and 1 should be keys.",
        "fixed": None
    },
    "list_snippet": {
        "code": "other_numbers = []\nother_numbers[0] = -5\nother_numbers[1] = 10.5",
        "explanation": "Lists don't allow the assignment to indexes that aren't made yet which causes an IndexError.",
        "fixed": "other_numbers = []\nother_numbers.append(-5)\nother_numbers.append(10.5)"
    }
}

if __name__ == '__main__':
    for key, data in code_snippets.items():
        print(f"--- Testing: {key.replace('_', ' ').title()} ---")
        print(f"Original Code:\n{data['code']}")
        print(f"\nExplanation: {data['explanation']}")

        if data['fixed']:
            print(f"\nFixed Code:\n{data['fixed']}")

        print("-" * 40 + "\n")