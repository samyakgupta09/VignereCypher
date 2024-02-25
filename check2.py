#!/usr/bin/env python3

from math import log2

print("Checking your code is named a1.py in the same directory as this file!")
import a1
print("OK")

print("Checking your code contains a function named cross_entropy ...")
from a1 import cross_entropy
print("OK")

freqs_a = {
    "A": 0.1,
    "B": 0.9,
    }

freqs_b = {
    "A": 0.4,
    "B": 0.6,
}

freqs_c = {
    "A": 0.2,
    "B": 0.3,
    "C": 0.5,
}

freqs_d = {
    "D": 0.05,
    "E": 0.95,
}

freqs_f = {
    "F": 0.01,
    "G": 0.99,
}


print("Checking cross_entropy works correctly for chars in both")
correct = -0.1 * log2(0.1) - 0.9 * log2(0.9)
got = cross_entropy(freqs_a, freqs_a)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in both #2")
correct = -0.1 * log2(0.4) - 0.9 * log2(0.6)
got = cross_entropy(freqs_a, freqs_b)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in both #3")
correct = -0.4 * log2(0.1) - 0.6 * log2(0.9)
got = cross_entropy(freqs_b, freqs_a)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in both #4")
correct = -0.4 * log2(0.4) - 0.6 * log2(0.6)
got = cross_entropy(freqs_b, freqs_b)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in freqs1 that aren't in freqs2")
correct = -0.2 * log2(0.1) - 0.3 * log2(0.9) - 0.5 * log2(0.1)
got = cross_entropy(freqs_c, freqs_a)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in freqs2 that aren't in freqs1")
correct = 0.0
correct -= 0.1 * log2(0.2)
correct -= 0.9 * log2(0.3)
correct -= 0.1 * log2(0.5)
got = cross_entropy(freqs_a, freqs_c)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly for chars in freqs2 that aren't in freqs1")
correct = 0.0
correct -= 0.1 * log2(0.2)
correct -= 0.9 * log2(0.3)
correct -= 0.1 * log2(0.5)
got = cross_entropy(freqs_a, freqs_c)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("Checking cross_entropy works correctly when freqs1 and freqs2 have no chars in common")
correct = 0.0
correct -= 0.05 * log2(0.01)
correct -= 0.95 * log2(0.01)
correct -= 0.05 * log2(0.01)
correct -= 0.05 * log2(0.99)
got = cross_entropy(freqs_d, freqs_f)
print(f"Expected: {correct}   Got: {got}")
assert abs(correct - got) < 0.0001
print("OK")

print("ALL OK")
print("Don't forget to run check1 too!")

