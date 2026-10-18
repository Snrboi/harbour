# Two Pointers — Teach-Back Notes

## Learning goal

By the end of this teach-back, the team should be able to explain **what the Two Pointers pattern is, why it works, what information makes a pointer movement safe, and when it improves a straightforward solution**.

> **Core idea:** Two Pointers keeps two meaningful positions in a sequence and moves one or both according to a rule that eliminates unnecessary work.

A “pointer” here usually means an **index or reference to a position**, not a low-level memory pointer.

---

## 1. Sorted Arrays — Finding a Pair With a Target Sum

### Problem

Given a **sorted** array and a target, determine whether two different elements add up to the target.

Example:

```python
numbers = [1, 2, 3, 4, 6, 8, 9]
target = 12
```

One valid pair is `3 + 9 = 12`.

### Approach A — Brute Force

The most direct idea is to try every possible pair.

```python
def pair_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])
    return None
```

#### Why it works

Every possible pair is eventually checked, so if a valid pair exists we will find it.

#### Cost

- **Time:** `O(n²)`
- **Extra space:** `O(1)`

The problem is repeated work: for large arrays we may inspect a huge number of pairs.

### Approach B — Two Pointers

Because the array is sorted, its ordering tells us how to move.

```text
L                       R
↓                       ↓
[1, 2, 3, 4, 6, 8, 9]
```

Calculate the current sum.

- If `sum == target`: found.
- If `sum < target`: we need a larger sum, so move `left` right.
- If `sum > target`: we need a smaller sum, so move `right` left.

```python
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
```

#### Why is a pointer movement safe?

Suppose `numbers[left] + numbers[right] < target`.

`numbers[right]` is already the largest available value. If the smallest current value cannot reach the target even when paired with that largest value, pairing it with any smaller value cannot work either. We can safely discard it and move `left`.

The opposite reasoning applies when the sum is too large.

#### Cost

- **Time:** `O(n)`
- **Extra space:** `O(1)`

### Comparison

| Approach | Time | Extra space | Key requirement |
|---|---:|---:|---|
| Brute force | `O(n²)` | `O(1)` | None |
| Two pointers | `O(n)` | `O(1)` | Array must already be sorted for this movement rule |

### Important trade-off

If the input is **not sorted**, sorting first costs `O(n log n)`. A hash-set solution can often solve pair sum in average `O(n)` time but uses `O(n)` extra memory. The best choice depends on the requirements.

### Teaching question

**Why can't we use the same left/right movement rule on an unsorted array?**

Because moving to the next position no longer guarantees a larger or smaller value. We lose the information that made elimination safe.

---

## 2. Palindromes

### Problem

Determine whether a string reads the same forward and backward.

Examples:

```text
racecar → palindrome
level   → palindrome
hello   → not a palindrome
```

### Approach A — Reverse the String

Python gives us a very simple solution:

```python
def palindrome_reverse(text):
    reversed_text = text[::-1]
    return text == reversed_text
```

#### Cost

- **Time:** `O(n)`
- **Extra space:** `O(n)`

The time is already linear, but reversing creates another string whose size grows with the input.

### Approach B — Two Pointers

A palindrome requires mirrored positions to match.

```text
R A C E C A R
↑           ↑
L           R
```

Compare the ends and move inward.

```python
def palindrome_two_pointers(text):
    left = 0
    right = len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True
```

#### Why it works

At every step, we verify a pair of mirrored positions. One mismatch is enough to prove the string is not a palindrome, so the algorithm can terminate immediately.

A useful **invariant** is:

> Everything outside `left` and `right` that has already been checked consists of matching mirrored pairs.

#### Cost

- **Time:** `O(n)`
- **Extra space:** `O(1)`

### Comparison

| Approach | Time | Extra space |
|---|---:|---:|
| Reverse string | `O(n)` | `O(n)` |
| Two pointers | `O(n)` | **`O(1)`** |

Here Two Pointers mainly improves **space**, not Big-O time.

### Real-world variation — ignore punctuation and case

For `"A man, a plan, a canal: Panama"`, we may want to ignore punctuation, spaces, and capitalization.

A space-efficient Two Pointers version can skip unwanted characters without first constructing a cleaned copy:

```python
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
```

### Edge cases to discuss

- Empty string
- One-character string
- Two equal/different characters
- Capital letters
- Spaces and punctuation
- Whether Unicode/non-English characters matter for the specification

### Teaching question

**Why use `while left < right` rather than `left <= right`?**

When the pointers meet, they refer to the same middle character. A character always equals itself, so there is nothing left to prove.

---

## 3. Container With Most Water

### Problem

Given vertical lines represented by their heights, choose two lines that form the container with the largest possible area.

```python
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```

For positions `left` and `right`:

```text
width = right - left
usable_height = min(heights[left], heights[right])
area = width * usable_height
```

The shorter wall determines usable height because water spills over the shorter side.

### Approach A — Brute Force

Try every pair of walls.

