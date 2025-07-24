import { motion } from 'framer-motion';
import { NavLink } from 'react-router-dom';
import styled from 'styled-components';

const StyledHeader = styled.header`
  background-color: var(--secondary-bg);
  padding: 1.5rem 2rem;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  position: relative;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }
`;

const Logo = styled(motion.h1)`
  margin-bottom: 0;
  font-size: 2rem;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  text-shadow: var(--neon-blue-glow);
`;

const Nav = styled.nav`
  display: flex;
  gap: 1.5rem;
`;

const StyledNavLink = styled(NavLink)`
  font-family: var(--font-heading);
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0.5rem 0;
  color: var(--text-secondary);
  position: relative;
  
  &.active {
    color: var(--accent-blue);
    text-shadow: var(--neon-blue-glow);
  }
  
  &::after {
    content: '';
    position: absolute;
    width: 0;
    height: 2px;
    bottom: -2px;
    left: 0;
    background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple));
    transition: width var(--transition-medium);
  }
  
  &:hover::after, &.active::after {
    width: 100%;
  }
`;

const Main = styled(motion.main)`
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
`;

const Footer = styled.footer`
  background-color: var(--secondary-bg);
  padding: 1.5rem 2rem;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-top: 3rem;
`;

// Animation variants
const pageVariants = {
  initial: {
    opacity: 0,
    y: 20
  },
  animate: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.4,
      ease: "easeInOut"
    }
  },
  exit: {
    opacity: 0,
    y: -20,
    transition: {
      duration: 0.3,
      ease: "easeInOut"
    }
  }
};

const logoVariants = {
  initial: { scale: 0.9 },
  animate: { 
    scale: 1,
    transition: {
      duration: 0.5,
      yoyo: Infinity,
      ease: "easeInOut"
    }
  }
};

const Layout = ({ children }) => {
  return (
    <>
      <StyledHeader>
        <Logo
          variants={logoVariants}
          initial="initial"
          animate="animate"
        >
          CyberBooks
        </Logo>
        <Nav>
          <StyledNavLink to="/">Home</StyledNavLink>
          <StyledNavLink to="/create-book">Add Book</StyledNavLink>
        </Nav>
      </StyledHeader>
      
      <Main
        variants={pageVariants}
        initial="initial"
        animate="animate"
        exit="exit"
      >
        {children}
      </Main>
      
      <Footer>
        &copy; {new Date().getFullYear()} CyberBooks - A Futuristic BookStore Experience
      </Footer>
    </>
  );
};

export default Layout;
