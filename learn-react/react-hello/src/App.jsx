import { useState } from 'react';


const App = () => {
  const [count, setCount] = useState(0)

  const dislike = () => {
    if (count > 0) {
      
    setCount(count - 1)
  }
}

  const increaseCount = () => {
    setCount(count + 1)
    console .log('Thanks For The Like')
  }



  return(
  <>

    <h1>Hi Brothers</h1>
    <p>{count}</p>
    <button onClick={increaseCount}>like</button>

    <button onClick={dislike}>dislike</button>
    
  </>
    
  )
}

export default App;