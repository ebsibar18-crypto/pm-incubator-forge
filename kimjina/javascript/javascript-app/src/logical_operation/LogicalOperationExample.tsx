export const LogicalOperationExample = () => {
    const strictEquality = 10 === ("10" as any)
    const roughEquality = 10 == ("10" as any)
    const logicalAnd = true && false
    const logicalOr = true || false
    const bitwiseAnd = 5 & 4
    const bitwiseOr = 5 | 2

return (
    <div>
        <h3> javascript 논리 연산자</h3>

        <pre>{
             `
console.log(10 === "10");      // ${strictEquality}
console.log(10 == "10");       // ${roughEquality}
console.log(true && false);    // ${logicalAnd}
console.log(true || false);    // ${logicalOr}
console.log(5 & 4);            // ${bitwiseAnd}
console.log(5 | 2);            // ${bitwiseOr}
             `   
            }</pre>
    </div>
   )
}