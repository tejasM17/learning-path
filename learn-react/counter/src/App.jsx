import Buttons from "./components/Buttons"
import Display from "./components/Display"
import CounterContextProvider from "./context/CounterContextProvider"

const App = () => {
  return (<>
    <h1>Counter  App</h1>


    <CounterContextProvider>
      <Display />
      <Buttons /> 
    </CounterContextProvider>
    
  </>
  )
}

export default  App