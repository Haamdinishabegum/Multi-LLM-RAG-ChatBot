from project import get_query

test_cases = [
    "show home team names",
    "show venue names",
    "matches where player salary > 1000"
]

print("\nRunning Test Cases...\n")

for i, question in enumerate(test_cases, 1):
    print("=" * 40)
    print(f"Test Case {i}: {question}")
    print("=" * 40)

    query, result = get_query(question)

    if result is None:
        print("\nResult: Invalid query (column not found)\n")
        continue

    print("\nGenerated Query:\n", query)

    print("\nOutput:\n")
    print(result.head())   # IMPORTANT: only once

print("\nAll test cases executed.\n")