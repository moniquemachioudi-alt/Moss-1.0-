import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import './AtmoHumidity.css';


export default function AtmoHumidity(){

    return(
      <div className="Humidity_pageContainer">

        <div className="Humidity_header"> 
          <h1> Humidity </h1>
          <p>This page will track the amount of humidity your current plant is receiving </p>
        </div>


        <div className="graph-container"> 
          <h2>Humidity </h2>
          <p>This is the graph showing the room's humidity as a function of time </p>
        </div>


          
      </div>



      
      
      
    );

    

}




