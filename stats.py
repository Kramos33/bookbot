from typing import Any


def number_of_words(text):
    num_words = len(text.split())
    print(f" Found {num_words} total words")

def number_of_characters(text: str) -> dict[str, int]:
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_by_greatest_to_least(char_counts: dict[str, int]) -> list[dict]:
    sorted_items = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    result = []
    for char, count in sorted_items:
        result.append({"char": char, "count": count})
    return result

