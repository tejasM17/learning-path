import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import './styles/cyberpunk.css';
import App from './App.jsx';
import ViewBook from './pages/ViewBook.jsx';
import CreateBook from './pages/CreateBook.jsx';
import EditBook from './pages/EditBook.jsx';
import { AnimatePresence } from 'framer-motion';
import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom';

// Wrap routes with AnimatePresence for page transitions
const AnimatedRoutes = () => {
  const location = useLocation();

  return (
    <AnimatePresence mode="wait">
      <Routes location={location} key={location.pathname}>
        <Route path='/' element={<App />} />
        <Route path='/books/:bookId' element={<ViewBook />} />
        <Route path='/create-book' element={<CreateBook />} />
        <Route path='/books/edit/:bookId' element={<EditBook />} />
      </Routes>
    </AnimatePresence>
  );
};

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <AnimatedRoutes />
    </BrowserRouter>
  </StrictMode>,
);
