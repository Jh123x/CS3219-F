from flask import Flask, jsonify


app = Flask(__name__)

cache = {}


@app.route('/factor/<path:num>', methods=["GET"])
def route_factorize(num: str):
    if(not num.isdigit()):
        return f"Error: {num} is not a valid integer"

    if (num in cache):
        return jsonify({
            'result': cache[num]
        })

    result = factorize(int(num))
    cache[num] = result
    return jsonify({
        "result": result
    })


def factorize(num: int) -> list:
    result = {1}
    curr = 2
    acc_num = num
    while (acc_num > 1 and curr < num):
        if (acc_num % curr != 0):
            curr += 1
            continue
        result.add(curr)
        acc_num = acc_num // curr

    return sorted(list(result))


if __name__ == "__main__":
    app.run(debug=True)
