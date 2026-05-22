# Python Learning Log | 05-21-2026


## Topic/Goal
* Create a sharable executable `.exe` / `.app`
* Turn Learning Log Generator script into a GUI desktop app by learning and
  using `argparse`

## What I Practiced/Built
* I turned my Learning Log Generator script into an executable file: 
  * I did so to create a `.command` file, which contains a series of terminal commands within it, rather than having to
    run those terminal commands myself
* Created a new function within `config.py` file so that it acts as a helper function

## Key Takeaways
* Being able to turn my script into a double-click file was easier than I though because all I had to do was:
  1. Create a `.command` file and name it whatever I wanted - `LearningLogGenerator.command`
  2. Within the `.command` file, write the following code:
     3. ```.commandline
        #!/bin/zsh 

        cd "$(dirname "$0")"
        ./learning-log-generator
        ```
        * This basically runs the file using zsh shell, move the Terminal into the folder where the 
          `LearningLogGenerator.command` file loves, and run the file `learning-log-generator` from the current folder
          which is `dist/learning-log-generator`... "Go to the folder where the launcher is, then run the executable in 
          that folder"
* The `resource_path` function contains a conditional that looks at my system to see if it is running inside a bundled
  PyInstaller executable (`.exe`) file
  * If yes, the files are trapped inside a hidden, temporary folder created by PyInstaller, the function grabs the 
    secret path to that folder `sys._MEIPASS` and attaches the file's name `relative_path` to the end of it so that it
    returns this total hidden path so the program can successfully open the file
  * Otherwise, if no, the code is being run normally in the code editor and the function skips the hidden folder logic
    entirely, and looks for the file right next to the code script using the original file name `relative_path`

## Next Step
* Use the standard built-in library `Tkinter`, to create a GUI by using the `learning_log_generator.py` script 