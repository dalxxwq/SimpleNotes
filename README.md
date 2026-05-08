# Week 8 Files Project

Small Python project for practicing file reading and writing.

## What It Does

This script works with a text file called `notes.txt`.

You can:

- add a new line of text to the file
- read everything already saved in the file
- exit the program

## Project Files

- `main.py` - main Python script
- `notes.txt` - text file where notes are stored
- `README.md` - project description and instructions

## How To Run

Open a terminal in this folder:

```powershell
cd E:\self-development\week8\week_8_files
python main.py
```

Then choose one of the commands:

```text
add
read
exit
```

## Example

```text
Wanna add some text or just read it? (add/read/exit): add
What should we write to the file? Today I practiced working with files.

Wanna add some text or just read it? (add/read/exit): read
Today I practiced working with files.
```

## What I Practiced

- opening files with `open()`
- writing text with append mode (`"a"`)
- reading text from a file
- using `with` so the file closes automatically
- using a `while True` loop for a simple menu
- using `break` to stop the program

## Next Improvements

- handle the case when `notes.txt` does not exist yet
- add a command to clear the file
- make command input more flexible
- improve messages so they use one language consistently
