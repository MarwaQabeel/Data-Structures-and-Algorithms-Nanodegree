## Explanation of Problem 5: Blockchain


**Design Decisions:**
I used hashlib to calculate the hash for all data, and datetime to calculate the current GMT.
There’s an if statement at the beginning of BlockChain.add_block to set the previous hash of
the first block added to 0. In all other cases, the block to be added retrieves the previous
block’s hash, which links them together.


**Time Complexity:**
`O(1)` since all we’re doing is adding blocks with statements.


**Space Complexity:**
`O(n)` since I need to store all blocks in a blockchain list.

