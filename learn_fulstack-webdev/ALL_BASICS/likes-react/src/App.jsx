import { NavLink } from "react-router";
import {useState} from 'react'

function App () {
  const [likes, setLikes] = useState(0)

  const likeButtonClick = () => {
    console.log('clicked')
    setLikes(likes + 1)
    // alert('like button clicked')
  }

  const disLike = () => {

    if (likes > 0 ) {
      setLikes(likes - 1)
      // alert('unlike button clicked')
    }
  }


  return (
    <div className="App">
      <h1>React + Vite</h1>
      <nav>
        <NavLink to="/about">About</NavLink>
      </nav>
    <div>
      <h2>Like Website</h2>
      <h1>total likes {likes}</h1>
      <br />
      <button onClick={likeButtonClick}>like</button>
      <button onClick={disLike}>unlike</button>
    </div>

    </div>
  )
}
export default App