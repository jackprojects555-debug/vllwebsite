# Development Workflow

## 1. Idea
Write the idea in plain language.

Goal:
- What are we building?
- Who is it for?
- What problem does it solve?

Output:
- Short project idea

---

## 2. SPEC
Create a clear specification before coding.

File:
docs/SPEC.md

Must include:
- Goal
- User flow
- Features
- What is included
- What is not included
- Data structure
- Edge cases
- Success criteria

Rule:
No coding before SPEC is clear.

---

## 3. PROMPT
Convert the SPEC into Cursor instructions.

File:
docs/PROMPT.md

Prompt must include:
- What to build
- Files to edit
- Files not to touch
- Expected behavior
- Constraints
- Testing instructions

Rule:
Cursor receives narrow, specific tasks only.

---

## 4. Branch
Create a feature branch before coding.

Commands:

git checkout main
git pull
git checkout -b feature/name-of-task

Rule:
Never build directly on main.

---

## 5. Cursor Build
Use Cursor only after SPEC and PROMPT are ready.

Rules:
- One task at a time
- Small changes
- No broad rewrites unless requested
- Preserve existing logic
- Ask Cursor to explain changed files

---

## 6. Local Test
Run the project locally before commit.

Commands:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py

Check:
- App runs
- Main flow works
- No terminal errors
- No obvious UI breakage

---

## 7. Review Changes
Check what changed before committing.

Commands:

git status
git diff

Rule:
Do not commit blindly.

---

## 8. Fix / Polish
Fix only what is necessary.

Rules:
- Small fixes
- No unrelated improvements
- No new feature during polish

---

## 9. Update Docs
Before commit, update if needed:

- docs/CHANGELOG.md
- README.md
- PROJECT_SETUP.md
- requirements.txt

Rule:
If behavior changed, documentation changes.

---

## 10. Commit
Commit with a clear message.

Commands:

git add .
git commit -m "Describe the change"

Good examples:
- Add contact search
- Fix data directory gitignore rule
- Add setup instructions
- Improve homepage layout

Bad examples:
- update
- changes
- fix

---

## 11. Push Branch

git push -u origin feature/name-of-task

---

## 12. Pull Request
Open PR on GitHub.

Base:
main

Compare:
feature/name-of-task

PR should include:
- What changed
- How tested
- Notes / risks

---

## 13. Merge to Main
Merge only after review.

Then locally:

git checkout main
git pull

---

## 14. Release / Live Test
If deployed, test the live version.

Check:
- Main page loads
- Main action works
- No visible breakage

---

## 15. Refactor Stage
Once in a while, create a dedicated refactor branch.

Use only for:
- Cleaning code
- Reducing duplication
- Improving structure
- No new features

Branch example:
refactor/cleanup-app-structure

Rule:
Refactor is separate from features.

---

## 16. Tests Stage
Add tests when the project becomes stable.

Use tests for:
- Core logic
- Input parsing
- Data saving
- Important user flows

Rule:
Do not delay product work for perfect tests, but add tests before complexity grows.

---

# Core Rules

1. SPEC before code.
2. PROMPT before Cursor.
3. Branch before changes.
4. Pull before work.
5. Test before commit.
6. Diff before commit.
7. Push after commit.
8. Merge only reviewed work.
9. Refactor separately.
10. Keep tasks small.
