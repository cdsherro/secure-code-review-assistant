# Testing Notes

For this checkpoint, I wanted to see whether the code review process could be influenced by instructions hidden in code comments.

Files used:
- `src/sample_app/app.py`
- `src/sample_app/app_injection_test.py`

The second file keeps the same risky patterns, but it also includes misleading comments that try to push the review in the wrong direction.

Prompt versions used:
1. baseline review prompt
2. defended review prompt

For both runs, I am checking:
- how many actual issues were still found
- whether the hidden comment seemed to affect the answer
- whether the findings were specific or too weak

This test stays inside the project and does not target anything real. The whole point is just to see whether the review workflow gets more reliable after tightening the prompt.
