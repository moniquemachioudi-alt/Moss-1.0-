import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import './SoilMoisture.css';


export default function SoilMoisture(){

    return(
      <div className="SoilMoisture_pageContainer">

        <div className="SoilMoisture_header"> 
          <h1> Soil Moisture </h1>
          <p>This page will track how moist is the soil of the plant, therefore indicating the amount of watering needed </p>
        </div>


        <div className="graph-container"> 
          <h2>Soil Moisture tracker  </h2>
          <p>This is the graph showing the moisture as a function of time </p>
        </div>


          
      </div>



      
      
      
    );

    

}




