export const ControlFlowIf = () => {
    let x = 10
    let result;

    // x>5 부동식은 ㅌ가 5보다 크나?
    // 해당 질문의 답은 참 or 거짓
    if (x > 5) {
        result = "x는 5보다 큽니다."
    } else {
        // 조건이 거짓이라면 else로 빠지게 됩니다
        result = "x는 5보다 작습니다."
    }

    let ternaryResult = x > 5 ? "x는 5보다 큽니다." : "x는 5보다 작습니다."

    return (
        <div>
            <h3>javascript 제어문 (if)</h3>

            <pre>{
                `
x = ${x}                          // 10
result = ${result}                // x는 5보다 큽니다.
ternaryResult = ${ternaryResult}
             `
            }</pre>
        </div>
    )   
            }