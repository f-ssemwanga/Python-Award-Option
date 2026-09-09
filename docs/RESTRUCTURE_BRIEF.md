# Python Award Option: Restructure Brief

Author: F. Ssemwanga
Working branch: `course-restructure`
Purpose: repair repository hygiene, rebalance the scheme of work, and add a
second lane for students arriving with GCSE Computer Science.

Execute the phases in order. Commit at the end of each phase using the message
given. Do not squash phases together. Do not rewrite git history at any point.

---

## Context you need before you start

This course was written for students who did **not** take programming at GCSE.
It runs as an award option alongside A Levels and prepares students for post-18
study.

A second intake now arrives having done GCSE Computer Science (AQA 8525). Those
students already hold: sequence, selection, iteration, subroutines, lists and
arrays, string handling, basic file read and write, and SQL from spec section
3.7. They have **not** met object-oriented programming, exception handling with
`try`/`except`, dictionaries or sets, version control, or writing Python that
talks to a database in code.

Both groups sit in the same room at the same time. This is the single most
important constraint in this brief. It means:

- Both lanes must always be on the **same topic** in the same lesson, differing
  only in depth. Never put the two lanes on different topics. If they diverge by
  topic, whole-class teaching, plenaries and pair work all become impossible.
- Lane membership is decided **per week, not per student for the whole course**.
  A GCSE student may run Fast Track for Weeks 1 to 4 and drop back to Core for
  Week 5, because exception handling is new to everyone. Nothing in the
  materials should imply fixed streaming.

The two lanes are named **Core** and **Fast Track** throughout. If Mr Ssemwanga
prefers different names, they are defined in one place only (see Phase 4) so a
rename is a single find and replace.

---

## Phase 1: repository hygiene

These are defects found in an audit of the repository. Fix all of them.

### 1.1 Duplicate portfolio guide

`Portfolio_Guidance.ipynb` and `Portfolio_Setup_ Guidance.ipynb` contain
byte-identical markdown. The second also has a stray space in its filename.

Delete `Portfolio_Setup_ Guidance.ipynb`. Keep `Portfolio_Guidance.ipynb`.

### 1.2 Duplicated Git guidance

`Resources.ipynb` at the root duplicates roughly half of
`Week1/usingGitHub.ipynb`. Same walkthrough, two files, guaranteed to drift.

`Resources.ipynb` does contain two sections that `usingGitHub.ipynb` lacks:
"Installing Git on a Raspberry Pi" and "Other useful git commands".

Merge those two sections into `Week1/usingGitHub.ipynb` as new cells at the end,
then delete `Resources.ipynb`. Do not lose the Raspberry Pi content.

### 1.3 Folder casing

`Week1`, `Week2`, `Week3`, `Week6`, `Week7` are capitalised. `week4` and `week5`
are not. This breaks links on case-sensitive filesystems and on GitHub Pages.

Rename `week4` to `Week4` and `week5` to `Week5`.

Windows and macOS use case-insensitive filesystems, so a direct rename is a
no-op. Use the two-step form:

```
git mv week4 tmp_week4 && git mv tmp_week4 Week4
git mv week5 tmp_week5 && git mv tmp_week5 Week5
```

Verify with `git status` that git has recorded a rename, not a deletion.

### 1.4 Filename typos

`week4/week4-python-itro.ipynb` and `week5/week5-python-itro.ipynb` are both
missing the "n" in "intro".

Rename to `Week4/Week4-python-intro.ipynb` and `Week5/Week5-python-intro.ipynb`.

Then grep the whole repository for any links to the old paths and update them.

### 1.5 Orphaned image

`images/initiasGen.png` is referenced by nothing. `images/initialsGen.png` is
the live file, referenced once. The orphan is a typo-named leftover.

Delete `images/initiasGen.png`. Confirm first with a repository-wide grep that
nothing references it.

### 1.6 Stray database file

`students.db` at the repository root is zero bytes. The real seed database is
`Week7/students.db`.

Delete the root `students.db`. Keep `Week7/students.db`, which becomes
`Week9/students.db` in Phase 2.

### 1.7 Scratch files shipped to students

Delete these. They are working files, not teaching material:

- `Week1/testpage.ipynb`
- `Week7/sqliteTestDB.ipynb`
- the entire `testFiles/` directory

### 1.8 Solutions are public

**This is the serious one.** `solutions/week1_solutions.ipynb` and
`solutions/Week2.ipynb` are both tracked in git. The existing `.gitignore`
attempts to exclude the first, but the rule does not work, for two reasons:
`.gitignore` has no effect on files that are already tracked, and the file has a
CRLF line ending, so the pattern carries a stray carriage return.

