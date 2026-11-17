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

These files are primarily written in the format expected by LeetCode. Some use LeetCode-provided classes such as `TreeNode` or `ListNode`, so they may need a small driver program and the relevant data structures before they can run as standalone files.

For a local Java solution:

```bash
javac Solution.java
java Solution
```

For a standalone Python solution:

```bash
python solution.py
```

Use the actual filename in the selected problem folder. C++ solutions require a C++17-compatible compiler unless the individual solution specifies otherwise.

## Contributing

This is a personal practice repository. Suggestions that improve correctness, readability, edge-case coverage, or explanations are welcome. When suggesting a correction, include the problem ID and a test case that demonstrates the issue.

## Scope

A solution in this repository is a learning record, not a claim that every implementation is optimal. Complexity and edge cases should be checked against the individual problem before relying on a solution.
