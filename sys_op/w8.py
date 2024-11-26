# SLAB
class Slab:
    def __init__(self, object_size, obj_per_slab=10):
        self.slabs=[]
        self.object_size=object_size
        self.obj_per_slab=obj_per_slab
        self._internal_alloc()
    def _internal_alloc(self):
        slab={
            "memory": bytearray(self.object_size * self.obj_per_slab),
            "available": set(range(self.obj_per_slab)) # {0,1,2,3,4,5,6,7,8,9}
        }
        self.slabs.append(slab)


    def alloc(self):
        for slab in self.slabs:
            if slab['available']: 
                index=slab["available"].pop()
                return (slab,index)
        self._internal_alloc()
        return self.alloc()
    

    def free(self,slab,index):
        slab["available"].add(index)
        for slab in self.slabs:
            if slab['available']: 
                index=slab["available"].pop()
                return (slab,index)
            


struct_size=100
allocator=Slab(struct_size)
slab, index =allocator.alloc()
allocator.free(slab,index)