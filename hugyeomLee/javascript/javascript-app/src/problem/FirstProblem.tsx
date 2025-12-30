export const FirstProblem = () => {
    // z가 x보다 크면 Hello를 result에 할당
    // 그렇지 않으면 Hi를 result에 할당
    // x와 z의 값은 마음대로 정하면 됩니다.

    let x = 10;
    let z = 20;
    let result;
    
    if (x > z) {
        // x는 z보다 크다.
        result = "Hello"
    } else {
        // x는 z보다 작거나 같다.
        result = "Hi"
    }

    let ternaryResult = x > z ? "Hello" : "Hi"

    return (
        <div>
            <h3>Javascript 첫 번째 퀴즈 (if)</h3>

            <pre>{
                `
x = ${x}                         // 10
z = ${z}                         // 20
result = ${result}               // x는 z보다 작다. if-else 문 결과
ternaryResult = ${ternaryResult} // 삼항 연산자 결과
                `
            }</pre>
        </div>
    )
}