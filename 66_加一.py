class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i]
            if i == len(digits) - 1:
                digits[i] = (digits[i] + carry + 1) % 10
                carry = (temp + carry + 1) // 10
            else:
                digits[i] = (digits[i] + carry) % 10
                carry = (temp + carry) // 10
        if carry == 1:
            digits.insert(0, 1)
        return digits
