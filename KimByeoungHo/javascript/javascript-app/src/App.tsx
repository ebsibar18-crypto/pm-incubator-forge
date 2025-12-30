import './App.css'
import { CalculationExample } from './math_operation/CalculationExample'
import VariableAndDataTypes from './data_type/VariableAndDataTypes'
import { LogicalOperationExample } from './logical_operation/LogicalOperationExample'
import { ControlFlowIf } from './control_flox/ControlFlowIf'
import { FirstProblem } from './problem/FirstProblem'
import { ControlFlowSwitch } from './control_flox/ControlFlowSwitch'
import { ControlFlowFor } from './control_flox/ControlFlowFor'
import { ControlFlowForSummation } from './control_flox/ControlFlowForSummation'


function App() {
 
  return (
    <>
      <div>
        {/* 여러분들만의 커스텀 태그 생성 */}
        {/* 이 커스텀 태그는 단순히 사칙연산 + 나머지(MOD) 연산 */}
        <CalculationExample/>
        <VariableAndDataTypes/>
        <LogicalOperationExample/>
        <ControlFlowIf/>
        <FirstProblem/>
        <ControlFlowSwitch/>
        <ControlFlowFor/>
        <ControlFlowForSummation/>
      </div>
    </>
  )
}

export default App
