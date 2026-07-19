"""Beginner-friendly NumPy examples converted from the notebook."""


def main() -> None:
    """Run the notebook examples in a clean, readable Python script."""

    # Cell 1: Import NumPy
    # NumPy is a Python library used for working with arrays and numerical calculations.
    import numpy as np

    # Cell 2: Check NumPy Version
    # Every library has a version number, and this line shows the installed version.
    print(np.__version__)

    # Cell 3: Creating a 1D Array
    # This example creates a one-dimensional array, multiplies it by 2, and prints the result.
    array = np.array([1, 2, 3, 4])
    array = array * 2
    print(array)
    print(type(array))

    # Cell 4: Creating a 3D Array
    # This example builds a three-dimensional array and shows how to access its elements.
    array = np.array(
        [[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
         [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
         [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]]
    )
    print(array.ndim)
    print(array.shape)
    print(array[1, 1, 1])
    word = array[0, 0, 0] + array[2, 0, 0] + array[1, 0, 1]
    print(word)

    # Cell 5: NumPy Slicing in a 2D Array
    # This section demonstrates slicing rows, columns, and submatrices from a 2D array.
    array = np.array([[1, 2, 3, 4],
                      [5, 6, 7, 8],
                      [9, 10, 11, 12],
                      [13, 14, 15, 16]])
    print("Original Array")
    print(array)
    print("\n1. Single Element:")
    print(array[2, 1])
    print("\n2. Complete Row")
    print(array[1])
    print("\n3. Complete Column:")
    print(array[:, 2])
    print("\n4. Slice Rows:")
    print(array[1:3])
    print("\n5. Slice Columns:")
    print(array[:, 1:3])
    print("\n6. Submatrix:")
    print(array[1:3, 1:3])
    print("\n7. Every Second row:")
    print(array[::2])
    print("\n8. Every Second Column")
    print(array[:, ::2])
    print("\n9. Reverse Rows:")
    print(array[::-1])
    print("\n10. Reverse Columns:")
    print(array[:, ::-1])
    print("\n11. Reverse Entire Matrix:")
    print(array[::-1, ::-1])
    print("\n12. Main Diagonal:")
    print(array.diagonal())

    # Cell 6: NumPy Arithmetic and Mathematical Operations
    # This section shows common arithmetic and mathematical operations on arrays.
    array = np.array([1.99, 2.99, 3.99])
    print("Original Array:")
    print(array)
    print("\n1. Addition (+1):")
    print(array + 1)
    print("\n2. Subtraction (-2):")
    print(array - 2)
    print("\n3. Multiplication (*3):")
    print(array * 3)
    print("\n4. Division (/4):")
    print(array / 4)
    print("\n5. Power(**5):")
    print(array ** 5)
    print("\n6. Modulus (%2):")
    print(array % 2)
    print("\n7. Square Root:")
    print(np.sqrt(array))
    print("\n8. Absolute Value:")
    print(np.abs(array))
    print("\n9. Round:")
    print(np.round(array))
    print("\n10. Floor:")
    print(np.floor(array))
    print("\n11. Ceiling:")
    print(np.ceil(array))
    print("\n12. Exponential:")
    print(np.exp(array))
    print("\n13. Natural Logarithm:")
    print(np.log(array))
    print("\n14. Log Base 10:")
    print(np.log10(array))
    print("\n15. Sine:")
    print(np.sin(array))
    print("\n16. Cosine:")
    print(np.cos(array))
    print("\n17. Tangent:")
    print(np.tan(array))
    print("\n18. Maximum Values:")
    print(np.max(array))
    print("\n19. Minimum Value:")
    print(np.min(array))
    print("\n20. Clip Values (2 to 3):")
    print(np.clip(array, 2, 3))
    print("\n21. Pi Constant:")
    print(np.pi)

    # Cell 7: NumPy Broadcasting
    # Broadcasting allows smaller arrays to be expanded automatically to match larger ones.
    array1 = np.array([[1, 2, 3, 4, 5]])
    array2 = np.array([[1], [2], [3], [4], [5]])
    print("1. Row Vector * Column Vector")
    print("Array 1 Shape:", array1.shape)
    print("Array 2 Shape:", array2.shape)
    print(array1 * array2)
    print("\n2. Scalar Broadcasting")
    array = np.array([1, 2, 3, 4, 5])
    print(array + 5)
    print("\n3. 1D Array + 2D Array")
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([10, 20, 30])
    print(array1 + array2)
    print("\n4. Column Vector Broadcasting")
    array1 = np.array([[1, 2, 3], [4, 5, 6]])
    array2 = np.array([[10], [20]])
    print(array1 + array2)
    print("\n5. Broadcasting Error")
    array1 = np.array([[1, 2, 3]])
    array2 = np.array([[1, 2]])
    try:
        print(array1 + array2)
    except ValueError as e:
        print("Error:", e)

    # Cell 8: NumPy Aggregate Functions
    # This section applies summary statistics such as sum, mean, min, max, and variance.
    array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print("Original Array:")
    print(array)
    print("\n1. Sum:")
    print(np.sum(array))
    print("\n2. Mean:")
    print(np.mean(array))
    print("\n3. Median:")
    print(np.median(array))
    print("\n4. Standard Deviation:")
    print(np.std(array))
    print("\n5. Variance:")
    print(np.var(array))
    print("\n6. Minimum Value")
    print(np.min(array))
    print("\n7. Maximum Value:")
    print(np.max(array))
    print("\n8. Index of Minimum Value:")
    print(np.argmin(array))
    print("\n9. Index of Maximum Value:")
    print(np.argmax(array))
    print("\n10. Product:")
    print(np.prod(array))
    print("\n11. Cumulative Sum:")
    print(np.cumsum(array))
    print("\n12. Cumulative Product:")
    print(np.cumprod(array))
    print("\n13. Sum (axis=0):")
    print(np.sum(array, axis=0))
    print("\n14. Sum (axis=1):")
    print(np.sum(array, axis=1))
    print("\n15. Mean (axis=0):")
    print(np.mean(array, axis=0))
    print("\n16. Mean (axis=1):")
    print(np.mean(array, axis=1))
    print("\n17. Minimum(axis=0):")
    print(np.min(array, axis=0))
    print("\n18. Minimum (axis=1):")
    print(np.min(array, axis=1))
    print("\n19. Maximum (axis=0):")
    print(np.max(array, axis=0))
    print("\n20. Maximum (axis=1):")
    print(np.max(array, axis=1))
    print("\n21. Standard Deviation (axis=0):")
    print(np.std(array, axis=0))
    print("\n22. Standard Deviation (axis=1):")
    print(np.std(array, axis=1))
    print("\n23. Variance (axis=0):")
    print(np.var(array, axis=0))
    print("\n24. Variance (axis=1):")
    print(np.var(array, axis=1))

    # Cell 9: NumPy Filtering
    # This section uses Boolean indexing and np.where() for filtering values.
    ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                     [39, 22, 15, 99, 18, 19, 20, 21]])
    print("Original Array:")
    print(ages)
    print("\n1. Teenagers (Age<18):")
    teenagers = ages[ages < 18]
    print(teenagers)
    print("\n2. Adults (18 <= Age < 65):")
    adults = ages[(ages >= 18) & (ages < 65)]
    print(adults)
    print("\n3. Seniors (Age >= 65):")
    seniors = ages[ages >= 65]
    print(seniors)
    print("\n4. Even Ages:")
    evens = ages[ages % 2 == 0]
    print(evens)
    print("\n5. Odd Ages:")
    odds = ages[ages % 2 != 0]
    print(odds)
    print("\n6. Adults using np.where():")
    adults = np.where(ages >= 18, ages, 0)
    print(adults)
    print("\n7. Adults using np.where() (-1 Fill Value):")
    adults = np.where(ages >= 18, ages, -1)
    print(adults)
    print("\n8. Ages Greater Than 20:")
    print(ages[ages > 20])
    print("\n9. Ages Less Than or Equal to 20:")
    print(ages[ages <= 20])
    print("\n10. Ages Equal to 18:")
    print(ages[ages == 18])
    print("\n11. Ages Not Equal to 18:")
    print(ages[ages != 18])
    print("\n12. Age Between 20 and 40:")
    print(ages[(ages >= 20) & (ages <= 40)])
    print("\n13. Age Less Than 18 OR Greater Than 65:")
    print(ages[(ages < 18) | (ages > 65)])
    print("\n14. Replace Ages Less Than 18 with 0:")
    print(np.where(ages < 18, 0, ages))
    print("\n15. Replace Ages Greater Than 65 with 65:")
    print(np.where(ages > 65, 65, ages))

    # Cell 10: NumPy Random Numbers
    # This section shows random integers, floats, shuffle behavior, and random choices.
    rng = np.random.default_rng()
    print("1. Random Integer (1-6):")
    print(rng.integers(low=1, high=7))
    print("\n2. Random Integer (1-100):")
    print(rng.integers(low=1, high=101))
    print("\n3. Three Random Integers:")
    print(rng.integers(low=1, high=101, size=3))
    print("\n4. 3*2 Random Integer Array:")
    print(rng.integers(low=1, high=101, size=(3, 2)))
    print("\n5. Random Number using Seed:")
    rng = np.random.default_rng(seed=1)
    print(rng.integers(low=1, high=101, size=5))
    print("\n6. Random Float (0 to 1):")
    print(rng.uniform())
    print("\n7. Random Float (-1 to 1):")
    print(rng.uniform(low=-1, high=1))
    print("\n8. Three Randomm Floats:")
    print(rng.uniform(low=-1, high=1, size=3))
    print("\n9. 3*2 Random Float array:")
    print(rng.uniform(low=-1, high=1, size=(3, 2)))
    array = np.array([1, 2, 3, 4, 5])
    print("\n10. Original Array:")
    print(array)
    rng.shuffle(array)
    print("Shuffled Array:")
    print(array)
    fruits = np.array(["Apple", "Orange", "Coconut", "Banana", "Pineapple"])
    print("\n11. Random Fruits:")
    print(rng.choice(fruits))
    print("\n12. Three Random Fruits:")
    print(rng.choice(fruits, size=3))
    print("\n13. 3*3 Random Fruits:")
    print(rng.choice(fruits, size=(3, 3)))
    print("\n14. Random Boolean Values:")
    print(rng.choice([True, False], size=10))
    numbers = np.array([10, 20, 30, 40, 50])
    print("\n15. Random Numbers from Custom List:")
    print(rng.choice(numbers, size=5))


if __name__ == "__main__":
    main()
