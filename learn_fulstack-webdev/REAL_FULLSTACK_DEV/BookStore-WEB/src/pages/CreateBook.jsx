import { useState } from 'react';
import { useNavigate, NavLink } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import styled from 'styled-components';
import Layout from '../components/Layout';
import Button from '../components/Button';

const FormContainer = styled(motion.div)`
  background-color: var(--secondary-bg);
  border-radius: 8px;
  padding: 2rem;
  box-shadow: var(--card-shadow);
  max-width: 800px;
  margin: 0 auto;
`;

const FormHeader = styled.div`
  margin-bottom: 2rem;
`;

const FormTitle = styled(motion.h1)`
  font-size: 2.5rem;
  margin-bottom: 1rem;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: var(--neon-blue-glow);
`;

const BackLink = styled(NavLink)`
  display: inline-block;
  margin-bottom: 1rem;
  font-family: var(--font-heading);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
`;

const StyledForm = styled(motion.form)`
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
`;

const FormGroup = styled(motion.div)`
  display: flex;
  flex-direction: column;
`;

const Label = styled.label`
  color: var(--text-secondary);
  font-family: var(--font-heading);
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
  text-transform: uppercase;
  letter-spacing: 1px;
`;

const Input = styled(motion.input)`
  background-color: rgba(26, 26, 46, 0.8);
  border: 1px solid var(--text-muted);
  border-radius: 4px;
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 1rem;
  padding: 0.75rem;
  transition: all var(--transition-fast);

  &:focus {
    border-color: var(--accent-blue);
    box-shadow: var(--neon-blue-glow);
    outline: none;
  }
`;

const Textarea = styled(motion.textarea)`
  background-color: rgba(26, 26, 46, 0.8);
  border: 1px solid var(--text-muted);
  border-radius: 4px;
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 1rem;
  padding: 0.75rem;
  transition: all var(--transition-fast);
  resize: vertical;
  min-height: 120px;

  &:focus {
    border-color: var(--accent-blue);
    box-shadow: var(--neon-blue-glow);
    outline: none;
  }
`;

const ErrorMessage = styled(motion.div)`
  color: var(--danger);
  background-color: rgba(255, 42, 109, 0.1);
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
  border-left: 3px solid var(--danger);
`;

const FormActions = styled(motion.div)`
  display: flex;
  justify-content: flex-end;
  gap: 1rem;
  margin-top: 1rem;

  @media (max-width: 480px) {
    flex-direction: column;
  }
`;

// Animation variants
const containerVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.5,
      when: "beforeChildren",
      staggerChildren: 0.1
    }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.3 }
  }
};

function CreateBook() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    Discription: '',
    Price: '',
    authour: '',
    genre: ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await fetch('http://localhost:5000/api/books', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create book');
      }

      const data = await response.json();
      console.log('Book created:', data);

      // Redirect to home page after successful creation
      navigate('/', {
        state: {
          notification: {
            type: 'success',
            message: 'Book created successfully'
          }
        }
      });
    } catch (err) {
      console.error('Error creating book:', err);
      setError(err.message || 'An error occurred while creating the book');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Layout>
      <FormContainer
        variants={containerVariants}
        initial="hidden"
        animate="visible"
      >
        <FormHeader>
          <BackLink to="/">← Back to Books</BackLink>
          <FormTitle variants={itemVariants}>Add New Book</FormTitle>
        </FormHeader>

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

        <StyledForm onSubmit={handleSubmit}>
          <FormGroup variants={itemVariants}>
            <Label htmlFor="name">Book Title</Label>
            <Input
              type="text"
              placeholder="Enter book title"
              id="name"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
              whileFocus={{ scale: 1.01 }}
              transition={{ duration: 0.2 }}
            />
          </FormGroup>

          <FormGroup variants={itemVariants}>
            <Label htmlFor="Discription">Description</Label>
            <Textarea
              id="Discription"
              name="Discription"
              placeholder="Enter book description"
              value={formData.Discription}
              onChange={handleChange}
              rows="5"
              required
              whileFocus={{ scale: 1.01 }}
              transition={{ duration: 0.2 }}
            />
          </FormGroup>

          <FormGroup variants={itemVariants}>
            <Label htmlFor="Price">Price</Label>
            <Input
              type="number"
              placeholder="Enter price"
              id="Price"
              name="Price"
              value={formData.Price}
              onChange={handleChange}
              required
              whileFocus={{ scale: 1.01 }}
              transition={{ duration: 0.2 }}
            />
          </FormGroup>

          <FormGroup variants={itemVariants}>
            <Label htmlFor="authour">Author</Label>
            <Input
              type="text"
              placeholder="Enter author name"
              id="authour"
              name="authour"
              value={formData.authour}
              onChange={handleChange}
              required
              whileFocus={{ scale: 1.01 }}
              transition={{ duration: 0.2 }}
            />
          </FormGroup>

          <FormGroup variants={itemVariants}>
            <Label htmlFor="genre">Genre</Label>
            <Input
              type="text"
              placeholder="Enter genre"
              id="genre"
              name="genre"
              value={formData.genre}
              onChange={handleChange}
              required
              whileFocus={{ scale: 1.01 }}
              transition={{ duration: 0.2 }}
            />
          </FormGroup>

          <FormActions variants={itemVariants}>
            <Button
              variant="secondary"
              type="button"
              onClick={() => navigate('/')}
            >
              Cancel
            </Button>
            <Button
              variant="primary"
              type="submit"
              disabled={loading}
            >
              {loading ? 'Creating...' : 'Create Book'}
            </Button>
          </FormActions>
        </StyledForm>
      </FormContainer>
    </Layout>
  );
}

export default CreateBook;