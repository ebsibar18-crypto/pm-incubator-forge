export const FirstProblem = () => {
    let z = 10;
    let x = 5;
    let result;

    if (z>x) {
        result = "Hello"
        

    } else {
        result = "Hi"
    }

   

    let ternaryResult = z>x? "z는 x보다 크다" : "z는 x보다 작거나 같다"
   
    return (
        <div>
            <h3>javascript 첫 번째 퀴즈 </h3>

            <pre>{
                `
z가 x보다 크면 Hello,
z가 x보다 작거나 같으면 Hi를 출력해주세요. 

x = ${x}                          // 5
z = ${z}                          // 10
result = ${result}                // z는 x보다 크다. 
ternaryResult = ${ternaryResult}

                `
            }</pre>
        </div>
    )
} 