import { motion } from 'framer-motion';
import styled from 'styled-components';

const StyledButton = styled(motion.button)`
  font-family: var(--font-heading);
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 1px;
  padding: 0.75rem 1.5rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  background-color: ${props => {
    if (props.variant === 'primary') return 'var(--accent-blue)';
    if (props.variant === 'danger') return 'var(--danger)';
    if (props.variant === 'success') return 'var(--success)';
    if (props.variant === 'warning') return 'var(--warning)';
    if (props.variant === 'secondary') return 'transparent';
    return 'var(--accent-blue)';
  }};
  color: ${props => {
    if (props.variant === 'primary') return 'var(--primary-bg)';
    if (props.variant === 'secondary') return 'var(--accent-blue)';
    return 'var(--text-primary)';
  }};
  border: ${props => props.variant === 'secondary' ? '1px solid var(--accent-blue)' : 'none'};
  box-shadow: ${props => {
    if (props.variant === 'primary') return 'var(--neon-blue-glow)';
    if (props.variant === 'danger') return 'var(--neon-pink-glow)';
    if (props.variant === 'secondary') return 'none';
    return 'none';
  }};
  
  &:hover {
    background-color: ${props => {
      if (props.variant === 'primary') return 'var(--accent-purple)';
      if (props.variant === 'danger') return '#ff0055';
      if (props.variant === 'success') return '#00cc7a';
      if (props.variant === 'warning') return '#e6a800';
      if (props.variant === 'secondary') return 'rgba(0, 240, 255, 0.1)';
      return 'var(--accent-purple)';
    }};
    box-shadow: ${props => {
      if (props.variant === 'primary') return 'var(--neon-purple-glow)';
      if (props.variant === 'danger') return 'var(--neon-pink-glow)';
      if (props.variant === 'secondary') return 'var(--neon-blue-glow)';
      return 'var(--neon-purple-glow)';
    }};
  }
  
  &:disabled {
    background-color: var(--text-muted);
    color: var(--text-secondary);
    cursor: not-allowed;
    box-shadow: none;
  }
  
  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: all var(--transition-fast);
  }
  
  &:hover::before {
    left: 100%;
  }
`;

const Button = ({ 
  children, 
  variant = 'primary', 
  disabled = false,
  onClick,
  type = 'button',
  ...props 
}) => {
  return (
    <StyledButton
      variant={variant}
      disabled={disabled}
      onClick={onClick}
      type={type}
      whileHover={{ scale: disabled ? 1 : 1.05 }}
      whileTap={{ scale: disabled ? 1 : 0.95 }}
      transition={{ duration: 0.2 }}
      {...props}
    >
      {children}
    </StyledButton>
  );
};

export default Button;
