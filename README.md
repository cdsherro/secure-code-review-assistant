# Secure Code Review Assistant for a Small App

This project is about testing how useful an LLM is for reviewing code for security issues in a small lab-safe app.

For this project, I am using a small Python web app with intentional security issues so I have a concrete review target for the project. My plan is to review the same code with an LLM, keep track of what it catches, and compare that against a known issue list. The main thing I want to see is whether the LLM gives useful results on a first pass and whether prompt changes make it better later.

## Checkpoint 2 progress

For this checkpoint, I focused on getting a baseline in place.

What I added:
- a small Python web app in `src/sample_app`
- a known issue list for that code
- an initial LLM review
- a before-measurement summary
- updated notes in `/docs`
- environment evidence and screenshots

## Project goal

The goal is not to show that an LLM can replace normal security tools. What I want to test is whether it can help with first-pass review, explain issues in plain language, and improve after I make the prompt more specific.

## Baseline for this checkpoint

My baseline is the first LLM review before I tried to improve the prompt.

For this version, I compared the model’s output against a six-item known issue list for the project test app.

Baseline summary:
- known issues in the project test app: 6
- clearly identified by baseline LLM: 4
- missed: 2
- weak or unsupported finding: 1
- baseline coverage: 66.7%

This gives me a starting point for the next checkpoint.

## What I did this week

This week I mainly worked on getting the project into a form where I can actually measure progress later. At first I was just going to save model findings and talk about them, but that felt too loose. I changed the approach so now I have a known issue list and a simple way to score each version of the review.

I also got the local environment working, confirmed Python and Flask were installed, ran the project locally, and saved screenshots for the checkpoint evidence.

## Folder layout

- `assets/` files that may be used later in the report or presentation
- `data/` notes or small test data if needed later
- `docs/` project updates and method notes
- `evidence/` baseline notes and scoring
- `src/sample_app/` review target
- `prompts/` prompt log
- `report/` report notes
- `screenshots/` checkpoint screenshots
- `scripts/` helper notes and command references

## Next step

For the next checkpoint, I want to revise the prompt so the findings are more specific and better tied to the code. After that I will compare the updated review back to this baseline and see if the results improve.

## Repository link

https://github.com/cdsherro/secure-code-review-assistant
