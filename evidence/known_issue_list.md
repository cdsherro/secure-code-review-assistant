# Known Issue List

The Python web app in this project includes intentional security problems so I can test baseline LLM review behavior.

## Known issues

1. Hardcoded secret key in the application
2. Hardcoded admin password
3. Unsafe use of `eval` on user-controlled input
4. Use of `subprocess.run(..., shell=True)` with unsanitized input
5. SQL query built through string formatting instead of parameterized input
6. Debug mode enabled in the application

## Purpose of this list

This list is being used as the comparison target for the baseline checkpoint. I am using it to score what the LLM clearly identified, what it missed, and what was too weak to count.
