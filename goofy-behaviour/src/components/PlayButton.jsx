// TestComponent.js
import { useState } from "react";
import "./PlayButton.css";

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  return (
    <div className="btn">
      <button
        className={`color-transition-button ${isHovered ? "hovered" : ""}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
      >
        <span>Hover Me</span>
      </button>
    </div>
  );
};

export default PlayButton;
