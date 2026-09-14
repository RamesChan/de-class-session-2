from decimal import Decimal, InvalidOperation

from flask import Flask, render_template, request

app = Flask(__name__)
OPERATORS = {"add": "+", "subtract": "−", "multiply": "×", "divide": "÷"}


@app.route("/", methods=["GET", "POST"])
def calculator():
    left = request.form.get("left", "")
    right = request.form.get("right", "")
    operation = request.form.get("operation", "add")
    result = error = None

    if request.method == "POST":
        try:
            a, b = Decimal(left), Decimal(right)
            if not a.is_finite() or not b.is_finite() or max(abs(a), abs(b)) > Decimal("1e12"):
                raise ValueError("กรุณาใช้ตัวเลขระหว่าง -1 ล้านล้านถึง 1 ล้านล้าน")
            if operation == "add":
                answer = a + b
            elif operation == "subtract":
                answer = a - b
            elif operation == "multiply":
                answer = a * b
            elif operation == "divide":
                if b == 0:
                    raise ValueError("หารด้วยศูนย์ไม่ได้ ลองเปลี่ยนตัวเลขที่สองนะ")
                answer = a / b
            else:
                raise ValueError("กรุณาเลือกเครื่องหมายที่รองรับ")
            result = format(answer, ".10f").rstrip("0").rstrip(".")
            if result == "-0":
                result = "0"
        except InvalidOperation:
            error = "กรุณากรอกตัวเลขให้ครบทั้งสองช่อง"
        except ValueError as exc:
            error = str(exc)

    return render_template("index.html", left=left, right=right,
                           operation=operation, operators=OPERATORS,
                           result=result, error=error)


if __name__ == "__main__":
    # Classroom demo: listen on the container interface so -p can reach Flask.
    app.run(host="0.0.0.0", port=5000, debug=False)
