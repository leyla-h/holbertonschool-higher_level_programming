 Extending the Python List with Notifications
Background:
In Python, you can extend built-in classes to add or modify behavior. The list class provides a collection of methods and functionalities that handle list operations. By extending the list class, you can provide custom behaviors while retaining the original functionalities.

Objective:
Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).

Instructions:
Setting up the VerboseList Class:
Define a class VerboseList that inherits from the built-in list class.
Within VerboseList, override the methods that modify the list: append, extend, remove, and pop.
Implementing Notifications:
For the append method: After adding the item to the list, print a message like "Added [item] to the list."
For the extend method: After extending the list, print a message like "Extended the list with [x] items." where [x] is the number of items added.
For the remove method: Before removing the item from the list, print a message like "Removed [item] from the list."
For the pop method: Before popping the item from the list, print a message like "Popped [item] from the list." If the index is not specified, default behavior is to pop the last item.
Testing:
Instantiate a VerboseList object.
Test all the overridden methods (append, extend, remove, and pop) and ensure that the appropriate messages are printed for each operation.
Hints:

Remember to call the original method of the list class using the super() function to ensure that the original functionality is retained. For example, for append: super().append(item).
Think about edge cases, such as trying to remove an item that doesn't exist in the list.
$ cat main_02_verboselist.py 
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

$ ./main_02_verboselist.py 
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: python-abc
File: task_02_verboselist.py
