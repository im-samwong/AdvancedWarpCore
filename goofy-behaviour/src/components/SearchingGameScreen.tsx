import React from "react";
import useStore from "../store"; // Import the useStore hook from your Zustand store
import "./SearchingGameScreen.css"; // Import your CSS styles for the joining-game-screen

const SearchingGameScreen = () => {
  // Use the useStore hook to access the estimatedTime state
  const { estimatedTime, setJoiningGameState } = useStore();

  const handleCancelClick = () => {
    // Implement your cancel logic here
    setJoiningGameState(false);
  };

  return (
    <div className="joining-game-screen">
      <span>Joining Game</span>
      <span>Estimated Time: {estimatedTime} seconds</span>
      <button className="cancel-button" onClick={handleCancelClick}>
        Cancel
      </button>
    </div>
  );
};

export default SearchingGameScreen;
