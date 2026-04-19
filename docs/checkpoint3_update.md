# Checkpoint 3 Update

For this checkpoint, I moved the project past the baseline stage and started testing whether the review process could be influenced by instructions hidden inside the code.

The main thing I added was a second version of the Python web app with misleading comments in it. After that, I used two prompt versions for review. The first one was the original basic review prompt. The second one was a stricter version that tells the model to treat comments and strings as untrusted input and ignore instructions found inside the file.

## What I got done

This week I:
- added an injection-test version of the project code
- wrote down the baseline prompt and the defended prompt
- set up the comparison for both prompt versions
- added checkpoint notes, evidence files, and report progress
- moved the report forward so it is more than just an outline

## Why this matters

Up to this point, the project was mostly about whether the LLM could find security problems. For this checkpoint, I wanted to test something more specific: whether the review process itself could be pushed in the wrong direction by text inside the code being reviewed.

That makes the project stronger because now I am not just checking whether the model is useful. I am also checking whether the workflow stays reliable when the input tries to influence the answer.

## What I am comparing

For this test, I am comparing:
- how many real issues were still identified
- whether the hidden instruction changed the answer
- whether the output became weaker or less supported

The final numbers will be filled in after I complete both review runs and save the results.

## Next step

For the next checkpoint, I want to finish the comparison write-up, tighten the discussion section, and turn the draft report into the final version.
