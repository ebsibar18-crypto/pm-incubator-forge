export const ControlFlowSwitch = () => {
    let grade = Math.floor(Math.random() * 6) + 1;
    let gradeName

    switch(grade) {
        case 1: gradeName = "SSS"; break;
        case 2: gradeName = "SS"; break;
        case 3: gradeName = "S"; break;
        case 4: gradeName = "A"; break;
        case 5: gradeName = "B"; break;

        default: gradeName = "규격 외(심해)"; break;
    }
    
    return (
        <div>
            <h3>javascript 제어문 (if)</h3>

            <pre>{
                `
grade = ${grade}                                   //
gradeName = ${gradeName}                         // 
                `
            }</pre>
        </div>
    )
}