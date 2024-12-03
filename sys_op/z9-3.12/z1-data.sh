#!/bin/bash

# generowanie plików random
dd if=/dev/urandom of=/tmp/data/random/1 bs=10M count=1
dd if=/dev/urandom of=/tmp/data/random/2 bs=10M count=1
dd if=/dev/urandom of=/tmp/data/random/3 bs=10M count=1
dd if=/dev/urandom of=/tmp/data/random/4 bs=10M count=1
dd if=/dev/urandom of=/tmp/data/random/5 bs=10M count=1

#generowanie plików empty
dd if=/dev/zero of=/tmp/data/empty/1 bs=10M count=1
dd if=/dev/zero of=/tmp/data/empty/2 bs=10M count=1
dd if=/dev/zero of=/tmp/data/empty/3 bs=10M count=1
dd if=/dev/zero of=/tmp/data/empty/4 bs=10M count=1
dd if=/dev/zero of=/tmp/data/empty/5 bs=10M count=1

# pliki z git'a
git clone https://github.com/MiloszKrajewski/SilesiaCorpus /tmp/data/various
