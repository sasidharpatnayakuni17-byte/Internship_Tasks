#Q1. Find the Frequency of Each Word in a Sentence

def word_frequency(sentence):
    result = {}

    for word in sentence.split():
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result

#Q2. Find the Frequency of Each Character in a Word
def character_frequency(word):
    result = {}

    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1

    return result

#Q3. Find the First Non-Repeating Character in a Word
def first_non_repeating(word):
    frequency = character_frequency(word)
    for char in word:
        if frequency[char] == 1:
            return char
    return None


# Q4. Check Whether Two Strings Are Anagrams
def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


# Q5. Find the First Repeating Character in a String
def first_repeating(word):
    seen = set()
    for char in word:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move All Zeros to the End of a List
def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]
    zeros = [num for num in numbers if num == 0]
    return non_zeros + zeros


# Q7. Find the Second Highest Distinct Number
def second_highest(numbers):
    unique_numbers = sorted(set(numbers), reverse=True)
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]


# Q8. Remove Duplicates Without Changing the Original Order
def remove_duplicates(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result


# Q9. Find the Missing Number from 1 to N
def missing_number(numbers, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum


# Q10. Find Two Numbers Whose Sum Equals a Target
def two_sum(numbers, target):
    for j in range(len(numbers)):
        for i in range(j):
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
    return []


# Q11. Find the Number Closest to Zero
def closest_to_zero(numbers):
    if not numbers:
        return None
    return min(numbers, key=lambda num: (abs(num), num < 0))


# Q12. Find Common Elements Between Two Lists
def common_elements(list1, list2):
    result = []
    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result


# Q13. Rotate a List to the Right by K Positions
def rotate_right(numbers, k):
    if not numbers:
        return []
    k = k % len(numbers)
    return numbers[-k:] + numbers[:-k] if k else numbers[:]


# Q14. Find the Maximum Sum of Two Consecutive Elements
def max_adjacent_sum(numbers):
    if len(numbers) < 2:
        return None
    return max(numbers[i] + numbers[i + 1]
               for i in range(len(numbers) - 1))


# Q15. Find All Pairs Whose Sum Equals a Target

def all_target_pairs(numbers, target):
    pairs = set()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                pair = tuple(sorted((numbers[i], numbers[j])))
                pairs.add(pair)

    return [list(pair) for pair in sorted(pairs)]

