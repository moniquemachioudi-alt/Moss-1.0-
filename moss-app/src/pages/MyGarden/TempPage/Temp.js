import React, { useState } from 'react';
import { Link } from 'react-router-dom';

import './Temp.css';


export default function Temp(){

    return(
      <div className="Temp_pageContainer">

        <div className="Temp_header"> 
          <h1> Temperature </h1>
          <p>This page will track the temperature of the room you plant is currently sitting in </p>
        </div>


        <div className="graph-container"> 
          <h2>Temperature </h2>
          <p>This is the graph showing the fluctuation of the room temperature as a function of time </p>
        </div>


          
      </div>



      
      
      
    );

    

}




