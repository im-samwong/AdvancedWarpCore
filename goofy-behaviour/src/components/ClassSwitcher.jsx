import "./ClassSwitcher.css";
import useStore from "../store"; // Update the path to your store

const ClassSwitcher = () => {
  const { isSurvivor, toggleClass } = useStore();

  console.log("isSurvivor: ", isSurvivor);

  if (!isSurvivor) {
    const arrow = document.querySelector(".class-switcher .arrow");
    arrow.classList.toggle("rotated");
  }

  return (
    <div className="class-switcher" onClick={toggleClass}>
      <span className={isSurvivor ? "active" : ""}>SURVIVOR</span>
      <span className={`arrow ${isSurvivor ? "rotated" : ""}`}>&rarr;</span>
      <span className={!isSurvivor ? "active" : ""}>KILLER</span>
    </div>
  );
};

export default ClassSwitcher;
