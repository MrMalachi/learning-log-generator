# Python Learning Log | 05-19-2026


## Topic/Goal
* Create a platform-agnostic method that opens a newly created file and opens a file when wanting to edit a learning log 

## What I Practiced/Built
* I built a `open_learning_log` method using A.I. that uses intra-class method calling in two methods:
  * `create_learning_log`
  * `edit_learning_log`
    * The `open_learning_log method` itself basically uses imported modules such as, `Path`, `platform`, `os`, and 
      `subprocess`. The method uses an `if-elif-else` chain to basically run the default app associated with a `.md` 
      file

## Key Takeaways
* A.I. needed to be used because implementing this feature was beyond the scope of my understanding, so I made sure to 
  ask questions while prompting for an answer that would help me gain a better understanding of what the heck the agent
  just spit out
* Things I learned about the three newly imported modules: `os`, `platform`, and `subprocess`:
  * They are built-in libraries in the Python Standard Library
  * They are used to interact with the system hosting the Python script
    * I wanted the method to work on most people's computers because this Learning Log Generator project is available to 
      the public via GitHub public repository, therefore...
  * I learned the term "platform-agnostic"
  * Not all operating systems are able to handle files the same: macOS, Windows, Linux

## Next Step
* Create method(s) for deleting a learning log (file)