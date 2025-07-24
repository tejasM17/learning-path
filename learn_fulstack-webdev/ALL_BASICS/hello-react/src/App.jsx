import { useEffect,useState } from 'react';


function App() {
  const [message, setMessage] = useState();


  //  backend call
  const getHello = async() => {
    const response = await fetch('http://localhost:5000/');

    const data = await response.json();

    console.log(data);

    setMessage(data.message)

  }

  useEffect(() => {
    getHello();
  },[])


  return (
    <div>
      <h1 className="top">Hello React</h1>
      <h1>{message}</h1>
      <h3>Welcome to my app!</h3>
    </div>
  )
}

export default App