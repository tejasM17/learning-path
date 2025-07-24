import { motion } from 'framer-motion';
import styled from 'styled-components';

const SpinnerContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 200px;
  flex-direction: column;
  gap: 1rem;
`;

const Spinner = styled(motion.div)`
  width: 50px;
  height: 50px;
  border: 3px solid rgba(0, 240, 255, 0.3);
  border-radius: 50%;
  border-top-color: var(--accent-blue);
`;

const LoadingText = styled(motion.p)`
  color: var(--accent-blue);
  font-family: var(--font-heading);
  letter-spacing: 2px;
  text-transform: uppercase;
  font-size: 0.9rem;
`;

const spinTransition = {
  repeat: Infinity,
  ease: "linear",
  duration: 1
};

const textVariants = {
  animate: {
    opacity: [0.5, 1, 0.5],
    transition: {
      repeat: Infinity,
      duration: 1.5,
      ease: "easeInOut"
    }
  }
};

const LoadingSpinner = ({ message = "Loading" }) => {
  return (
    <SpinnerContainer>
      <Spinner
        animate={{ rotate: 360 }}
        transition={spinTransition}
      />
      <LoadingText
        variants={textVariants}
        animate="animate"
      >
        {message}
      </LoadingText>
    </SpinnerContainer>
  );
};

export default LoadingSpinner;
