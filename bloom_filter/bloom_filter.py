# TODO: Wenyi Chu, wc625
# TODO: Qixin Ding, qd49

# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1
from cs5112_hash import cs5112_hash2
from cs5112_hash import cs5112_hash3

# Implementation of a basic bloom filter. Uses exactly three hash functions.
class BloomFilter:
  def __init__(self, size=10):
    # DO NOT EDIT THIS CONSTRUCTOR
    self.size = size
    self.array = FixedSizeArray(size)
    for i in range(0, size):
      self.array.set(i, False)

  # To add an element to the bloom filter, use each of the k=3 hash functions we provided and compute
  # the positions that we are setting in the fixed size array using modulo operation.
  def add_elem(self, elem):
    index1 = cs5112_hash1(elem) % self.size
    index2 = cs5112_hash2(elem) % self.size
    index3 = cs5112_hash3(elem) % self.size
    print(index1, index2, index3 )

    # set indices to True
    self.array.set(index1, True)
    self.array.set(index2, True)
    self.array.set(index3, True)


  # Returns False if the given element was definitely not added to the filter. 
  # Returns True if it's possible that the element was added to the filter.
  def check_membership(self, elem):
    index1 = cs5112_hash1(elem) % self.size
    index2 = cs5112_hash2(elem) % self.size
    index3 = cs5112_hash3(elem) % self.size
    print(index1, index2, index3 )

    value1 = self.array.get(index1)
    value2 = self.array.get(index2)
    value3 = self.array.get(index3)
    print(value1, value2, value3 )

    # if all these indices are set to True in the bit array -> probably present (True)
    result = value1 and value2 and value3
    return result

    