Anyone who clones or forks this repository gets the answers.

Do this:

```
git rm -r --cached solutions
```

Leave the files on disk. They stay in Mr Ssemwanga's local working copy and stop
being tracked from this commit forward.

**Decision still open, do not act on it without asking:** the two solution
notebooks remain in the public history on GitHub and in every existing clone.
Removing them from history means a force push, which breaks every student fork.
The recommendation is to accept the exposure of those two files, move solutions
to a separate private repository, and not rewrite history. Flag this and wait
for a decision rather than deciding it yourself.

### 1.9 Rewrite .gitignore

Replace the contents entirely. Write with **LF line endings**, not CRLF.

```
# Solutions are kept locally and published to a separate private repo
solutions/

# Jupyter
.ipynb_checkpoints/
*/.ipynb_checkpoints/

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Student-generated databases and data files
*.db
!Week9/students.db
*.pickle
*.pkl

# OS
.DS_Store
Thumbs.db
```

The negation line matters. `Week9/students.db` is a seed database the lesson
depends on and must stay tracked.

**Commit message for Phase 1:**
`chore: repository hygiene, remove duplicates, scratch files and tracked solutions`

---

## Phase 2: rebalance the scheme of work

The README promises ten topics. The repository delivers seven week folders, and
Week 7 is carrying six notebooks covering three separate topics.

Current Week 7 contents:

- `week7-python-intro.ipynb` (OOP basics)
- `week7-extendedOopTasks.ipynb` (inheritance and extension tasks)
- `Week7-persistentObjects.ipynb` (pickle)
- `Week7-PersistentObjects_sqlite.ipynb` (saving objects to SQLite)
- `Week7_database_intro.ipynb` (databases and SQL from first principles)
- `students.db`

Split into four weeks:

| Week   | Topic                              | Files                                                                                                                                                            |
| ------ | ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Week7  | Object-oriented programming        | `week7-python-intro.ipynb`, `week7-extendedOopTasks.ipynb`                                                                                                       |
| Week8  | Persistence: from files to objects | `Week7-persistentObjects.ipynb` renamed `Week8-persistent-objects.ipynb`                                                                                         |
| Week9  | Databases and Python integration   | `Week7_database_intro.ipynb` renamed `Week9-database-intro.ipynb`, `Week7-PersistentObjects_sqlite.ipynb` renamed `Week9-objects-to-sqlite.ipynb`, `students.db` |
| Week10 | Portfolio project                  | new, see below                                                                                                                                                   |

Use `git mv` for every move so history is preserved.

Week 10 is new. Create `Week10/Week10-portfolio-project.ipynb`. It pulls the
course together into one assessed artefact: a program that uses classes, stores
data in SQLite, validates input, handles errors, and is committed to the
student's own GitHub portfolio repository. `Portfolio_Guidance.ipynb` already
describes the portfolio itself, so Week 10 should reference it rather than
repeat it.

Give the Week 10 project a Core specification and a Fast Track specification
following the pattern in Phase 3.

Then update `README.md` so the programme of study maps onto the weeks that
actually exist. Note in particular that version control is taught in Week 1,
not late in the course as the current README ordering implies. Teaching it
first is correct, because students need it to submit work. The README is what is
wrong, not the delivery.

**Commit message for Phase 2:**
`refactor: split overloaded Week 7 into Weeks 7 to 10 and align README`

---

## Phase 3: add the Fast Track lane to Weeks 1 to 6

This is the substance of the change. Do not skip the design rules.

### The block to insert

In each of `Week1` through `Week6`, in the main intro notebook for that week,
insert two new markdown cells immediately after the Lesson Objectives cell and
before the Concepts cell.

**Cell A, the placement check.** Titled `### Already done GCSE Computer Science?
Start here`. Three to five short questions on this week's topic that a GCSE
leaver should be able to answer in under five minutes without running code.
Include the answers in a collapsed HTML `<details>` block so students self-mark.
End with a single clear instruction: get them all right, go to Fast Track; miss
any, stay with Core and rejoin Fast Track next week.

**Cell B, the Fast Track tasks.** Titled `### Fast Track challenges`. Three to
four tasks on the same topic as the Core challenges but demanding more. State
plainly at the top that Fast Track students skip the Core challenge list and do
these instead, and that both lanes present in the same plenary.

Do not delete or weaken any existing Core content. Core stays exactly as it is.

### What goes in Fast Track each week

**Week 1, Introduction to Python.** GCSE students know variables, input and
output. Push them to: rewrite each Core tool as a function with a docstring,
f-string formatting, type hints, and a translation task converting AQA
pseudocode from a past paper into working Python.

