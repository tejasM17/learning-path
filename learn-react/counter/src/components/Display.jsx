import { useContext } from "react"
import CounterContext from "../context/CounterContext"
import React from "react"


const Display = () => {
    const {count} = useContext(CounterContext);

    return (
        <>
           <h1>Count = {count}</h1>
        </>
    )
}

export default  Display