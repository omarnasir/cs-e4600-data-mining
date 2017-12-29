import numpy as np

def generate_bitmask(size):
    mask = ''
    for i in range(0,size):
        mask = mask + str(np.random.binomial(1, 0.5 ** (i + 1)))
    return mask

def compute_b(bitmask,n):
    bitmask = np.binary_repr(bitmask)
    masks = [bitmask[i:i+n] for i in range(0, len(bitmask), n)]
    sum = 0
    for mask in masks:
        pos = mask.find('0')
        if pos > -1:
            sum += pos
    return sum / len(masks)