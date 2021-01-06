"""
Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products
after each character of searchWord is typed.

Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
"""
import bisect


def suggested_products(products, search_word: str):
    products = sorted(products)  # O(nlogn)
    results = []
    i = 0
    prefix = ""
    for c in search_word:
        prefix += c
        i = bisect.bisect_left(products, prefix, i)  # O(logn)
        suggestions = [w for w in products[i : i + 3] if w.startswith(prefix)]
        results.append(suggestions)
    return results


if __name__ == "__main__":
    result = [
        ["mobile", "moneypot", "monitor"],
        ["mobile", "moneypot", "monitor"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
        ["mouse", "mousepad"],
    ]
    assert (
        suggested_products(
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"
        )
        == result
    )
