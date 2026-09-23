# Setting Up Python and Notebooks

Read this before your first lesson. It is a plain text guide on purpose, because you cannot open a notebook until the software below is working.

We write and run the notebooks in **VS Code**. On the school machines VS Code cannot run Python notebooks by itself, so you start a small Jupyter server first and connect VS Code to it. It takes two minutes once you have done it once.

| Part | What | When |
| --- | --- | --- |
| 1 | Python and the packages | Once per machine |
| 2 | Your copy of the course files | Once per machine |
| 3 | VS Code on a school machine | Every lesson, Steps 3.3 and 3.4 |
| 4 | VS Code at home | Once |
| 5 | JupyterLab in the browser | Only if VS Code will not work |

---

## Part 1: Python

### Step 1.1 Check whether Python is already installed

Open a terminal. On Windows press the Windows key, type `cmd`, press Enter. On a Mac press Cmd and Space, type `terminal`, press Enter.

Type this and press Enter:

```
python --version
```

**You should see:** something like `Python 3.13.7`. Any version from 3.10 upwards is fine.

**If you see** `Python was not found` or `command not found`, go to Step 1.2. Otherwise skip to Part 2.

On a Mac use `python3` instead of `python` everywhere in this guide.

### Step 1.2 Install Python, only if Step 1.1 failed

On a school machine you probably cannot run an installer that asks for an administrator password. Use the Microsoft Store version, which does not need one. Open the Microsoft Store, search for `Python 3.13`, click Get.

At home, download from python.org instead. On the Windows installer, tick **Add python.exe to PATH** on the first screen before clicking Install. Missing that tick causes most of the problems people hit later.

Close the terminal, open a new one, and run `python --version` again.

### Step 1.3 Install the packages the course needs

```
python -m pip install --user jupyterlab pandas matplotlib
```

**You should see:** a lot of downloading, ending in `Successfully installed`.

Two details here matter and both are deliberate.

**`python -m pip`, not plain `pip`.** On a machine with more than one Python, and most school machines have more than one, bare `pip` often belongs to a different Python from the one `python` runs. Going through `python -m` guarantees they match.

**`--user`.** If Python was installed for all users, it lives in `C:\Program Files`, and writing packages there needs administrator rights you will not have. `--user` puts them in your own profile instead.

---

## Part 2: Getting the course files

### With a GitHub account (the normal way)

You fork the course on GitHub, then clone your fork into VS Code. Your work then syncs to GitHub every lesson and follows you from machine to machine.

The steps are in **`Week1/usingGitHub.ipynb`**. It is all text, so you can open and read it in VS Code before anything else is working. Open the course on GitHub in your browser, click `Week1`, then `usingGitHub.ipynb`, and follow Parts 1 to 5.

### Without a GitHub account

Only if your teacher tells you to. Your work stays on this one machine and does not sync anywhere.

```
git clone https://github.com/f-ssemwanga/Python-Award-Option.git
```

**You should see:** a few lines ending in `done.`, and a new folder called `Python-Award-Option`.

If Git is not installed, go to the repository page, click the green **Code** button, then **Download ZIP**. Find the ZIP in Downloads, right click, Extract All. Do not work inside the ZIP file itself. Windows will let you open files from inside it and then silently throw away everything you save.

---

## Part 3: VS Code on a school machine

The school's VS Code is an older version that the school manages, and the newest Jupyter extension will not run on it. So you do two things differently from the guides online: you install an older Jupyter extension that matches, and you run Python in a Jupyter server that you start yourself.

### Step 3.1 Install the matching Jupyter extension (once)

1. Click the **Extensions** icon in the left bar, or press Ctrl, Shift and X.
2. Search for **Jupyter**, published by **Microsoft**. Check the publisher. There are imitations.
3. Click the small arrow next to **Install**, or the gear icon if it is already installed, and choose **Install Specific Version...**
4. Pick the version your teacher has given you.
5. If a **Reload** or **Restart Extensions** button appears, click it.

**You should see:** the Jupyter extension with a gear icon and no warning triangle.

Installing a specific version also stops VS Code updating that extension by itself, which is what you want. An automatic update would put back the version that does not work here.

### Step 3.2 Open the course folder and trust it (once)

**File**, then **Open Folder**, and choose the `Python-Award-Option` folder. Open the folder, not a single notebook.

Look at the bottom left of the window, on the blue bar. If there is a badge reading **Restricted Mode**, click it and choose **Trust**. Until you trust the folder, VS Code switches the Jupyter extension off, and you get no error message, just a kernel list with nothing in it.

### Step 3.3 Start the Jupyter server (every lesson)

1. Open **Thonny**.
2. **File**, **Open**, and open `start_jupyter.py` from the course folder.
3. Press **Run**. The first time, it installs what it needs, which takes a minute or two.
4. A browser tab with JupyterLab opens. You can close the tab. **Do not stop Thonny.** The server runs inside it, and stopping it stops your code running in VS Code.
5. In Thonny's shell at the bottom, find the line that starts `http://localhost:8888/lab?token=` followed by a long string of letters and numbers. Select the whole line and copy it.

