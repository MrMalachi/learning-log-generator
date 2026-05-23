# Python Learning Log | 05-23-2026


## Topic/Goal
* Re-learn Python Classes for O.O.P.
* After strengthening my understanding of Classes:
  * Continue working on GUI for Learning Log Generator by using `tkinter` framework

## What I Practiced/Built
* Learning the difference between instance variables & class variables

## Key Takeaways
* Instance Variables:
  * Unique for each individual instance (object) of a Class
* Class Variables:
  * The same for each instance because they are shared across every single project created from that Class
  * When accessing Class variables, they must be accessed through an instance variable OR the Class itself
    * Using a class variable within the initializer (constructor) method can be used when needing to track the total 
      number of employees everytime a new instance of the Class is created, for example:
      * ```python
        class Employee:
            num_of_emps = 0
            raise_amount = 1.04

            def __init__(self, first, last, pay):
              self.first = first
              self.last = last
              self.pay = pay
              self.email = f"{first}.{last}@company.com"
    
              Employee.num_of_emps += 1
        ```

## Next Step
