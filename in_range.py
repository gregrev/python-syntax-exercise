def in_range(nums, lowest, highest):
    """Print numbers inside range.

    - nums: list of numbers
    - lowest: lowest number to print
    - highest: highest number to print

    For example:

      in_range([10, 20, 30, 40], 15, 30)

    should print:

      20 fits
      30 fits
    """

    # YOUR CODE HERE
    numbers = nums
    low = lowest
    high = highest
    for num in numbers:
        if num >= low and num <= high: 
            print(num)
            



in_range([10, 20, 30, 24, 16, 21, 22,29, 40, 50], 15, 30)         
