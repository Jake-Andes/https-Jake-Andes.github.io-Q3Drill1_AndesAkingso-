from pyscript import document, display  # type: ignore

def adding_numbers(e=None):
    first = document.getElementById("input1").value.strip()
    last = document.getElementById("input2").value.strip()
    n1 = document.getElementById("input3").value.strip()
    n2 = document.getElementById("input4").value.strip()
    target = "output1"

    if first == "" or last == "":
        display("Please enter both first and last name.", target=target)
    else:
        if n1 == "":
            num1 = 0.0
        else:
            num1 = float(n1)
        if n2 == "":
            num2 = 0.0
        else:
            num2 = float(n2)

        avg = (num1 + num2) / 2

        if avg >= 75:
            result = f"{first} {last} — Average: {avg:.2f} ✅ Passed"
        else:
            result = f"{first} {last} — Average: {avg:.2f} ❌ Failed"

        display(result, target=target)