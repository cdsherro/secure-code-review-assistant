# Checkpoint 2 Update

For this checkpoint, I worked on getting a baseline in place for the Secure Code Review Assistant project.

The main thing I did was move from just having a project idea to having something I can actually measure. I picked a small Python web app, wrote down the known issues in it, ran an initial LLM review, and then compared that output against the known issue list.

## What I completed

This week I:
- kept the repo organized and fixed the root structure
- added a small Python web app under `src/sample_app`
- documented a six-item known issue list
- saved a baseline LLM review
- wrote a before-measurement summary
- updated the project method and next steps in `/docs`
- verified the local Python environment and ran the project locally

## Baseline result

The baseline for this checkpoint is the first-pass LLM review using a simple prompt.

Results:
- total known issues: 6
- clearly identified by baseline LLM: 4
- missed by baseline LLM: 2
- weak or unsupported finding: 1
- baseline coverage: 66.7%

That gives me the before-measurement I need for the AI/LLM part of the project.

## What I noticed

The first review did a decent job on the more obvious problems, especially risky patterns like `eval`, `shell=True`, and hardcoded secrets. It was less consistent on other issues, and one of the findings was too broad to count as a strong result. That showed me pretty quickly that I need a better prompt and a stricter way to score the output.

## Method changes

After doing the baseline, I changed the method a little.

Instead of just saving whatever the model says and describing it later, I am now doing this:
1. keep a known issue list for the target code
2. save the raw model output
3. score the findings as correct, missed, or weak
4. compare later prompt versions back to the baseline

That makes the project easier to measure and easier to explain in the report.

## Next steps

For the next checkpoint, I want to improve the prompt so the model gives more specific findings and better support for each one. I also want to make the comparison table cleaner so I can reuse it in the final report.
