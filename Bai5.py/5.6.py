class Polynomial:
    def __init__(self, coeffs: list):
        # coeffs[0] là hệ số bậc cao nhất
        self.coeffs = list(coeffs)

    def __str__(self):
        terms = []
        degree = len(self.coeffs) - 1

        for i, coef in enumerate(self.coeffs):
            if coef == 0:
                continue

            power = degree - i

            # Xử lý dấu
            sign = "-" if coef < 0 else "+"
            abs_coef = abs(coef)

            # Tạo term
            if power == 0:
                term = f"{abs_coef}"

            elif power == 1:
                if abs_coef == 1:
                    term = "x"
                else:
                    term = f"{abs_coef}x"

            else:
                if abs_coef == 1:
                    term = f"x^{power}"
                else:
                    term = f"{abs_coef}x^{power}"

            terms.append((sign, term))

        # Nếu tất cả hệ số đều = 0
        if not terms:
            return "0"

        # Term đầu tiên
        first_sign, first_term = terms[0]

        if first_sign == "-":
            result = f"-{first_term}"
        else:
            result = first_term

        # Các term còn lại
        for sign, term in terms[1:]:
            result += f" {sign} {term}"

        return result

    def __call__(self, x):
        # Horner's Method
        result = 0

        for coef in self.coeffs:
            result = result * x + coef

        return result

    def __add__(self, other):
        a = self.coeffs[:]
        b = other.coeffs[:]

        # Zero-pad đa thức ngắn hơn
        if len(a) < len(b):
            a = [0] * (len(b) - len(a)) + a
        elif len(b) < len(a):
            b = [0] * (len(a) - len(b)) + b

        new_coeffs = []

        for i in range(len(a)):
            new_coeffs.append(a[i] + b[i])

        return Polynomial(new_coeffs)