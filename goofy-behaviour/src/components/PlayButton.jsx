// TestComponent.js
import { useState } from "react";
import "./PlayButton.css";
import useStore from "../store";
import {
  convertRankName,
  convertRankNum,
  convertPlayer,
  convertModelType,
} from "../store";

function convertSecondsToMinutes(seconds) {
  const fullMinutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.round(seconds % 60);

  // Formatting the output to ensure two digits for seconds
  const formattedSeconds = remainingSeconds < 10 ? `0${remainingSeconds}` : remainingSeconds;

  return `${fullMinutes}:${formattedSeconds}`;
}

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);
  const { setJoiningGameState, estimatedTime, setEstimatedTime } = useStore();

  const handleMouseEnter = () => {
    setHovered(true);
  };

  const handleMouseLeave = () => {
    setHovered(false);
  };

  const {
    time,
    day,
    rankName,
    rankNum,
    modelType,
    server,
    partySize,
    isSurvivor,
  } = useStore();

  const handlePlay = async () => {
    setJoiningGameState(true)
    const rank = convertRankName[rankName] + convertRankNum[rankNum];
    const playerType = convertPlayer[isSurvivor];

    const data = {
      MATCHMAKING_ATTEMPT_START_TIME_UTC: time,
      MATCHMAKING_DAY_OF_WEEK: day,
      PLAYER_ROLE: playerType,
      PARTY_SIZE: partySize,
      SERVER_NAME: server,
      MATCHMAKING_OUTCOME: "success",
      MMR_GROUP_DECILE: rank,
    };

    console.log(data);

    const modelTypeCode = convertModelType[modelType];

    const urls = {
      "0": "http://127.0.0.1:5000/predict",
      "1": "http://127.0.0.1:5000/predict1",
      "2": "http://127.0.0.1:5000/predict2",
    };

    const url = urls[modelTypeCode];
    if (url) {
      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        });

        if (response.ok) {
          const result = await response.json();
          const timeInMinutes = convertSecondsToMinutes(result.predictions[0]);

          setEstimatedTime(timeInMinutes)
          console.log(result); // Handle the result as needed


        } else {
          console.error("Error in response", response.status);
        }
      } catch (error) {
        console.error("Error making the request", error);
      }
    }
  };

  return (
    <div>
      <button
        className={`color-transition-button ${isHovered ? "hovered" : ""}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        onClick={handlePlay}
      >
        <span>PLAY</span>
      </button>
      <button
        className={`color-transition-button  ${isHovered ? "hovered" : ""}`}
        style={{ display: "none" }}
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
