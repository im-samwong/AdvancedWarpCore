import useStore from "../store"; // Update the path as needed
import survivorImage from "../assets/survivor1.png";
import killerImage from "../assets/killer1.png";
import "./CharacterInput.css";

const CharacterInput = () => {
  const {
    setTime,
    setDay,
    setRankName,
    setRankNum,
    setModelType,
    setServer,
    setPartySize,
  } = useStore();

  const { isSurvivor } = useStore();

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    switch (name) {
      case "time":
        setTime(value);
        break;
      case "day":
        setDay(value);
        break;
      case "rankName":
        setRankName(value);
        break;
      case "rankNum":
        setRankNum(value);
        break;
      case "modelType":
        setModelType(value);
        break;
      case "server":
        setServer(value);
        break;
      case "partySize":
        setPartySize(value);
        break;
      default:
        break;
    }
  };

  return (
    <div className="charInput">
      <div className="inputCol">
        <div className="input-group">
          <label htmlFor="time">TIME:</label>
          <input
            type="time"
            id="time"
            name="time"
            className="otherInput"
            onChange={handleInputChange}
          />
        </div>
        <div className="input-group">
          <label htmlFor="day">DAY:</label>
          <select id="day" name="day" onChange={handleInputChange}>
            <option>Mon</option>
            <option>Tue</option>
            <option>Wed</option>
            <option>Thu</option>
            <option>Fri</option>
            <option>Sat</option>
            <option>Sun</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="rankName">RANK:</label>
          <div className="rankSelect">
            <select id="rankName" name="rankName" onChange={handleInputChange}>
              <option>Ash</option>
              <option>Bronze</option>
              <option>Silver</option>
              <option>Gold</option>
              <option>Iridescent</option>
            </select>
            <select id="rankNum" name="rankNum" onChange={handleInputChange}>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
            </select>
          </div>
        </div>
      </div>
      <div className="imageContainer">
        <img
          src={isSurvivor ? survivorImage : killerImage}
          alt="Character"
          className="centered-image"
        />
      </div>
      <div className="inputCol">
        <div className="input-group">
          <label htmlFor="partySize">MODEL TYPE:</label>
          <select id="partySize" name="modelType" onChange={handleInputChange}>
            <option>1</option>
            <option>2</option>
            <option>3</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="server">SERVER:</label>
          <select id="server" name="server" onChange={handleInputChange}>
            <option>us-west-2</option>
          </select>
        </div>
        <div className="input-group">
          <label htmlFor="partySize">PARTY SIZE:</label>
          <select id="partySize" name="partySize" onChange={handleInputChange}>
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
          </select>
        </div>
      </div>
    </div>
  );
};

export default CharacterInput;
