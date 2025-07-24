import { useEffect, useState } from 'react';
import { useParams, NavLink, useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import styled from 'styled-components';
import Layout from '../components/Layout';
import Button from '../components/Button';
import LoadingSpinner from '../components/LoadingSpinner';

const BookDetailsContainer = styled(motion.div)`
  background-color: var(--secondary-bg);
  border-radius: 8px;
  padding: 2rem;
  box-shadow: var(--card-shadow);
  max-width: 800px;
  margin: 0 auto;
`;

const BookHeader = styled.div`
  margin-bottom: 2rem;
  position: relative;
`;

const BackLink = styled(NavLink)`
  display: inline-block;
  margin-bottom: 1rem;
  font-family: var(--font-heading);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
`;

const BookTitle = styled(motion.h1)`
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: var(--neon-blue-glow);
`;

const BookInfo = styled.div`
  margin-bottom: 2rem;
`;

const Description = styled(motion.p)`
  color: var(--text-secondary);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
  padding-left: 1rem;
  border-left: 2px solid var(--accent-blue);
`;

const InfoItem = styled(motion.div)`
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
`;

const Label = styled.span`
  color: var(--text-muted);
  width: 100px;
`;

const Value = styled.span`
  color: var(--text-primary);
  font-weight: 500;
`;

const Genre = styled(motion.span)`
  display: inline-block;
  background-color: rgba(0, 240, 255, 0.1);
  color: var(--accent-blue);
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  margin-top: 0.5rem;
`;

const Price = styled(motion.div)`
  font-size: 1.5rem;
  color: var(--accent-yellow);
  font-weight: bold;
  margin: 1.5rem 0;
`;

const Actions = styled(motion.div)`
  display: flex;
  gap: 1rem;
  margin-top: 2rem;

  @media (max-width: 480px) {
    flex-direction: column;
  }
`;

const ErrorMessage = styled(motion.div)`
  color: var(--danger);
  background-color: rgba(255, 42, 109, 0.1);
  padding: 0.75rem;
  border-radius: 4px;
  margin: 1rem 0;
  border-left: 3px solid var(--danger);
`;

const DeleteConfirmation = styled(motion.div)`
  background-color: var(--card-bg);
  padding: 1.5rem;
  border-radius: 8px;
  margin-top: 1.5rem;
  border: 1px solid var(--danger);
  box-shadow: var(--neon-pink-glow);
`;

const ConfirmActions = styled.div`
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
  justify-content: flex-end;
`;

function ViewBook() {
  const [book, setBook] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showDeleteConfirm, setShowDeleteConfirm] = useState(false);
  const [deleting, setDeleting] = useState(false);
  const { bookId } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBook = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://localhost:5000/api/books/${bookId}`);
        if (!response.ok) {
          throw new Error('Book not found');
        }
        const data = await response.json();
        setBook(data.book);
      } catch (error) {
        console.error('Error fetching book:', error);
        setError(error.message || 'Failed to load book details');
      } finally {
        setLoading(false);
      }
    };

    fetchBook();
  }, [bookId]);

  const deleteBook = async () => {
    try {
      setDeleting(true);
      setError('');
      const response = await fetch(`http://localhost:5000/api/books/${bookId}`, {
        method: 'DELETE'
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.message || 'Failed to delete book');
      }

      console.log("Book deleted successfully");

      // Navigate to home page after successful deletion
      navigate('/', {
        state: {
          notification: {
            type: 'success',
            message: 'Book deleted successfully'
          }
        }
      });
    } catch (error) {
      console.error('Error deleting book:', error);
      setError(error.message || 'An error occurred while deleting the book');
      setShowDeleteConfirm(false);
    } finally {
      setDeleting(false);
    }
  };

  const navigateToEdit = () => {
    navigate(`/books/edit/${bookId}`);
  };

  if (loading) {
    return (
      <Layout>
        <LoadingSpinner message="Loading Book Details" />
      </Layout>
    );
  }

  if (!book) {
    return (
      <Layout>
        <BookDetailsContainer
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h2>Book Not Found</h2>
          <p>The book you're looking for doesn't exist or has been removed.</p>
          <NavLink to="/">
            <Button variant="primary" style={{ marginTop: '1rem' }}>
              Back to Books
            </Button>
          </NavLink>
        </BookDetailsContainer>
      </Layout>
    );
  }

  return (
    <Layout>
      <BookDetailsContainer
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <BookHeader>
          <BackLink to="/">← Back to Books</BackLink>
          <BookTitle
            initial={{ opacity: 0, y: -20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2, duration: 0.5 }}
          >
            {book.name}
          </BookTitle>
        </BookHeader>

        <BookInfo>
          <Description
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3, duration: 0.5 }}
          >
            {book.Discription}
          </Description>

          <InfoItem
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4, duration: 0.5 }}
          >
            <Label>Author:</Label>
            <Value>{book.authour}</Value>
          </InfoItem>

          <InfoItem
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.5, duration: 0.5 }}
          >
            <Label>Genre:</Label>
            <Value>
              <Genre
                whileHover={{ scale: 1.05 }}
                transition={{ duration: 0.2 }}
              >
                {book.genre}
              </Genre>
            </Value>
          </InfoItem>

          <Price
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.6, duration: 0.5 }}
          >
            ${book.Price}
          </Price>
        </BookInfo>

        <AnimatePresence>
          {error && (
            <ErrorMessage
              initial={{ opacity: 0, y: -10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -10 }}
              transition={{ duration: 0.3 }}
            >
              {error}
            </ErrorMessage>
          )}
        </AnimatePresence>

        <Actions
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.7, duration: 0.5 }}
        >
          <Button
            variant="primary"
            onClick={navigateToEdit}
          >
            Edit Book
          </Button>
          <Button
            variant="danger"
            onClick={() => setShowDeleteConfirm(true)}
          >
            Delete Book
          </Button>
        </Actions>

        <AnimatePresence>
          {showDeleteConfirm && (
            <DeleteConfirmation
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 20 }}
              transition={{ duration: 0.3 }}
            >
              <h3>Confirm Deletion</h3>
              <p>Are you sure you want to delete "{book.name}"? This action cannot be undone.</p>
              <ConfirmActions>
                <Button
                  variant="secondary"
                  onClick={() => setShowDeleteConfirm(false)}
                  disabled={deleting}
                >
                  Cancel
                </Button>
                <Button
                  variant="danger"
                  onClick={deleteBook}
                  disabled={deleting}
                >
                  {deleting ? 'Deleting...' : 'Yes, Delete'}
                </Button>
              </ConfirmActions>
            </DeleteConfirmation>
          )}
        </AnimatePresence>
      </BookDetailsContainer>
    </Layout>
  );
}

export default ViewBook;
