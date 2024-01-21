import { useState } from 'react';
import myImage from "../assets/survivor1.png"; // Import the image


const CharacterInput = () => {
    return (
        <div className='charInput'>
            <div className="inputCol">
                <label for='location'>TIME:</label>
                <input type="time" id="time" name="time" />
                <label for='day'>DAY:</label>
                <select id='day' name='day'>
                    <option>Mon</option>
                    <option>Tue</option>
                    <option>Wed</option>
                    <option>Thu</option>
                    <option>Fri</option>
                    <option>Sat</option>
                    <option>Sun</option>
                </select>
                <label for='partySize'>PARTY SIZE:</label>
                <select id='partySize' name='partySize'>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                </select>
            </div>
            <img src={myImage} alt="Centered" className="centered-image" />
            <div className="inputCol">
            <label for='location'>TIME:</label>
                <input type="time" id="time" name="time" />
                <label for='day'>DAY:</label>
                <select id='day' name='day'>
                    <option>Mon</option>
                    <option>Tue</option>
                    <option>Wed</option>
                    <option>Thu</option>
                    <option>Fri</option>
                    <option>Sat</option>
                    <option>Sun</option>
                </select>
                <label for='partySize'>PARTY SIZE:</label>
                <select id='partySize' name='partySize'>
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
