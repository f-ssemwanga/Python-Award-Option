# Python-Award-Option by Mr Ssemwanga

### Overview

A ten week Python course for sixth form students heading into STEM subjects at university. It is not an exam course. There are no exams, and students who complete it receive a certificate. Every lesson is about becoming a better programmer.

The course was first written for students who had not studied programming at GCSE. It now also takes students who have, so it runs in two lanes.

### Getting started

1. **`SETUP.md`**: install Python, and get VS Code running notebooks. Read this first.
2. **`Week1/usingGitHub.ipynb`**: fork the course, clone it into VS Code, and make your first commit.
3. **`Week1/Week1-Python-intro.ipynb`**: the first lesson, which opens with the placement check.

Each week has its own folder, `Week1` to `Week10`. Every notebook is written to be run in VS Code, cell by cell.

### The two lanes

| | Core | Fast Track |
| --- | --- | --- |
| For | Anyone meeting the week's topic for the first time | Anyone who already knows the week's basics, usually from GCSE Computer Science |
| Does | Learns the topic from the concepts, then the Core challenges | Skips the basics and goes straight to its own challenges, on material that is new to them |
| Decided by | The placement check at the top of each week's notebook | The same check |

**Lanes are decided fresh every week.** Scoring full marks on the Week 1 check puts you in Fast Track for Week 1 only. Plenty of students will be Fast Track one week and Core the next, because some topics are new to everybody. Nobody is on a fixed track.

Both lanes work in the same room on the same topic, and come together for the plenary at the end of each lesson.

Fast Track is **not** a harder version of the Core challenges. Repeating the basics at a higher difficulty teaches you nothing, so Fast Track does different work.

From Week 7 onwards the topics are new to everyone, so there is nothing to skip. Fast Track becomes an **additional data strand** instead, open to anybody who wants it.

### Weekly delivery

| Week | Topic | Core | Fast Track |
| --- | --- | --- | --- |
| 1 | Introduction to Python, Git and notebooks | Variables, `input`, arithmetic, f-strings | Functions written properly: type hints, docstrings, returning values, self-checking tests |
| 2 | Control structures | `if`, `elif`, `else`, `for`, `while` | Linear and binary search, counting the cost of each on bigger and bigger lists |
| 3 | Functions and modules | Defining functions, parameters, return values, `math` and `random` | Your own module in a `.py` file, `__name__ == "__main__"`, default arguments, testing with `assert` |
| 4 | Data structures | Lists, dictionaries, tuples | Nested structures, comprehensions, `Counter`, choosing the right structure and saying why |
| 5 | Validation and error handling | `try`, `except`, validation loops | Close to Core this week, since this is new to nearly everyone. Custom exceptions and `finally` |
| 6 | File handling | `open`, reading, writing, the `with` statement, CSV | `csv` and `json` modules, first `pandas` DataFrame, first chart |
| 7 | Object-oriented programming | Classes, attributes, methods, `__init__` | Additional strand: inheritance, `__str__` and `__repr__` |
| 8 | Persistence: from files to objects | Saving and loading objects with `pickle` | Additional strand: `json`, and why `pickle` is unsafe for files you did not make |
| 9 | Databases and Python | SQLite and SQL from Python | Additional strand: parameterised queries and SQL injection, joins, query results into a DataFrame |
| 10 | Portfolio project | A program using classes, a database, validation and error handling, on GitHub | The same, plus an analysis notebook: query, chart, and write up what the data shows |

Week 1 is fully written for both lanes. The Fast Track material for the later weeks is being written ahead of each lesson, and the table above is the plan it follows.

Git and GitHub are taught to everyone together in Week 1, because nobody can hand in any work without a repository. Git is new to both lanes, so there is no split for that part of the lesson.

### Programme of study

These are the course's topics, and the week each one is taught in.

- **Introduction to Python programming** (Week 1): a solid foundation in Python syntax and basic programming concepts.
- **Version control** (Week 1, used every week after): the basics of Git and GitHub, for collaborative development and an online repository to show your work.
- **Working with notebooks** (Week 1, used every week after): running code interactively, cell by cell. Notebooks are how the whole course is delivered rather than a topic of their own, and they are the standard tool for data work at university.
- **Control structures** (Week 2): loops and conditional statements to control the flow of a program.
- **Functions and modules** (Week 3): reusable, organised code.
- **Data structures** (Week 4): lists, dictionaries, sets and tuples for managing collections of data.
- **Validation and error handling** (Week 5): robust code that copes with bad input.
- **File handling** (Week 6): reading from and writing to files.
- **Object-oriented programming** (Weeks 7 and 8): classes and objects to model real-world things, and saving them between runs.
- **Python and databases** (Week 9): storing and retrieving data from Python.
- **Portfolio project** (Week 10): one program that draws the whole course together.

### The course dataset

Real Met Office weather records from five UK stations, some going back to 1853, sit in the `data` folder. The same data is used from Week 1 to the Week 10 project, so what you learn each week is used on something real rather than thrown away. `data/README.md` explains where it came from and what each column means.

### Also in this repository

- `Portfolio_Guidance.ipynb`: how to build and write up your GitHub portfolio.
- `start_jupyter.py`: starts the Jupyter server on a school machine. `SETUP.md`, Part 3, explains when to use it.

### Justification

This programme of study forms a strong foundation for students' programming skills post-18 for several reasons:

- **Comprehensive coverage**: the topics cover essential programming concepts and skills that are fundamental to any further study or career in computer science.
- **Practical skills**: file handling, database integration and version control are directly applicable in real-world work.
- **Problem-solving**: control structures, functions and error handling develop strong problem-solving habits.
- **Preparation for advanced topics**: object-oriented programming and data structures prepare students for what they will meet in university courses.
- **Working with real data**: running notebooks against a real dataset every week is how science and engineering departments actually use Python.
