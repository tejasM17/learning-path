import { useContext } from "react"
import CounterContext from "../context/CounterContext"


const Buttons = () => {
    const {increase, decrease} = useContext(CounterContext);

    return (
        <>
        <button onClick={increase}>Increment</button>
        <button onClick={decrease}>Decrement</button>
        </>
    )
}

export default Buttons