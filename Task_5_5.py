src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src_ = {i: 0 for i in src}

for i in src:
    if i in src_:
        src_[i] += 1

print([i for i in src_ if src_[i] == 1])