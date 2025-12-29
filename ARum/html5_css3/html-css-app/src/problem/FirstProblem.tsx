export const FirstProblem = () => {
    let x = 10;
    let z = 20;
    let result;

    if (z > x) {
        result = "Hello"
    } else {
        result = "Hi"
    }

    let ternaryResult = z > x ? "Hello" : "Hi"

    return (
        <div>
            <h3>javascript 제어문 (if)</h3>

            <pre>{
                `
x = ${x}                            // 10
z = ${z}                            // 20
result = ${result}                  // Hello
ternaryResult = ${ternaryResult}
                `
            }</pre>
        </div>
    )
}