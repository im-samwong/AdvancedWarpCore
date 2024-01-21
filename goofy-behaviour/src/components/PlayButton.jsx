// TestComponent.js
import { useState } from "react";
import useStore from "../store";
import "./PlayButton.css";

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const { isSurvivor, time, day, rankName, rankNum, modelType, server, partySize } = useStore();

  const handlePlayClick = () => {
    console.log("Here is the request data: ", {
      isSurvivor,
      time,
      day,
      rankName,
      rankNum,
      modelType,
      server,
      partySize,
    });
    };


  return (
    <div>
      <button
        className={`color-transition-button ${isHovered ? "hovered" : ""}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        onClick={handlePlayClick}
      >
        <span>PLAY</span>
      </button>
    </div>
  );
};

export default PlayButton;
