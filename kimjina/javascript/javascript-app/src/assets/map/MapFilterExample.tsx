export const MapFilterExample= () => {
    let number_array : number[] = [2, 4, 6, 8, 10]
    
    // fflter가 오면 배열의 요소를 element로 뽑습니다.
    // 화살표 이후가 핵심인데
    // element % 4 === 0 은 아래를 의미한다,
    // 배열의 낱개 요소를 4로 나눈 나머지가 0 맞아? true / false
    // filter는 조건의 결과가 true인 녀석들만 뽑아간다.
    let  result_array : number[] = 
          number_array.filter(element => element % 4 === 0)

          // 만약 for루프로 구현한다면 어떻게 해야 했을까? Te -> Ti로 논리 검증
          // for (배열 전체 순회){
          //    if (배열요소 % 4 === 0){
          //        result_array.push(베열요소)
          //     }
          //}
    
return (
    <div>
        <h3> javascript Reduce Function</h3>

        <pre>{
             `
number_array = ${number_array}
result_array = ${result_array}
             `   
            }</pre>
    </div>
   )
}
