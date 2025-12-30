export const ControlFlowFor = () => {
    // 대괄호 = 배열 - array
    // 배열: 여러개의 값을 담을 수 있는 그릇
    // 예시: 이커머스 장바구니안에 여러개의 상품을 한번에 담아서 계산할 때 사용

    // for문: (초기값; 조건식; 증감식) { 반복시킬 코드 }
    // 조건이 만족된다는 전제하에 반복시킬 코드 : loopResultArray.push(i);
    let loopResultArray = [];

    for (let i = 1; i <= 3; i++) {
        loopResultArray.push(i);
    }

    return (
        <div>
            <h3>javascript 제어문 (for)</h3>

            <pre>{
                `
loopResultArray = [${loopResultArray}]
                `
            }</pre>
        </div>
    )
}