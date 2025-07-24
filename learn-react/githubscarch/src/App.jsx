import axios from "axios";
import { useState } from "react";

const App = () => {

  const [username, setusername] = useState('');
  const [user, setuser] = useState({});

  // 1st crested a Function  , async is nessesary for function
  const scarchGithub = async (name) => {
  const {data} = await axios.get(`https://api.github.com/users/${name}`);
      // datadestructure

  console.log(data);
  setuser(data);

}

// callingfunction
  // scarchGithub(username);

  const serachuser = () => {
    console.log(username);
    scarchGithub(username);
    
  }

  return (
    <>
      <h1>GIThuB-Scarch</h1>

      <input type="text" placeholder="Serach Github username" onChange={(e) => setusername(e.target.value)} />
      <button onClick={serachuser}>Scarch</button>

      <h3>{user.name}</h3>
      <img src={user.avatar_url} alt="" width="100%"/>
      <p>{user.bio}</p>
      <p>{user.location}</p>
      
      
    </>
  )
}

export default App;