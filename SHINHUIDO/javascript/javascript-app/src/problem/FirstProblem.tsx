export const FirstProblem = () => {
    let x = 10;
    let z = 15;
    let result;

    if (z > x) {
        result = "Hello"
    }  else {
        result = "Hi"
    }

    let ternaryResult = z > x ? "Hello" : "Hi"

  return (
     <div>
        <h3>javascript 첫 번째 퀴즈 </h3>

            <pre>{
             `
x = ${x}                            // 10
z = ${z}                            // 15
result = ${result}                  // Hello
ternaryResult = ${ternaryResult}
             `
            }</pre>     
        </div>
    )
}
