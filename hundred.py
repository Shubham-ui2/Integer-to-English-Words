def numberToWord(num):

    one = ["", "One", "Two", "Three", "Four", "Five",
           "Six", "Seven", "Eight", "Nine"]

    ten = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
           "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


    def small(n):
        word = ""
        # hundred part
        if n >= 100:
            a = n // 100
            word = word + one[a] + " Hundred "
            n = n % 100
        # 10 to 19
        if n >= 10 and n <= 19:
            word = word + ten[n - 10]
        else:
            # tens
            if n >= 20:
                b = n // 10
                word = word + tens[b] + " "
                n = n % 10
            # single number
            if n > 0:
                word = word + one[n]
        return word
    ans = ""

    # for negative number
    if num < 0:
        ans = "Minus "
        num = num * -1

    # for thousand
    if num >= 1000:
        t = num // 1000
        ans = ans + one[t] + " Thousand "
        num = num % 1000
    ans = ans + small(num)
    if ans == "":
        ans = "Zero"
    return ans
while True:

    n = int(input("Enter number : "))
    result = numberToWord(n)
    print(result)
    again = input("Want to enter again ? ")
    if again == "no":
        break