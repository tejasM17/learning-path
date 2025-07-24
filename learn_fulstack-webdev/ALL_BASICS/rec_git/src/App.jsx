import { useState } from "react"

function App() {
  const [username, setUsername] = useState('')
  const [userdetails, setUserdetails] = useState({})

  const searchGitHub = async () => {
    const response = await fetch(`https://api.github.com/users/${username}`)
    const data = await response.json()
    console.log(data)
    setUserdetails(data)
  }

  return (
    <div>
      <h1 className="title">gitHub search</h1>
      <input className="input" type="text" onChange={(e) => {
        setUsername(e.target.value)
      }} placeholder="enter user name"/>

      <button className="button" onClick={()=> {
        searchGitHub()
      }}>Search</button>


      <h1 className="user-name">{userdetails.name}</h1>
      <img className="user-img" src={userdetails.avatar_url} alt="" />
      <p>{userdetails.bio}</p>
    </div>
  )
}

export default App