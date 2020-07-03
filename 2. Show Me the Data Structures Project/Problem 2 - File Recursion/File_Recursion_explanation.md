## Explanation of Problem 2: File Recursion


**Design Decisions:**
I used recursion and concatenated each new valid file found to current path, then returned the
new files found and extended the current list of files with them. This accumulates the list of
valid files across sub-directories.


**Time Complexity:**
`O(mn)` because of the loop over all files includes number of sub-directories, `m`, and number of
files per directory, `n`.


**Space Complexity:**
`O(mn)` since in the worse case, we could have `n` files to hold, and `m` sub-directories to search.


