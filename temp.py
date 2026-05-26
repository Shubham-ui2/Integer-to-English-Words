def convert(num):

    ones = ["", "One", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine"]

    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
             "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    # small function for numbers below 1000
    def part(n):

        ans = ""

        if n >= 100:
            ans = ans + ones[n // 100] + " Hundred "
            n = n % 100

        if n >= 10 and n <= 19:

            ans = ans + teens[n - 10]

        else:

            if n >= 20:
                ans = ans + tens[n // 10] + " "
                n = n % 10

            if n > 0:
                ans = ans + ones[n]

        return ans.strip()


    if num == 0:
        return "Zero"

    final = ""

    if num < 0:
        final = "Negative "
        num = num * -1

    # crore
    if num >= 10000000:

        c = num // 10000000

        final = final + part(c) + " Crore "

        num = num % 10000000

    # lakh
    if num >= 100000:

        l = num // 100000

        final = final + part(l) + " Lakh "

        num = num % 100000

    # thousand
    if num >= 1000:

        t = num // 1000

        final = final + part(t) + " Thousand "

        num = num % 1000

    # last part
    if num > 0:

        final = final + part(num)

    return final.strip()


while True:

    n = int(input("Enter number : "))

    print(convert(n))

    ch = input("Again? yes/no : ")

    if ch == "no":
        break