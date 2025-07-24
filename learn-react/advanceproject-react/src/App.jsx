import {Route, RouterProvider,createBrowserRouter, createRoutesFromElements} from 'react-router-dom';
import HomePage from './pages/HomePage';
import About from './pages/About';


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path='/'>
        <Route index element={<HomePage />} />
        <Route path='about' element={<About />} />
    </Route>
  )
)

const App = () => {
  return (
    <RouterProvider router={router} />
  )
}

export default App