**You should see:** Thonny still running, with that line in its shell. The token is different every time the server starts.

### Step 3.4 Connect VS Code to the server (every lesson)

1. In VS Code, open a notebook, for example `Week1/Week1-Python-intro.ipynb`.
2. Top right, click **Select Kernel**. If it already shows a kernel, click that instead.
3. Choose **Existing Jupyter Server...** You may need to choose **Select Another Kernel...** first to see it.
4. Paste the line you copied from Thonny and press Enter.
5. If it asks for a display name, press Enter to accept the suggestion.
6. Choose **Python 3 (ipykernel)**.

**You should see:** the button at the top right showing **Python 3 (ipykernel)**.

**Next lesson** VS Code offers last lesson's server in the list. It will not work, because the token has changed. Choose **Existing Jupyter Server...** again and paste the new line.

### Step 3.5 Run a cell

Click a code cell and press **Shift and Enter**.

**You should see:** output directly underneath the cell, and a number in square brackets to its left like `[1]`.

### Stopping

Save with Ctrl and S, commit and sync your work, then press **Stop** in Thonny.

---

## Part 4: VS Code at home

At home your VS Code is up to date, so it is simpler. No server, no Thonny.

1. **Help**, then **About**. If the version is more than about six months old, update VS Code first.
2. In Extensions, install **Python** and **Jupyter**, both published by Microsoft, the normal way.
3. Open the course folder and trust it, as in Step 3.2.
4. Open a notebook, click **Select Kernel**, then **Python Environments**, then your Python version.

**You should see:** the button change to something like `Python 3.13.7`.

**If the list is empty**, VS Code has not found Python. In a terminal type `where python` on Windows, or `which python3` on a Mac, and copy the path. Then in VS Code press Ctrl, Shift and P, type `Python: Select Interpreter`, choose **Enter interpreter path...**, and paste it.

If a box asks you to install `ipykernel`, click Install and wait. This happens once per machine.

---

## Part 5: JupyterLab in the browser (the fallback)

If VS Code will not connect, you can still do the lesson. Run `start_jupyter.py` in Thonny as in Step 3.3, and work in the JupyterLab tab that opens in the browser instead of closing it. Everything in the notebooks works the same way.

At home you can also double-click **`start-jupyter.bat`**. School networks block batch files, so it only works on your own machine.

If neither works, open a terminal, move into the course folder, and run:

```
python -m jupyter lab
```

Note the `python -m` at the front. Plain `jupyter lab` usually fails, because `--user` installs put the command line scripts somewhere that is not on your PATH.

---

## Why not github.dev

github.dev opens the repository in a browser and lets you read and edit files, which is useful. It cannot run Python. There is no kernel behind it, so every code cell will sit there and do nothing.

Use github.dev to read and make quick text edits. Use VS Code on the machine in front of you to actually run code.

---

## When something goes wrong

**Cells do nothing and produce no output.** No kernel is selected, or the folder is untrusted. Steps 3.2 and 3.4.

**A cell spins forever, or VS Code says it cannot connect to the server.** The Jupyter server has stopped, usually because Thonny was stopped or closed. Run `start_jupyter.py` again, then redo Step 3.4 with the new line.

**The Jupyter extension shows a warning and will not activate.** It has updated itself to a version the school's VS Code cannot run. Redo Step 3.1.

**`ModuleNotFoundError: No module named 'pandas'`.** The kernel is a different Python from the one you installed into. Fix it from inside the notebook, in a code cell:

```python
%pip install pandas matplotlib
```

The percent sign matters. It installs into the kernel the notebook is actually using.

**`'python' is not recognised`.** Python is installed but not on PATH. Use the Microsoft Store version from Step 1.2.

**`'jupyter' is not recognised`.** Use `python -m jupyter lab` instead of `jupyter lab`.

**`WinError 1260: This program is blocked by group policy`.** The school blocks programs from running out of your user profile, and that is where `jupyter-lab.exe` gets installed. Start it as a module instead, which stays inside `python.exe`:

```
python -m jupyterlab
```

`start_jupyter.py` already does this for you, which is why it is the recommended route on school machines.

**Access denied, or a permissions error, when installing a package.** You left off `--user`. Add it.

**`'git' is not recognised`.** Git is not installed. Tell your teacher. You can still read the notebooks, but your work will not sync until Git is available.

**The notebook opens as a wall of code and curly brackets.** VS Code has opened the raw file rather than the notebook. Close it, right click the file, Open With, Jupyter Notebook.

**Your work has vanished after restarting.** Output disappears when the kernel restarts, which is normal. Your code does not. If the code has gone too, you were working inside the ZIP file. Go back to Part 2.

---

## Saving your work

Press Ctrl and S, or Cmd and S on a Mac, regularly.

Notebooks save both your code and its output. A saved notebook shows your results to anyone who opens it, which is exactly what we want for your portfolio.
