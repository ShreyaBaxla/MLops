import unittest

# Palindrome function
def is_palindrome(s):
    cleaned = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned == cleaned[::-1]

# Test Case Class
class TestIsPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        input_str = "madam"
        expected_result = True
        actual_result = is_palindrome(input_str)
        self.assertEqual(actual_result, expected_result)
        print(f"test_palindrome_simple: {'PASSED' if actual_result == expected_result else 'FAILED'}")

    def test_palindrome_with_spaces_and_case(self):
        input_str = "A man a plan a canal Panama"
        expected_result = True
        actual_result = is_palindrome(input_str)
        self.assertEqual(actual_result, expected_result)
        print(f"test_palindrome_with_spaces_and_case: {'PASSED' if actual_result == expected_result else 'FAILED'}")

    def test_not_palindrome(self):
        input_str = "hello"
        expected_result = False
        actual_result = is_palindrome(input_str)
        self.assertEqual(actual_result, expected_result)
        print(f"test_not_palindrome: {'PASSED' if actual_result == expected_result else 'FAILED'}")

    def test_palindrome_with_numbers_and_special_chars(self):
        input_str = "1A Toyota! racecar@ aToy1a"
        expected_result = True
        actual_result = is_palindrome(input_str)
        self.assertEqual(actual_result, expected_result)
        print(f"test_palindrome_with_numbers_and_special_chars: {'PASSED' if actual_result == expected_result else 'FAILED'}")

    def test_empty_string(self):
        input_str = ""
        expected_result = True
        actual_result = is_palindrome(input_str)
        self.assertEqual(actual_result, expected_result)
        print(f"test_empty_string: {'PASSED' if actual_result == expected_result else 'FAILED'}")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
