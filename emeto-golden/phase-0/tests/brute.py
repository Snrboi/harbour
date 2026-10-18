## 1. Sorted Arrays — Finding a Pair With a Target Sum

numbers = [1, 2, 3, 4, 6, 8, 9]
target = 12

def pair_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None

result = pair_sum_brute_force(numbers, target)
print(result)


## 2. Palindromes
## easy way to check for palindrome.
def palindrome_reverse(text):
    reversed_text = text[::-1]
    return text == reversed_text

result = palindrome_reverse("racecar")
print(result)


## checking for palindrome covering all cases including spaces, punctuation, and case sensitivity.
def is_palindrome(text):
    cleaned = ""

    for char in text:
        if char.isalnum():
            cleaned += char.lower()

    return cleaned == cleaned[::-1]

result = is_palindrome("A man, a plan, a canal: Panama")
print(result)



## 3. Container With Most Water
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def max_water_brute_force(heights):
    max_area = 0

    for left in range(len(heights)):
        for right in range(left + 1, len(heights)):
            width = right - left
            usable_height = min(heights[left], heights[right])
            area = width * usable_height
            max_area = max(max_area, area)

    return max_area

result = max_water_brute_force(heights)
print(result)