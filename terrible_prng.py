# Generate some pseudorandom numbers based on three seed values.
import random

def terrible_prng(seed = None):
  # Just in case
  try:
    # I will accept any pull requests that only change these four values:
    exponent = 101
    modulus = 19
    base = 23
    max_values = 30
    # We'll start with the randomist of numbers: 3.
    random_numbers = [3]
    # Make sure the algorithm parameters have the right types. 
    if not (type(exponent) == int and type(modulus) == int and type(base) == int and type(max_values) == int):
      return random_numbers

    # You get as many numbers as you get.
    num_values = random.randint(0, max_values - 1)
    for _ in range(num_values):
      base = pow(base, exponent, modulus)
      random_numbers.append(base)
    return random_numbers
  except:
    return [3]
