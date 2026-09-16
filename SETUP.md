# Setting Up Python and Jupyter Notebooks in VS Code

Read this before your first lesson. It is a plain text guide on purpose, because you cannot open a notebook until the software below is working.

Work through it in order. Each step has a "you should see" line. If you do not see it, stop at that step and ask rather than carrying on.

---

## Why we are not using github.dev

github.dev opens the repository in a browser and lets you read and edit files, which is useful. It cannot run Python. There is no kernel behind it, so every code cell in a notebook will sit there and do nothing.

Use github.dev to read and to make quick text edits. Use VS Code on the machine in front of you to actually run code.

---

## Step 1: Check whether Python is already installed

Open a terminal.

- On the school Windows machines, press the Windows key, type `cmd`, press Enter.
- At home on a Mac, press Cmd and Space, type `terminal`, press Enter.

Type this and press Enter:

```
python --version
```

**You should see:** something like `Python 3.12.4`. Any version from 3.10 upwards is fine.

**If you see** `Python was not found` or `command not found`, go to Step 2. Otherwise skip to Step 3.

On a Mac you may need `python3 --version` instead.

---

## Step 2: Install Python, only if Step 1 failed

On a school machine you probably cannot run an installer that asks for an administrator password. Use the Microsoft Store version, which does not need one.

1. Open the Microsoft Store.
2. Search for `Python 3.12`.
3. Click Get.

At home, on Windows or Mac, download from python.org instead. On the Windows installer, tick **Add python.exe to PATH** on the first screen before clicking Install. This is the single most common thing people miss and it causes most of the problems later.

Close the terminal, open a new one, and run `python --version` again.

**You should see:** a version number.

---

## Step 3: Install VS Code

The school machines already have it. Press the Windows key and type `Visual Studio Code`.

At home, download it from `code.visualstudio.com` and install it.

**You should see:** VS Code opens to a Welcome tab.

---

## Step 4: Install the two extensions

In VS Code, click the Extensions icon in the left bar. It looks like four small squares, one detached. The keyboard shortcut is Ctrl and Shift and X together, or Cmd and Shift and X on a Mac.

Search for and install these two, in this order:

1. **Python**, published by Microsoft
2. **Jupyter**, published by Microsoft

Check the publisher says Microsoft. There are imitations.

**You should see:** both extensions showing a gear icon instead of a blue Install button.

---

## Step 5: Get the course files onto your machine

You have two ways of doing this. Ask which one we are using before you start.

### Option A, with Git

In your terminal, move to where you want the folder to live, then:

```
git clone https://github.com/f-ssemwanga/Python-Award-Option.git
```

**You should see:** a few lines ending in `done.`, and a new folder called `Python-Award-Option`.

### Option B, without Git

1. Go to the repository page in your browser.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Find the ZIP in your Downloads folder, right click, Extract All.

Do not work inside the ZIP file itself. Windows will let you open files from inside it and will then silently throw away everything you save.

---

## Step 6: Open the folder in VS Code

In VS Code, File, then Open Folder. Select the `Python-Award-Option` folder.

Open the folder itself, not a single file. VS Code behaves differently when it has a folder open and several things later in this guide depend on it.

**You should see:** the folder name at the top of the left hand panel, with `Week1`, `Week2` and the rest underneath.

If a message appears asking whether you trust the authors, click Yes.

---

## Step 7: Open a notebook and choose a kernel

Click `Week1`, then `Week1-Python-intro.ipynb`.

Look at the **top right** of the notebook. There is a button that says `Select Kernel`.

1. Click it.
2. Choose **Python Environments**.
3. Choose the Python version you saw in Step 1.

**You should see:** the button change from `Select Kernel` to something like `Python 3.12.4`.

This is the step people get stuck on. The kernel is the Python that runs your code. Without one selected, cells do nothing and there is no error message to tell you why.

---

## Step 8: Run your first cell

Click on any grey code cell. Press **Shift and Enter** together.

**You should see:** a spinner briefly, then output appearing directly underneath the cell, and a number in square brackets to its left like `[1]`.

If a box appears at the top of the window asking you to install `ipykernel`, click Install and wait. This happens once per machine.

---

## Step 9: Install the two libraries we use later

From Week 6 onwards some notebooks need pandas and matplotlib. Install them now so it is done.

In the terminal:

```
pip install pandas matplotlib
```

On a Mac use `pip3` instead of `pip`.

**You should see:** a list of packages downloading, ending in `Successfully installed`.

Check it worked. In a notebook code cell, run:

```python
import pandas
import matplotlib
print("Both libraries loaded")
```

**You should see:** `Both libraries loaded`.

---

## When something goes wrong

**Cells do nothing and produce no output.** No kernel is selected. Go back to Step 7.

**`ModuleNotFoundError: No module named 'pandas'`.** The kernel you selected is a different Python from the one `pip` installed into. Fix it from inside the notebook instead, in a code cell:

```python
%pip install pandas matplotlib
```

The percent sign matters. It installs into the kernel the notebook is actually using.

**`'python' is not recognised as an internal or external command`.** Python is installed but not on PATH. Reinstall using the Microsoft Store version from Step 2.

**`'git' is not recognised`.** Git is not installed. Use Option B in Step 5 instead.

**The notebook opens as a wall of code and curly brackets.** VS Code has opened the raw file rather than the notebook. Close it, right click the file, Open With, Jupyter Notebook.

**Your work has vanished after restarting.** Output disappears when the kernel restarts, which is normal. Your code does not. Press Ctrl and S to save often. If the code has gone too, you were working inside the ZIP file. Go back to Step 5.

---

## Saving your work

Press Ctrl and S, or Cmd and S on a Mac, regularly.

Notebooks save both your code and its output. That means a saved notebook shows your results to anyone who opens it, which is exactly what we want for your portfolio.
