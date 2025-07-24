import { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import styled from 'styled-components';
import Layout from './components/Layout';
import BookCard from './components/BookCard';
import LoadingSpinner from './components/LoadingSpinner';
import Button from './components/Button';
import { NavLink } from 'react-router-dom';

const HomeHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
`;

const Title = styled(motion.h2)`
  font-size: 2rem;
  margin: 0;
`;

const BookGrid = styled(motion.div)`
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;

  @media (max-width: 768px) {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  @media (max-width: 480px) {
    grid-template-columns: 1fr;
  }
`;

const EmptyState = styled(motion.div)`
  text-align: center;
  padding: 3rem;
  background-color: var(--secondary-bg);
  border-radius: 8px;
  margin-top: 2rem;
`;

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

function App() {
  const [books, setBooks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const listBooks = async() => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:5000/api/books');

      if (!response.ok) {
        throw new Error('Failed to fetch books');
      }

      const data = await response.json();
      setBooks(data.books || []);
    } catch (err) {
      console.error('Error fetching books:', err);
      setError(err.message || 'An error occurred while fetching books');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    listBooks();
  }, []);

  return (
    <Layout>
      <HomeHeader>
        <Title
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
        >
          Explore Books
        </Title>
        <NavLink to="/create-book">
          <Button
            variant="primary"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Add New Book
          </Button>
        </NavLink>
      </HomeHeader>

      {loading ? (
        <LoadingSpinner message="Loading Books" />
      ) : error ? (
        <EmptyState
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h3>Error</h3>
          <p>{error}</p>
          <Button
            variant="primary"
            onClick={listBooks}
            style={{ marginTop: '1rem' }}
          >
            Try Again
          </Button>
        </EmptyState>
      ) : books && books.length > 0 ? (
        <BookGrid
          variants={containerVariants}
          initial="hidden"
          animate="visible"
        >
          {books.map((book, index) => (
            <BookCard key={book._id} book={book} index={index} />
          ))}
        </BookGrid>
      ) : (
        <EmptyState
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h3>No Books Found</h3>
          <p>Start by adding your first book to the collection.</p>
          <NavLink to="/create-book">
            <Button
              variant="primary"
              style={{ marginTop: '1rem' }}
            >
              Add Book
            </Button>
          </NavLink>
        </EmptyState>
      )}
    </Layout>
  );
}

export default App;