```python
def max_water_brute_force(heights):
    max_area = 0

    for left in range(len(heights)):
        for right in range(left + 1, len(heights)):
            width = right - left
            usable_height = min(heights[left], heights[right])
            area = width * usable_height
            max_area = max(max_area, area)

    return max_area
```

#### Cost

- **Time:** `O(n²)`
- **Extra space:** `O(1)`

It is correct, but checks many pairs that can be ruled out logically.

### Approach B — Two Pointers

Start with maximum possible width:

```text
L                               R
↓                               ↓
[1, 8, 6, 2, 5, 4, 8, 3, 7]
```

Calculate the area, save the best result, and then move the pointer at the **shorter wall**.

```python
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
```

### Why move the shorter wall?

Suppose:

```text
left height  = 5
right height = 10
```

The container is limited to height `5`.

If we keep the `5` and move the `10` inward:

- width becomes smaller;
- usable height can still be at most `5`.

That cannot improve the current area for that fixed shorter wall.

If we instead discard the `5`, the next wall might be taller. The width decreases, but the limiting height now has a chance to increase.

> Moving the shorter wall does **not guarantee** the next area is better. It is the only move that still has a chance to improve the limiting height.

### Cost

- **Time:** `O(n)`
- **Extra space:** `O(1)`

### Comparison

| Approach | Time | Extra space |
|---|---:|---:|
| Every pair | `O(n²)` | `O(1)` |
| Two pointers | **`O(n)`** | `O(1)` |

### Trap question

**Why don't we move the taller wall?**

Because the shorter wall is already limiting the container. Moving the taller wall decreases width without allowing the current limiting height to increase.

---

## 4. What connects all three examples?

Do **not** memorize “Two Pointers means put one index at each end.”

The stronger definition is:

> **Two Pointers is a problem-solving pattern where two positions move through data according to rules that allow us to safely eliminate possibilities or avoid unnecessary copying/scanning.**

The movement rule comes from the problem:

| Problem | Information used | Movement rule |
|---|---|---|
| Sorted pair sum | Sorted order | Too small → move left; too large → move right |
| Palindrome | Mirrored characters must match | Match → move both inward; mismatch → stop |
| Container | Shorter wall limits area | Move the shorter wall |

The key question when solving a new problem is:

> **What fact makes it safe to move this pointer and never reconsider what I just discarded?**

---

## 5. Quick Complexity Summary

| Problem | Straightforward approach | Two Pointers | Main improvement |
|---|---|---|---|
| Sorted pair sum | `O(n²)` time, `O(1)` space | `O(n)` time, `O(1)` space | Time |
| Palindrome | `O(n)` time, `O(n)` space | `O(n)` time, `O(1)` space | Space |
| Container | `O(n²)` time, `O(1)` space | `O(n)` time, `O(1)` space | Time |

Two Pointers does **not** automatically turn every problem into `O(n)`, and an algorithm can be better even when its Big-O class stays the same.

---

# Exploration — Other Two Pointer Variations

These are **not the main teach-back topics**. Use them if someone wants to explore the wider pattern.

## A. Same-direction / read-write pointers

Typical idea:

```text
write
 ↓
[1, 1, 2, 2, 3, 4, 4]
    ↑
   read
```

One pointer scans the input while another maintains a boundary or output position.

Good problems to explore:

- Remove duplicates from a sorted array
- Move zeroes to the end
- Partition an array around a condition

Search/study terms: **read/write pointers**, **in-place array modification**, **stable partition**.

## B. Fast and slow pointers

Two pointers move in the same direction at different speeds:

```text
slow → one step
fast → two steps
```

Good problems to explore:

- Find the middle of a linked list
- Detect a linked-list cycle (Floyd's cycle detection)
- Find the start of a cycle

Search/study terms: **tortoise and hare**, **Floyd cycle detection**, **fast slow pointer**.

## C. Two Pointers vs Sliding Window

Sliding Window often uses two boundary pointers, but the important concept is maintaining a **contiguous window** whose state changes as its boundaries move.

Explore:

- Longest substring without repeating characters
- Smallest subarray satisfying a target
- Fixed-size window sums

This connects directly to the next Harbour Python-problem-solving chunk.

---

# Suggested 15-Minute Teach-Back Flow

1. **2 min — Definition and motivation:** Two Pointers is about exploiting structure to avoid unnecessary work.
2. **4 min — Sorted pair sum:** brute force → sorted-array insight → pointer movement → `O(n²)` vs `O(n)`.
3. **3 min — Palindrome:** reverse-copy solution → mirrored comparison → `O(n)` space vs `O(1)`.
4. **4 min — Container With Most Water:** brute force → area formula → why shorter pointer moves → `O(n²)` vs `O(n)`.
5. **1 min — Wider family:** same-direction and fast/slow exist too.
6. **1 min — Takeaway:** always ask what information makes discarding a position safe.

## Final takeaway

Two Pointers is not valuable because it uses two variables. It is valuable because **the structure of the problem gives us enough information to move through the search space without repeatedly reconsidering discarded possibilities**.