**Week 2, Control structures.** They know selection and iteration. Push them to:
loop-and-a-half patterns, nested loops, choosing `while` against `for` with
written justification, and implementing linear search and binary search in code
rather than tracing them on paper as they did at GCSE.

**Week 3, Modules.** Push them to: write their own module in a `.py` file and
import it, use `if __name__ == "__main__"`, seed `random` for reproducible
testing, and use `datetime` rather than only `time`.

**Week 4, Data structures.** This is the widest gap in the course. AQA GCSE
covers lists and records but not dictionaries or sets. Fast Track goes deep on
dictionaries, sets, nested structures, list comprehensions, and a task requiring
students to choose a structure and justify the choice in writing.

**Week 5, Validation and error handling.** The gap narrows sharply here.
Exception handling is not on the GCSE specification, so this is new to nearly
everyone. Keep Fast Track light: custom exception classes, `finally`, and when
to validate with a loop rather than catch an exception. Say in the notebook that
most students should stay in Core this week. That is by design, not a gap in the
materials.

**Week 6, File handling.** GCSE covers basic read and write. Fast Track moves to
the `csv` and `json` modules, the `with` statement, and a task that reads a data
file, processes it, and writes a summary file.

From Week 7 the lanes merge. OOP, persistence and databases are new ground for
both groups. State this explicitly at the top of `Week7/week7-python-intro.ipynb`
so students understand the lanes were temporary by design and nobody has been
permanently labelled.

### Style rules

Match the existing house style in the repository: markdown cells with `###` and
`####` headings, emoji used sparingly in headings as the Week 7 notebooks
already do, British spelling, and challenges numbered in a plain list. Do not
introduce a new visual style, a colour scheme, or badge images.

**Commit message for Phase 3:**
`feat: add Fast Track lane and placement checks to Weeks 1 to 6`

---

## Phase 4: documentation

Create `SCHEME_OF_WORK.md` at the repository root. It is for the teacher and for
departmental records, not for students. It contains:

- The ten programme topics mapped to the ten weeks.
- A table with a row per week and columns for topic, Core outcome, Fast Track
  outcome, and prior GCSE coverage.
- A short section defining Core and Fast Track, stating that lanes are decided
  weekly and never used as fixed sets, and recording that both lanes converge at
  Week 7.
- A note that the lane names are defined here and used consistently across all
  notebooks, so renaming them is a single find and replace.

Keep it plain. No colour, no branding, black and white throughout.

**Commit message for Phase 4:**
`docs: add scheme of work mapping both lanes across ten weeks`

---

## Known sequencing defect, fix in Phase 3

`Week1/Week1-Python-intro.ipynb` sets two challenges that require functions:
"Task 2: Enhanced Calculator with Functions" and "Task 3: String Manipulation
with functions". Functions are not taught until Week 3, and Week 3 presents them
as a recap, implying they were covered earlier. They were not.

A true beginner hits this in the first lesson.

Recommended fix: move both tasks into the Week 3 challenge set, where functions
are actually taught, and replace them in Week 1 with equivalent tasks that use
only sequence, input and output. The Fast Track block added to Week 1 already
asks confident students to write functions, so the stretch is preserved without
stranding beginners.

Alternative, if Mr Ssemwanga prefers: add a short functions primer to Week 1 and
retitle Week 3 to "Modules" only. This conflicts with the README, which pairs
functions with modules as topic 3, so the README would need amending too.

Do not choose between these. Ask.

---

## Acceptance criteria

Before opening the pull request, verify all of the following:

1. `git status` is clean and every rename was recorded by git as a rename.
2. Every notebook still opens. Run `python -m json.tool` over each `.ipynb` and
   confirm valid JSON, or open them in VS Code.
3. No file in the repository references `week4`, `week5`, `itro`, `initiasGen`,
   `Resources.ipynb`, `testFiles`, or `Portfolio_Setup_`.
4. `git ls-files | grep solutions` returns nothing.
5. `git check-ignore -v solutions/week1_solutions.ipynb` confirms the rule now
   matches.
6. `git ls-files | grep students.db` returns `Week9/students.db` and nothing else.
7. Weeks 1 to 6 each contain a placement check cell and a Fast Track cell.
8. `README.md` and `SCHEME_OF_WORK.md` agree with each other and with the
   folders on disk.
9. Nothing has been force pushed and no history has been rewritten.

## Open questions to raise before finishing

1. Solutions in public history: accept, or rewrite and break student forks?
2. Week 1 functions defect: move the tasks, or add a Week 1 primer?
3. Are students already working in clones of this repository? If so the folder
   renames need a written instruction to hand out, and a chosen date to land.
