"""Example of implementing a cache class via dictionary"""


class Cache():
    def __init__(self):
        """Instantiate a Cache instance
        simple cache management with the following strategies:
        1. The percentage of cache to shrink when purged
        2. The max size threshold of cache to keep
        3. Keeping most-frequently-used items when purged

        Each key of the cache has a list as value, containing two elements:
        1. value object (any user-defined object)
        2. reference count (integer): to keep track of the number of access the key
        """
        self.cache = dict()

    def __repr__(self):
        """Dump the cache"""
        str_dump = f'Dump cache ({len(self.cache)}) items...\n'
        count = 1
        for key, value in self.cache.items():
            str_dump += f'{count}: Key: {key}\n'
            val_str = str(value[0])
            str_dump += f'===>val: ...{val_str[5:50]}...\n'
            str_dump += f'===>ref: {value[1]}\n'
            count += 1
        return str_dump

    def has(self, key):
        """Check if the key is in the cache"""
        if key in self.cache:
            return True
        return False

    def add(self, key, value):
        """Add a key-value pair to the cache"""
        self.cache[key] = [value, 1]

    def inc(self, key):
        """Increment the reference count of the specified key"""
        val_list = self.cache.pop(key)
        val_list[1] += 1
        self.cache.update({key: val_list})

    def get(self, key):
        """Get the value associated with the specified key"""
        return self.cache[key][0]

    def purge(self, size=100):
        """Purge all the least-used items to the specified size.
        And reset the refernece count for each remaining items."""
        if len(self.cache) <= size:
            # The cache already within the limit
            return

        s_li = sorted(self.cache.items(), key=lambda kv: (
            kv[1][1], kv[0]), reverse=True)

        # Clear the cache
        self.cache.clear()
        for i in range(size):
            # Load up the top percentage items into cache
            # key is the first element of 's_li' list
            # Reset the reference count that is at 2nd element of val-list,
            # which is the 2nd element of 's_li' list
            s_li[i][1][1] = 0
            self.cache[s_li[i][0]] = s_li[i][1]

    def shrink(self, percent=50):
        """Shrink the cache down to the specified percentage,
        but no reset the reference count at all."""
        s_li = sorted(self.cache.items(), key=lambda kv: (
            kv[1][1], kv[0]), reverse=True)
        count_keep = len(self.cache) * percent // 100 + 1

        # Clear the cache
        self.cache.clear()
        for i in range(count_keep):
            # Load up the top percentage items into cache
            self.cache[s_li[i][0]] = s_li[i][1]
