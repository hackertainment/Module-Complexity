class LruCache:
    def __init__(self, limit):
        if limit<=0:
            raise ValueError("limit must be positive")
        else:
            self.limit = limit
            self.pairs = {}  # FIFO cache

    def __str__(self):
        return str(self.limit)+str(self.pairs)+"<"
    
    def get(self, key):
        if (key in self.pairs):  # if cache hit
            value = self.pairs.pop(key)
            self.pairs[key] = value
        else:
            value = None
        return value

    def set(self, key, value):
        if (key in self.pairs):  # if cache hit
            self.pairs.pop(key)
        elif (len(self.pairs)==self.limit):  # if cache miss but cache full
            self.pairs.pop(next(iter(self.pairs)))
        self.pairs[key] = value


if __name__ == "__main__":
    print(LruCache(1))
