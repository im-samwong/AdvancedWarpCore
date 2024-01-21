// TestComponent.js
import { useState } from 'react';
import './PlayButton.css';
import useStore from '../store';
import { convertRankName, convertRankNum, convertPlayer, convertModelType } from '../store';

const PlayButton = () => {
  const [isHovered, setHovered] = useState(false);

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
    isSurvivor
  } = useStore();

  const handlePlay = async () => {
    const rank = convertRankName(rankName) + convertRankNum(rankNum);
    const playerType = convertPlayer(isSurvivor);

    const data = {
      MATCHMAKING_ATTEMPT_START_TIME_UTC: time,
      MATCHMAKING_DAY_OF_WEEK: day,
      PLAYER_ROLE: playerType,
      PARTY_SIZE: partySize,
      SERVER_NAME: server,
      MATCHMAKING_OUTCOME: "success",
      MMR_GROUP_DECILE: rank
    };

    console.log(data);

    const modelTypeCode = convertModelType(modelType);
    const urls = {
      "1": "http://127.0.0.1:5000/predict",
      "2": "http://127.0.0.1:5000/predict1",
      "3": "http://127.0.0.1:5000/predict2",
      // Add more URLs as needed
    };

    const url = urls[modelTypeCode];
    if (url) {
      try {
        const response = await fetch(url, {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(data)
        });

        if (response.ok) {
          const result = await response.json();
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
        className={`color-transition-button ${isHovered ? 'hovered' : ''}`}
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        onClick={handlePlay}
      >
        <span>PLAY</span>
      </button>
    </div>
  );
};

export default PlayButton;
