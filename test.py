<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }
        input, button {
            padding: 10px;
            margin: 5px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <h1>Calculator</h1>

    <input type="number" id="num1" placeholder="First number">
    <input type="number" id="num2" placeholder="Second number">
    <br>

    <button onclick="calculate('+')">Add</button>
    <button onclick="calculate('-')">Subtract</button>
    <button onclick="calculate('*')">Multiply</button>
    <button onclick="calculate('/')">Divide</button>

    <h2 id="result">Result: </h2>

    <script>
        function calculate(op) {
            let n1 = parseFloat(document.getElementById("num1").value);
            let n2 = parseFloat(document.getElementById("num2").value);
            let res;

            if (isNaN(n1) || isNaN(n2)) {
                res = "Enter valid numbers";
            } else {
                if (op === '+') res = n1 + n2;
                else if (op === '-') res = n1 - n2;
                else if (op === '*') res = n1 * n2;
                else if (op === '/') {
                    if (n2 === 0) res = "Cannot divide by zero";
                    else res = n1 / n2;
                }
            }

            document.getElementById("result").innerText = "Result: " + res;
        }
    </script>

</body>
</html>
