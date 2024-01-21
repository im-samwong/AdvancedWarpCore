import myImage from "../assets/survivor1.png"; // Import the image

const CharacterInput = () => {
  return (
    <div className="charInput">
      <div className="inputCol">
        <label htmlFor="location">TIME:</label>
        <input type="time" id="time" name="time" className="otherInput" />
        <label htmlFor="day">DAY:</label>
        <select id="day" name="day">
          <option>Mon</option>
          <option>Tue</option>
          <option>Wed</option>
          <option>Thu</option>
          <option>Fri</option>
          <option>Sat</option>
          <option>Sun</option>
        </select>
        <label htmlFor="rankName">RANK:</label>
        <div className="rankSelect">
            <select id="rankName" name="rankName">
                <option>Ash</option>
                <option>Bronze</option>
                <option>Silver</option>
                <option>Gold</option>
                <option>Iridescent</option>
            </select>
            <select id="rankNum" name="rankNum">
            <option>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            </select>
        </div>
      </div>
      <img src={myImage} alt="Centered" className="centered-image" />
      <div className="inputCol">
        <label htmlFor="modelType">MODEL TYPE:</label>
        <div className="otherInput">
            <label>
                <input type="radio" name="modelType" value="1" className="modelTypeSelect" />
                1
                <input type="radio" name="modelType" value="2" className="modelTypeSelect" />
                2
                <input type="radio" name="modelType" value="3" className="modelTypeSelect" />
                3
            </label>
        </div>
        <label htmlFor="server">SERVER:</label>
        <select id="server" name="server">
          <option>us-west-2</option>
        </select>
        <label htmlFor="partySize">PARTY SIZE:</label>
        <select id="partySize" name="partySize">
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
        </select>
      </div>
    </div>
  );
};

export default CharacterInput;
