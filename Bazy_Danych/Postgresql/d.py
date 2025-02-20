import math

class BuddyAllocator:
    def __init__(self, memory_size, max_splits):
        self.memory_size = memory_size
        self.max_splits = max_splits
        self.min_block_size = memory_size // (2 ** max_splits)  
        self.free_blocks = {memory_size: [0]}  


    def alloc(self, size):
        block_size = 2 ** math.ceil(math.log2(size)) 
        
        if block_size > self.memory_size or block_size < self.min_block_size:
            return None

        for size in sorted(self.free_blocks.keys()):
            if size >= block_size and self.free_blocks[size]:
                address = self.free_blocks[size].pop(0) 

                while size > block_size and size > self.min_block_size:
                    size //= 2
                    buddy_address = address + size
                    self.free_blocks.setdefault(size, []).append(buddy_address)

                return address, block_size

        return None 


    def free(self, address, size):
        buddy_address = address ^ size # XOR
        if buddy_address in self.free_blocks.get(size, []):
            self.free_blocks[size].remove(buddy_address)
            new_address = min(address, buddy_address)
            new_size = size * 2
            self.free(new_address, new_size) 
        else:
            self.free_blocks.setdefault(size, []).append(address)


    def display_memory_map(self):
        print("Mapa pamięci:")
        for size in sorted(self.free_blocks.keys(), reverse=True):
            print(f"  Size {size}: {self.free_blocks[size]}")



if __name__ == "__main__":
    allocator = BuddyAllocator(1024,5)
    
    allocator.display_memory_map()

    print("\nAlokacja 200 bajtów:")
    alloc_1 = allocator.alloc(55)
    print(f"Przydzielono: {alloc_1}")
    allocator.display_memory_map()

    print("\nAlokacja 30bajtów:")
    alloc_2 = allocator.alloc(55)
    print(f"Przydzielono: {alloc_2}")
    allocator.display_memory_map()

    # print("\nZwolnienie bloku 200 bajtów:")
    # if alloc_1:
    #     allocator.free(alloc_1[0], alloc_1[1])
    # print(f"Zwolniono blok: {alloc_1}")
    # allocator.display_memory_map()

    # print("\nZwolnienie bloku 30 bajtów")
    # if alloc_2:
    #     allocator.free(alloc_2[0], alloc_2[1])
    # print(f"Zwolniono blok: {alloc_2}")
    # allocator.display_memory_map()

    # print("\nAlokacja 1024 bajtów: ")
    # alloc_3 = allocator.alloc(1024)
    # print(f"Przydzielono: {alloc_3}")
    # allocator.display_memory_map()

    print("\nZwolnienie bloku 1024 bajtów")
  
    allocator.free(0, 1024)
    allocator.display_memory_map()