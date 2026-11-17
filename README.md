# LeetCode Solutions

A personal collection of LeetCode problem solutions, organised into numbered folders by problem ID and title.

The repository is used to practise data structures and algorithms, record problem-solving approaches, and revisit solutions while preparing for technical interviews.

## Languages

Solutions currently appear in:

- Python
- Java
- C++

The language used depends on the individual problem. Not every problem has a solution in every language.

## Repository structure

Each problem has its own folder:

```text
<problem-id>-<problem-name>/
├── README.md
└── <solution-file>
```

For example:

```text
100-same-tree/
├── README.md
└── same-tree.java
```

The problem-level README contains the problem statement and examples. The source file contains the corresponding implementation.

## Browsing the solutions

1. Find the problem by its LeetCode ID or title.
2. Open its folder.
3. Read the problem statement and examples in `README.md`.
4. Review the implementation file for the language used.

## Running a solution

Most files follow the format expected by LeetCode rather than being complete standalone programs. For example, a solution may depend on LeetCode-provided types such as `TreeNode` or `ListNode`, and may not include a `main` method.

To run a solution locally, use the matching problem's test harness or create a small driver program that supplies the required data structures and test cases. Use the compiler/runtime version required by the selected language.

## Contributing

This is a personal practice repository. Suggestions that improve correctness, readability, edge-case coverage, or explanations are welcome. When suggesting a correction, include the problem ID and a test case that demonstrates the issue.

## Scope

A solution in this repository is a learning record, not a claim that every implementation is optimal. Complexity and edge cases should be checked against the individual problem before relying on a solution.
