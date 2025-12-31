export const MapFilterExample = () => {
    let number_array: number[] = [2, 4, 6, 8, 10];
    
    let result_array: number[] = 
        number_array.filter(element => element % 4 === 0);
        // 배열의 낱개 요소를 4로 나눈 나머지가 0인 요소만 걸러내기

    return (
        <div>
            <h3>javascript Filter Function</h3>

            <pre>{
                `
number_array = [${number_array}]
result_array = [${result_array}]
                `
            }</pre>
        </div>
    )
}