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

  const handleStartQueue =  async () => {

};
  const {
    time,
    day,
    rankName,
    rankNum,
    modelType,
    server,
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
