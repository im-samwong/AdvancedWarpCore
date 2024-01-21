// TestComponent.js
import { useState } from "react";
import useStore from "../store";
import "./PlayButton.css";
import { convertModelType, convertRankName, convertRankNum } from "../store";

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);
  const [isQueingUp, setIsQueuingUp] = useState(false);
  const [estimatedTime, setEstimatedTime] = useState(0)

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
      <button
        className={`color-transition-button  ${isHovered ? "hovered" : ""}`}
        style={{display:"none"}}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        
      >
        <span>CANCEL QUEUE</span>
        <span>{estimatedTime}</span>
      </button>
    </div>
  );
};

export default PlayButton;
