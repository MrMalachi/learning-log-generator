# Python Learning Log | 05-20-2026


## Topic/Goal
* Refactor methods within Learning Log Generator project
* Add confirmation before allowing user to delete a learning log

## What I Practiced/Built
* I added more error-handling where necessary within methods
* While refactoring, I built a new method that reads all the saved marked down files from the LOGS_FOLDER path using 
  .glob() method
* I built and re-built a method for confirming a user's choice by prompting them to confirm whether or not to delete the
  specified learning log
  * Rather than returning a string containing a user's input as 'y' or 'n', the method returns a boolean so that choice
    5, nested if-statement, within the orchestrator method reads more naturally
* Add various functionalities like:
  * Calling .lower() & .strip() methods on string objects
  * Include important parameters to methods and pass them as arguments within orchestrator methods 

## Key Takeaways
* I learned how to return boolean values and the importance of using them within methods in order to make method calls
  more readable
* I learned the importance of using the .glob() method (global) in python and passing the wildcard `*.md` as an argument
  in order to only look through Markdown files specifically, rather than using the .iterdir() method, which iterates 
  over all contents of a given directory
* Lastly, I learned from yesterday how to import third-party packages, how to properly follow PEP-8 Style Guide when 
  importing modules at the top of the `.py` file, and how to include the module `send2trash` within the 
  `delete_learning_log` method so that files are not permanently deleted

## Next Step
* Create a shareable executable `.exe` / `.app`
* Turn Learning Log Generator script into GUI desktop app by learning & using 
  `argparse`