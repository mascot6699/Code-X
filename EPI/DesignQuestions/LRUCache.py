import collections
from queue import Queue

class LRUCache:

    def __init__(self, capacity, read_time, write_time):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.read_time = read_time
        self.write_time = write_time

    def lookup(self, key, value):
        if key in self.cache and self.cache[key] == value:
            return True
        return False

    def read(self, key):
        if key in self.cache:
            return self.cache.get(key)
        return False

    def write(self, key, value):
        # check capacity
        if self.capacity == len(self.cache):
            self.cache.popitem(last=False)
        self.cache[key] = value

    def filled(self):
        return len(self.cache)

class LevelCache:

    def __init__(self, level, cache_arr, no_of_ops_to_track=10):
        self.level = level
        self.caches = cache_arr #.extend([None] * (self.level - len(cache_arr)))
        self.last_read = Queue(no_of_ops_to_track)
        self.last_write = Queue(no_of_ops_to_track)

    def write(self, key, value):
        # return write time
        # print(key, value, cache.lookup(key, value))
        write_time = 0
        level_found_on = None
        for level, cache in enumerate(self.caches):
            if not level_found_on:
                myvalue = cache.read(key)
                write_time += cache.read_time
                if myvalue:
                    level_found_on = level + 1
            if not cache.lookup(key, value):
                cache.write(key, value)
                write_time += cache.write_time
            else:
                #write_time += cache.read_time
                break
        #print("level {}".format(level_found_on))

        self.add_write_time(write_time)
        return write_time

    def read(self, key):
        # return read time
        read_time = 0
        level, value = 0, 0
        for level, cache in enumerate(self.caches):
            value = cache.read(key)
            read_time += cache.read_time
            if value:
                for cache in self.caches[:level]:
                    cache.write(key, value)
                    read_time += cache.write_time
                self.add_read_time(read_time)
                return read_time
        return 0

    def stats(self):
        for cache in self.caches:
            print("Usage: {}/{}".format(cache.filled(), cache.capacity))
        #print("Avg Read Time: {}".format(avg(self.last_read)))

    def add_write_time(self, time):
        if not self.last_write.full():
            self.last_write.put(time)
        else:
            self.last_write.get()
            self.last_write.put(time)

    def add_read_time(self, time):
        if not self.last_read.full():
            self.last_read.put(time)
        else:
            self.last_read.get()
            self.last_read.put(time)

def main():
    level = int(input())
    capacity = [int(x) for x in input().split()]
    read_time = [int(x) for x in input().split()]
    write_time = [int(x) for x in input().split()]
    cache_arr = []
    for i in range(level):
        c = LRUCache(capacity[i], read_time[i], write_time[i])
        cache_arr.append(c)
    my_cache = LevelCache(level, cache_arr)
    count = 10
    while(count):
        command, *str1 = input().split()
        if command == "WRITE":
            print(my_cache.write(str1[0], str1[1]))
        elif command == "READ":
            print(my_cache.read(str1[0]))
        count -=1
    print(my_cache.stats())

if __name__ == '__main__':
    main()
