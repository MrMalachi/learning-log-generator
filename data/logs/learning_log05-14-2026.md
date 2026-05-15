# Python Learning Log | 05-14-2026


## Topic/Goal
* Add functional modifications to `learning_log_generator.py` methods that affect both behaviors: 
  viewing saved learning logs and searching learning logs by keyword
  1. Modify output when displaying enumerated logs to exclude path and only 
     display file name with extension
  2. Create method to display matching logs based on returned keyword
     * Modify output when displaying matched logs to exclude path and only 
       display file name with extension

## What I Practiced/Built
* I built improvements to the following methods:
  * `create_learning_log` - the variable `new_file_path` now has a file path that contains an object instead of just a 
                            string by using Path joining with a '/'. Path objects and string paths are no longer being 
                            mixed
  * `display_saved_learning_logs` - instead of using `with open()` context manager, all that was needed to display saved 
                                    learning logs was a for loop to iterate over the files within the constant variable 
                                    containing the path of the directory, pointing to the files within. Finally, the 
                                    `.name()` pathlib attribute was assigned to the `file` variable to perform path 
                                    manipulation
  * `display_matching_logs` - in order to actually display the matching logs based on entered keyword(s), which were the 
                              files appended to the returned list, first I needed an `if` statement based on the 
                              condition that there are no `matching_logs` based on the returned keyword. Finally, a 
                              `for` loop was used with the `enumeration` function to display both the index and file(s)
                              names, along with the `.name()` attribute, for all matching logs containing keyword(s)

## Key Takeaways
* Displaying the file names neatly while excluding their path was simpler than I thought
* I needed more methods than I thought when including features for viewing and searching for saved logs

## Next Step
* Add functionality for editing a learning log