// TestComponent.js
import { useState } from "react";
import "./PlayButton.css";
import useStore from "../store";

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const {
    setTime,
    setDay,
    setRankName,
    setRankNum,
    setModelType,
    setServer,
    partySize,
  } = useStore();

  return (
    <div>
      <button
        className={`color-transition-button  ${isHovered ? "hovered" : ""}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
      >
        <span>PLAY</span>
      </button>
    </div>
  );
};

export default PlayButton;
