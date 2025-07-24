import { motion } from 'framer-motion';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';
import Button from './Button';

const Card = styled(motion.div)`
  background-color: var(--card-bg);
  border-radius: 8px;
  box-shadow: var(--card-shadow);
  overflow: hidden;
  position: relative;
  z-index: 1;
  padding: 1.5rem;
  height: 100%;
  display: flex;
  flex-direction: column;
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, var(--accent-blue), var(--accent-purple));
    opacity: 0;
    z-index: -1;
    transition: opacity var(--transition-medium);
  }
  
  &:hover::before {
    opacity: 0.05;
  }
`;

const Title = styled.h2`
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);
  
  &::after {
    content: '';
    display: block;
    width: 50px;
    height: 2px;
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
    margin-top: 0.5rem;
  }
`;

const Description = styled.p`
  color: var(--text-secondary);
  margin-bottom: 0.5rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
`;

const Price = styled.p`
  color: var(--accent-yellow);
  font-weight: bold;
  font-size: 1.2rem;
  margin: 0.5rem 0;
`;

const Author = styled.p`
  color: var(--text-secondary);
  font-style: italic;
`;

const Genre = styled.span`
  display: inline-block;
  background-color: rgba(0, 240, 255, 0.1);
  color: var(--accent-blue);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.8rem;
  margin-top: 0.5rem;
`;

const Actions = styled.div`
  display: flex;
  gap: 0.5rem;
  margin-top: auto;
  padding-top: 1rem;
`;

const StyledNavLink = styled(NavLink)`
  text-decoration: none;
  color: inherit;
  display: block;
  width: 100%;
`;

// Animation variants
const cardVariants = {
  hidden: { 
    opacity: 0,
    y: 20
  },
  visible: (custom) => ({
    opacity: 1,
    y: 0,
    transition: {
      delay: custom * 0.1,
      duration: 0.5,
      ease: "easeOut"
    }
  }),
  hover: {
    y: -10,
    boxShadow: "0 0 10px rgba(0, 240, 255, 0.5), 0 0 20px rgba(0, 240, 255, 0.3)",
    transition: {
      duration: 0.3,
      ease: "easeOut"
    }
  }
};

const BookCard = ({ book, index }) => {
  return (
    <Card
      variants={cardVariants}
      initial="hidden"
      animate="visible"
      whileHover="hover"
      custom={index}
      layoutId={`book-${book._id}`}
    >
      <Title>{book.name}</Title>
      <Description>{book.Discription}</Description>
      <Price>${book.Price}</Price>
      <Author>By {book.authour}</Author>
      <Genre>{book.genre}</Genre>
      
      <Actions>
        <StyledNavLink to={`/books/${book._id}`}>
          <Button variant="primary">View Details</Button>
        </StyledNavLink>
      </Actions>
    </Card>
  );
};

export default BookCard;
