# Creating a New Project

## 1. Clone Template

cd ~/Projects
git clone https://github.com/YOUR_USERNAME/python-project-template.git my_new_project
cd my_new_project

## 2. Reset Git

rm -rf .git
git init

## 3. Update Project Name

Edit:

- README.md
- PROJECT_SETUP.md

Replace "Project Name" with your project name.

## 4. Setup Environment

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## 5. Define the Project

docs/SPEC.md

Write:
- What you are building
- Main flow
- Features

## 6. Create Prompt

docs/PROMPT.md

Define:
- What Cursor should build
- Which files to edit
- Expected behavior

## 7. Start Development

Follow docs/WORKFLOW.md

## Core Rule

Do not start coding before SPEC and PROMPT are clear.
