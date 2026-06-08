import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import './SunLight.css';


export default function SunLight(){

    return(
      <div className="SunLight_pageContainer">

        <div className="SunLight_header"> 
          <h1> Sunlight </h1>
          <p>This page will track the amount of sunight your current plant is receiving </p>
        </div>


        <div className="graph-container"> 
          <h2>Sun Light tracker  </h2>
          <p>This is the graph showing the fluctuation of sunlight as a function of time </p>
        </div>


          
      </div>



      
      
      
    );

    

}




