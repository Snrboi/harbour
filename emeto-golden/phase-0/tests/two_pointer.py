## 1. Sorted Arrays — Finding a Pair With a Target Sum

numbers = [1, 2, 3, 4, 6, 8, 9]
target = 12

def pair_sum_two_pointers(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return (numbers[left], numbers[right])

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return None

result = pair_sum_two_pointers(numbers, target)
print(result)


## 2. Palindromes

## easy way to check for palindrome.
def palindrome_two_pointers(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True

result = palindrome_two_pointers("racecar")
print(result)


## checking for palindrome covering all cases including spaces, punctuation, and case sensitivity.
def valid_palindrome_two_pointers(text):
    left = 0
    right = len(text) - 1

    while left < right:
        while left < right and not text[left].isalnum():
            left += 1

        while left < right and not text[right].isalnum():
            right -= 1

        if text[left].lower() != text[right].lower():
            return False

        left += 1
        right -= 1

    return True

result = valid_palindrome_two_pointers("A man, a plan, a canal: Panama")
print(result)


## 3. Container With Most Water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def max_water_two_pointers(heights):
    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:
        width = right - left
        usable_height = min(heights[left], heights[right])
        area = width * usable_height

        max_area = max(max_area, area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

result = max_water_two_pointers(heights)
print(result)