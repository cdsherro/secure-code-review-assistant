# Secure Code Review Assistant for a Small App

> Checkpoint 1 repository setup for the April cybersecurity project.

## Project Overview
This project will build a lab-only **Secure Code Review Assistant** that uses a large language model to review a small application and flag potential security issues. The main goal is to compare AI-generated code review findings against static analysis tools such as **Semgrep**, **Bandit**, and, if needed for JavaScript components, **ESLint security rules**. The project will measure overlap, missed findings, false positives, and prompt improvements over time.

This project follows the approved **Track A - AI for Security** option for a **Secure Code Review Assistant for a Small App**. The assignment requires a public GitHub repo, steady checkpoint progress, a professional PDF report, and a short presentation. It also requires all AI-track work to remain lab-only, use only authorized code and synthetic data if needed, and include validation/evaluation results.

## Problem Statement
AI can produce fast code review feedback, but it can also miss important vulnerabilities or invent unsupported claims. This project tests whether an LLM can be useful as a first-pass security reviewer when its output is checked against static analysis and the source code itself.

## Target and Scope
The review target for this project will be a **small, intentionally vulnerable, lab-safe application**. The default plan is to use a lightweight Python/Flask sample app because it is easy to review with both an LLM and static analysis tools like Bandit and Semgrep. If the sample app includes frontend JavaScript, ESLint security rules may also be used.

### In Scope
- One small lab-safe application codebase
- Manual review of selected files and functions
- LLM-based code review prompts and structured outputs
- Static analysis with Semgrep and Bandit
- Comparison of AI findings to tool findings
- Documentation of overlap, misses, false positives, and prompt tuning
- Evidence collection, screenshots, and checkpoint updates

### Out of Scope
- Real production applications
- Private or sensitive codebases
- Real user data or real credentials
- Exploitation of systems outside approved lab work
- Any unauthorized scanning or testing

## Repository Structure
```text
.
├── README.md
├── assets/
├── data/
├── docs/
│   └── Project_Charter_Checkpoint1.pdf
├── evidence/
├── prompts/
├── report/
├── scripts/
├── screenshots/
└── src/
```

### Folder Purpose
- `docs/` - project charter, planning notes, checkpoint documents
- `src/` - the sample app or target code under review
- `scripts/` - helper scripts for parsing findings or comparing outputs
- `prompts/` - prompt log, prompt revisions, and structured AI review templates
- `evidence/` - raw tool output, notes, screenshots, and validation records
- `report/` - final report draft, figures, and final PDF
- `data/` - normalized findings and comparison tables
- `assets/` - diagrams and supporting visuals
- `screenshots/` - screenshots used in checkpoints and final report

## Planned Workflow
1. Select or build a small intentionally vulnerable sample application.
2. Save the target code in `src/`.
3. Run static analysis tools such as Bandit and Semgrep against the codebase.
4. Save raw tool output in `evidence/`.
5. Prompt the LLM to review the same code and return:
   - suspected vulnerabilities
   - severity estimate
   - explanation of the risk
   - remediation suggestions
6. Normalize both AI and static tool findings into a comparison table.
7. Measure:
   - overlap between LLM and tool findings
   - LLM-only findings that are valid
   - LLM false positives
   - findings missed by the LLM
8. Improve prompts and document whether the results get better.

## Methodology Plan
The project will use a repeatable review process:

- choose a fixed sample app and document why it was selected
- establish a baseline static analysis result
- run the LLM with a structured review prompt
- manually verify important findings against the actual code
- record which claims were supported, unsupported, or partially correct
- repeat after prompt tuning and compare results

## Planned Tools
- Git and GitHub
- Python
- Semgrep
- Bandit
- ESLint security rules (if JavaScript is included)
- Markdown and PDF reporting
- ChatGPT or another approved LLM for code review assistance

## Validation Plan
Because the project uses AI, every major LLM claim will be checked against the source code and the static analysis output before it is counted as a valid result. Validation will include:

- matching the finding to a real code location
- checking whether the vulnerability explanation is technically correct
- checking whether severity wording is supported
- comparing the LLM finding to Semgrep/Bandit results
- documenting false positives and missed issues
- documenting how prompt changes affect quality

## Milestones
### Week 2 - Checkpoint 1
- initialize public repo
- upload README and project charter PDF
- define project scope, ROE, and methodology
- set up folder structure and planning documents

### Week 3 - Checkpoint 2
- choose or create the sample app
- run first static analysis baseline
- draft first LLM review prompts
- save evidence and screenshots

### Week 4 - Checkpoint 3
- compare AI findings to static analysis results
- verify true positives and false positives
- refine prompts and record changes
- begin final report sections

### Final Week - Checkpoint 4 / Final Submission
- finalize comparison tables and conclusions
- complete PDF report
- polish repository evidence
- prepare presentation slides

## Success Criteria
The project will be on track if:
- the repo stays organized and updated at each checkpoint
- the target codebase is clearly documented and lab-safe
- the AI review process is repeatable
- the report includes overlap, misses, false positives, and prompt improvements
- major claims are supported by source code and tool evidence
- the `checkpoint-1` tag is created for this submission

## Ethics and Safety Statement
This project is limited to authorized educational work only. The code under review will be a lab-safe sample application, not a real production system. No real secrets, real user data, or unauthorized targets will be used. If test credentials or secret-like values are needed, they will be synthetic and clearly labeled. Findings will be reported honestly, including cases where the LLM is wrong or incomplete.

## Checkpoint 1 Git Commands
```bash
git init
git add .
git commit -m "Checkpoint 1 - Secure Code Review Assistant setup"
git branch -M main
git remote add origin <your-public-repo-url>
git push -u origin main
git tag checkpoint-1
git push origin checkpoint-1
```

## Submission Checklist
- public GitHub repo link added to Canvas
- professional repo structure pushed to GitHub
- `README.md` initialized
- `Project_Charter_Checkpoint1.pdf` uploaded in the repo
- `checkpoint-1` tag created

## Repo Link
Replace this placeholder before you submit:

`https://github.com/<username>/secure-code-review-assistant`
