class ExtendedHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def simple_hash(self, key):
        # Converts the last 3 digits of the product ID to an integer and maps it to the table size
        return int(key[-3:]) % self.size

    def insert(self, key, value):
        hash_index = self.simple_hash(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = [(key, value)]
        else:
            # Replace existing value if key exists, else append new key-value pair
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
            if bucket is not None:
                print(f"Index: {i}, Entries: {bucket}")
            else:
                print(f"Index: {i}, Entries: None")
        print("\n")

# Initialize ExtendedHashTable
extended_hash_table = ExtendedHashTable()

# Insert product data and print state after each insertion
product_data = {
    "P1001": "Laptop",
    "P1002": "Smartphone",
    "P1003": "Tablet",
    "P1004": "Monitor",
    "P1005": "Keyboard",
    "P1006": "Mouse",
    "P1007": "Webcam",
    "P1008": "Headset",
    "P1009": "Microphone",
    "P1010": "Printer",
    # Additional product data for new scenarios
    "P1011": "Charger",  # Will have the same index as one of the previous entries
    "P1021": "External Hard Drive"  # Will also result in a collision
}

# Print initial state
print("Initial State of Hash Table:")
extended_hash_table.print_table_state()

# Insert each product and print the table state
for key, value in product_data.items():
    print(f"Inserting {key}: {value}")
    extended_hash_table.insert(key, value)

# Demonstrate search operation and how it improves search time
search_key = "P1005"
print(f"Searching for {search_key}...")
search_result = extended_hash_table.get(search_key)
print(f"Search Result: {search_result}")
