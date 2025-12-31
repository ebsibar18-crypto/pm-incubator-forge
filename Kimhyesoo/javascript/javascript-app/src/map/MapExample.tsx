export const MapExample = () => {
    // typescript특성 -> type을 명시하는 작업
    // :number[]는 숫자 배열임을 명시하는 행위
    let number_array: number[] = [2,4,6,8,10]
    
    // square(제곱) 결과 배열
    //  number_array.map()을 사용하면 number[] 배열에 있는 요쇼들을 하나씩 꺼내옴
    // => 를 통해 배열 요소를 화살표가 가리키는 연산으로 적용.
    // num이 아닌 element로 작성해도 됨(element => element*element)
    let square_result_array: number[] = number_array.map(num => num * num) 

    return(
        <div>
            <h3>Javascript Map(Hash 방식)</h3>
            <pre>{
            `
            number_array = ${number_array}
            square_result_array = ${square_result_array}
            ` 
            }</pre>
        </div>
    )
}