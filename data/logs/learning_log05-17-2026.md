# Python Learning Log | 05-17-2026


## Topic/Goal
* Complete functionality for `edit_learning_log` method
* Add a new feature for users when viewing saved learning logs


## What I Practiced/Built
* Refactored `learning_log_generator.py`:
  * Condense menu display into 5 options by categorizing both view & edit options together
    * This created the need to refactor `if-elif` conditional within the method orchestrator by corresponding menu 
      option choice with menu display
* Add features to `learning_log_generator.py`:
  * As a result of condensing the learning log menu display, there was a need for a new method to be defined for the 
    purpose of asking the user after viewing their list of saved files, if they want to edit a specific saved file. 
    Based on the  user's yes or no choice, their response is returned, and if "yes", then another method is used to get
    the user's learning log choice (entered integer), index their choice according to the interpreter, and finally 
    returned 

## Key Takeaways
* I had to remember how to use a counter variable in Python
* Re-learn how to index user input with Python's interpreter  

## Next Step
* Add feature to `edit_learning_log` method to allow user to edit the selected file they chose to edit by either:
  1. Opening the file through the IDE `pycharm learning_log5-..-2026.md`
  2. Or, open the file to edit another way...