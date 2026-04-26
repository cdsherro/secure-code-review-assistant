# Reproducibility

These steps reproduce the final project results.

1. Open the repository: https://github.com/cdsherro/secure-code-review-assistant
2. Review `src/sample_app/app_injection_test.py`.
3. Run the baseline review using `prompts/baseline_review_prompt.md`.
4. Save the output to `evidence/raw_baseline_output.md`.
5. Run the defended review using `prompts/defended_review_prompt.md`.
6. Save the output to `evidence/raw_defended_output.md`.
7. Score both outputs against the six known issues in `evidence/known_issue_list.md`.
8. Update `evidence/comparison_results.md` with the before-vs-after result.

Optional local environment proof:

```powershell
py --version
py -m pip --version
py -m pip install flask
py .\src\sample_app\app.py
```

Final files for packaging:

- `report/Final_Report.pdf`
- `slides/Final_Presentation.pdf`
- tag/release: `final`
