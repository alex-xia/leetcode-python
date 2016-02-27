__author__ = 'Qing'

'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''

digit_lookup = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
specials = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 14: 'Fourteen', 20: 'Twenty'}
prefix_lookup = {3: 'Thir', 4: 'For', 5: 'Fif', 8: 'Eigh'}
scale_order = ['Thousand', 'Million', 'Billion']

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        res = self.number_to_word_within_thousand(num%1000)
        num = num // 1000
        rank = 0
        while num > 0:
            hundreds_name = self.number_to_word_within_thousand(num%1000)
            if len(hundreds_name) > 0:
                hundreds_name += ' ' + scale_order[rank]
                if len(res) > 0:
                    hundreds_name += ' '
            res = hundreds_name + res
            num = num // 1000
            rank += 1
        return res

    def number_to_word_within_thousand(self, num):
        assert num < 1000
        digits = num % 10
        tens = (num // 10) % 10
        hundreds = num // 100
        name = ''
        if hundreds:
            name += digit_lookup[hundreds] + ' Hundred'
        if tens:
            tens_name = self.tens_name(tens,digits)
            if len(tens_name) > 0:
                if hundreds:
                    name += ' '
                name += tens_name
        if digits:
            digits_name= self.digits_name(tens, digits)
            if len(digits_name) > 0:
                if hundreds or tens:
                    name += ' '
                name += digits_name
        return name

    def tens_name(self, tens, digits):
        num = tens * 10 + digits
        if tens == 0:
            return ''
        if tens == 1:
            if num in specials:
                return specials[num]
            if digits in prefix_lookup:
                return prefix_lookup[digits] + 'teen'
            return digit_lookup[digits] + 'teen'
        if tens in prefix_lookup:
            return prefix_lookup[tens] + 'ty'
        if tens*10 in specials:
            return specials[tens*10]
        return digit_lookup[tens] + 'ty'

    def digits_name(self, tens, digits):
        if tens != 1:
            return digit_lookup[digits]
        return ''

if __name__ == '__main__':
    s = Solution()
    print(s.numberToWords(1000010))