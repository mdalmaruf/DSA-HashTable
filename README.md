# Understanding Hash Tables and Hash Functions

Hash Tables are a crucial data structure in computer science, used for storing key-value pairs. They offer fast retrieval, insertion, and deletion operations. This blog post dives into the concept of Hash Tables, the mechanics of Hash Functions, and tackles various scenarios and considerations in their application.

## Introduction to Hash Tables

A Hash Table is a data structure that organizes data for quick access based on keys. It uses a hash function to compute an index into an array of slots, from which the desired value can be found.

## The Essence of Hash Functions

A Hash Function takes a key and computes an index in the array where the key-value pair resides. The efficiency of a hash table is highly dependent on the design of its hash function. A well-designed hash function should:
- Evenly distribute keys across the hash table to minimize collisions.
- Be quick to calculate.

### Example of a Simple Hash Function

```python
def simple_hash(self, key):
    return int(key[-3:]) % self.size
```
This function maps the last three digits of a product ID to a hash table size using modulo operation. The simple hash function can be implemented in different way. Another example?

```python
def ascii_hash(self, key):
    # Sum ASCII values of all characters in the key
    ascii_sum = sum(ord(char) for char in key)
    # Use modulo to fit the hash table size
    return ascii_sum % self.size
```
This hash function iterates through each character in the key, calculates its ASCII value using `ord()`, sums these values, and then applies modulo operation with the hash table size to ensure the result fits within the table bounds. It tends to distribute strings more uniformly across the table, especially when keys have varied lengths and characters.




## Collision Handling
Collisions occur when two keys hash to the same index. A popular strategy to manage collisions is chaining, where each index in the array points to a list of entries that hash to the same index.

## Implementing a Hash Table in Python
Here's how you can implement a basic hash table with chaining in Python:
```python
class ExtendedHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def simple_hash(self, key):
        return int(key[-3:]) % self.size

    def insert(self, key, value):
        hash_index = self.simple_hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[hash_index]):
                if k == key:
                    self.table[hash_index][i] = (key, value)
                    return
            self.table[hash_index].append((key, value))
        self.print_table_state()

    def get(self, key):
        hash_index = self.simple_hash(key)
        if self.table[hash_index] is not None:
            for k, v in self.table[hash_index]:
                if k == key:
                    return v
        return "Product not found"
    
    def print_table_state(self):
        print("Current State of Hash Table:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index: {i}, Entries: {bucket}")
            else:
                print(f"Index: {i}, Entries: None")
```
## Scenarios and Considerations
#### Scenario 1: Insertion and Search
When inserting a new key-value pair, if the hash index is already occupied, the new pair is appended to the list at that index, using chaining. This allows for efficient search operations, demonstrating the hash table's capability for fast data retrieval.

#### Considerations
-  Hash Function Design: A good hash function is essential for distributing keys evenly across the hash table.
-  Collision Handling: Proper management of collisions ensures efficient data retrieval.
-  Table Size and Resizing: The size of the hash table and its resizing strategy can significantly affect performance.

## Conclusion
Hash Tables, powered by efficient hash functions and effective collision handling strategies, are invaluable for creating fast and reliable applications that require quick access to data. Understanding their implementation and potential pitfalls is key to leveraging their full potential.
