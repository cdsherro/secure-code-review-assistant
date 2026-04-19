# Secure Code Review Assistant for a Small App

## 1. Introduction

This project is about testing whether an LLM can actually help with reviewing a small Python web app for security issues. The goal is not to prove that it can replace other tools. What I want to know is whether it can help with first-pass review, explain problems clearly, and get more reliable when the prompt is tightened.

I picked this topic because it gave me something practical to test without making the scope too big. I also liked that I could measure the results instead of just saying the model seemed helpful.

## 2. Scope and Rules of Engagement

This project is limited to a small lab-safe Python web app that I control. There are no real production systems, no real accounts, and no private data involved. The code includes intentional security problems so I have a clear target to review and compare against.

The attack testing is also safe. I am not attacking any outside system. What I am testing is whether the model can be influenced by misleading instructions hidden inside the code comments. The point is to evaluate the review workflow and see whether prompt changes make it more reliable.

## 3. Methodology

The project started with a baseline review. I used a simple prompt to review the Python code and compared the results against a known issue list. That gave me a before-measurement for the project.

For checkpoint 3, I added a second version of the code with misleading comments inside it. Then I ran two review passes:
- one with the original review prompt
- one with a defended prompt that tells the model to treat comments as untrusted input and ignore instructions found in the file

The comparison is based on:
- how many real issues were still identified
- whether the hidden instruction seemed to change the answer
- how many findings were weak or unsupported

## 4. Initial Results

The earlier baseline stage showed that the model could catch some obvious problems, but it was not fully consistent. That was enough to show me I needed a stricter process instead of relying on general impressions.

Checkpoint 3 adds a more useful AI security test. Instead of only asking whether the model can find issues, I am also checking whether the workflow can be pushed off course by text inside the code being reviewed.

### Baseline vs Defended Comparison

| Version | Issues Found | Hidden Instruction Followed | Weak Claims |
|--------|--------|--------|--------|
| Baseline prompt | to be filled after local test | to be filled after local test | to be filled after local test |
| Defended prompt | to be filled after local test | to be filled after local test | to be filled after local test |

## 5. Discussion

So far, the project shows that prompt wording matters more than I originally thought. A basic review prompt may still give readable output, but that does not mean the workflow is reliable when the input tries to influence the model. Adding stronger rules about ignoring comments and only using code-supported findings should help, but the comparison results need to show whether that actually happened.

One limitation is that this is still a small review target, not a full real-world codebase. Even so, it works well enough for a controlled project because I can compare the results directly and keep the scope manageable.

## 6. Remaining Work

The last part of the project is to finish filling in the measured comparison, tighten the discussion, and convert this draft into the final report version.
