export const MapReduceExample = () => {
    let numbber_array: number[] = [2, 4, 6, 8, 10]

    // reduce의 경우엔 아래와 같이 연산됩니다. 
    // (누산 대상, 배열의 요소) => 누산 대상 + 배열 요소, 초기값)
    // accumulatr의 시작값은 지정한 초기값으로 설정됨. 
    
    // 실행 효율 T 관점입니다. 
    // 앞서 만들었던 다소 복잡한 연산의 for loop 구성을 단순화 시킨 작업임. 
    let result_array: number = 
        numbber_array.reduce((accumulator, element) => accumulator + element, 0)
    
    return (
        <div> 
            <h3>javascript Reduce Function</h3>
            <pre>{
            `
number_array = ${numbber_array}
square_result_array = ${result_array}
            `   
            }</pre>
        </div>    
    )
}
 