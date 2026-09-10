# Lab 02 CLI comparison journal

Do not include passwords, tokens, API keys, or complete authentication output.

## Tool check

### GitHub Copilot CLI

I installed and authenticated GitHub Copilot CLI. Verification: Copilot v1.0.83.

### Antigravity CLI

I installed and authenticated Antigravity CLI. Verification: Antigravity CLI v1.2.0.

## Shared task

### Shared prompt

```text
Write a Python implementation for this function:

def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case; do not count y."""

Explain your approach briefly and provide the function implementation.
```

### Copilot CLI observations

Copilot suggested using casefold() to handle uppercase and lowercase letters and then checking each character against a set containing the five vowels. I liked this approach because it was simple and easy to understand. The set automatically leaves out y, so there was no extra condition needed for it. I would verify the function with uppercase and lowercase vowels, a word with no vowels, an empty string, and words containing y. These checks would confirm that the function follows the required case-insensitive behavior and only counts a, e, i, o, and u.

### Antigravity CLI observations

Antigravity took a slightly different approach. Instead of changing the text to one case, it created a set containing both lowercase and uppercase vowels. It then went through each character and counted it if it was in that set. I thought this was also a straightforward solution, and the explanation made sense. I would verify that mixed-case words work correctly and that y is not counted. I would also test an empty string, text with no vowels, and text containing punctuation or spaces to make sure only the five required vowels are counted.

### Comparison

Both tools gave me correct solutions, and the main difference was how they handled uppercase and lowercase letters. Copilot used casefold() to make the comparison case-insensitive, while Antigravity put both uppercase and lowercase vowels directly into the set. I thought Copilot's solution was a little cleaner because there were fewer characters to put in the vowel set, but Antigravity's solution was also easy to follow. Neither approach needed a separate check for y because y was not included as a vowel. Both solutions go through the text one character at a time, so their basic approach is similar. I ended up using the Antigravity approach because it was explicit about which characters counted and was easy to compare directly with the function requirements.

## Test-guided implementation

I ran the required tests from the repository root using the command provided in the lab instructions. The grader found 13 tests in total, and all 9 Python behavior tests passed, including the tests for make_greeting, is_even, and count_vowels. The remaining 4 tests were journal checks rather than Python behavior checks. They failed because the journal still contained a template marker and did not yet have the required structure. After reviewing the test output, I identified that “the template marker” needed to be removed and that the required section headings needed to be included. The final count_vowels implementation uses a set containing the uppercase and lowercase versions of a, e, i, o, and u, so it follows the required case-insensitive behavior without counting y.

## Preferred tool combination

A browser chat is useful for getting explanations or working through a problem when I am not necessarily in my code environment. GitHub Copilot in VS Code would be useful when I am already writing code because the suggestions are directly next to the code I am working on. Copilot CLI and Antigravity CLI are useful when I am working in the terminal and want to get suggestions without switching to a browser. For this lab, I liked being able to compare two different CLI responses to the same prompt because it showed that there can be multiple correct ways to solve a simple problem. Right now, I would probably use a browser chat for understanding a problem and then use VS Code or a CLI tool for actually implementing and testing the solution. My preference could change if one of the tools consistently gave better suggestions for more complicated coding tasks.

