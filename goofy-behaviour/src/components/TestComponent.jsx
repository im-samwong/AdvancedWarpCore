
// TestComponent.js
import React, { useState } from 'react';
import './TestComponent.css';

const TestComponent = () => {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  return (
    <div className='btn'>
        <button
        className={`color-transition-button ${isHovered ? 'hovered' : ''}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        >
        Hover Me
        </button>
    </div>

  );
};

export default TestComponent;
