import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import './MyGarden.css';

// importing the subpages
import Sunlight from './SunLightPage/SunLight';
import SoilMoisture from './SoilMoisturePage/SoilMoisture';
import Humidity from './AtmoHumidityPage/AtmoHumidity';
import Temp from './TempPage/Temp';





export default function MyGarden(){

    return(
      <div className="MyGarden_pageContainer">



        <div className="myGarden_header"> 
          <h1> My Garden </h1>
          <p>This main page contains the almagam of all your plants! </p>
        </div>



        <div className="boxes-container"> 
          <Link to="/garden/sunlight" className="link-box"> Sun Light </Link>
          <Link to="/garden/soilMoisture" className="link-box"> Soil Moisture </Link>
          <Link to="/garden/humidity" className="link-box"> Humidity </Link>  {/* this is the atmospheric Humidity */}
          <Link to="/garden/temperature" className="link-box"> Temperature  </Link> 
        </div>


        <div className="chatbox-container"> 
          <h2>Your assistant Bloom </h2>
          <p>Chat with Bloom for any question you might have! </p>

        </div>


          
      </div>



      
      
      
    );

    

}


