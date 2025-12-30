import './App.css'
import { ControlFlowFor } from './control_flow/ControlFlowFor'
import { ControlFlowForSummation } from './control_flow/ControlFlowForSummation'
import { ControlFlowIf } from './control_flow/ControlFlowIf'
import { ControlFlowIfSwitch } from './control_flow/ControlFlowSwitch'
import { VariableAndDataTypes } from './data_type/VariableAndDataTypes'
import { LogicalOperationExample } from './logical_operation/LogicalOperationExample'
import { CalculationExample } from './math_operation/CalculationExample'
import { FirstProblem } from './problem/FirstProblem'

function App() {

  return (
    <>
      <div>
        <CalculationExample/>
        <VariableAndDataTypes/>        
        <LogicalOperationExample/>
        <ControlFlowIf/>
        <FirstProblem/>
        <ControlFlowIfSwitch/>
        <ControlFlowFor/>
        <ControlFlowForSummation/>
      </div>
    </>
  )
}

export default App