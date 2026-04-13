# Methodology

This project uses a small Python web app with intentional security problems so I can compare the LLM review against a known issue list.

For the baseline stage, I am keeping the process simple:
1. review the same code with an LLM
2. compare the output against the known issue list
3. mark each issue as clearly identified, missed, or weak
4. save the results in the repo for later comparison

I changed the plan a little from my original idea because I wanted something easier to measure. Instead of just collecting general notes, I am treating this like a before-and-after test. The baseline review is the "before" version. Later, I will refine the prompt and compare the updated results against this first pass.

What I am paying attention to:
- how many real issues the model catches
- what it misses
- whether any findings are too vague
- whether the explanations are actually tied to the code

Everything in this project is lab-safe. I am using a small local Python web app and not using real secrets or real production code.
