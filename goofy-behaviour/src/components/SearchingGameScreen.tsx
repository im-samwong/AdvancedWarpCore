import React, { useState, useEffect } from "react";
import useStore from "../store"; // Import the useStore hook from your Zustand store
import "./SearchingGameScreen.css"; // Import your CSS styles for the joining-game-screen

const SearchingGameScreen = () => {
  // Use the useStore hook to access the estimatedTime state
  const { estimatedTime, setJoiningGameState } = useStore();

  const handleCancelClick = () => {
    // Implement your cancel logic here
    setJoiningGameState(false);
  };

  const [ellipsis, setEllipsis] = useState("");

  useEffect(() => {
    const intervalId = setInterval(() => {
      setEllipsis((prevEllipsis) => {
        if (prevEllipsis.length < 3) return prevEllipsis + ".";
        return "";
      });
    }, 500); // Update every 500ms

    return () => clearInterval(intervalId); // Clear interval on component unmount
  }, []);

  return (
    <div className="joining-game-screen">
      <span className="searching-text">Searching for game{ellipsis}</span>
      <span>Estimated Time: {estimatedTime} seconds</span>
      <button className="cancel-button" onClick={handleCancelClick}>
        Cancel
      </button>
    </div>
  );
};

export default SearchingGameScreen;
