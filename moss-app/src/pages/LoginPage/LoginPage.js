import React from 'react';
import { SignIn } from "@clerk/clerk-react";
import './LoginPage.css';
<<<<<<< HEAD
import bgVideo from '../../videos/LoginPage_slow.mp4';
=======
// import bgVideo from '../../videos/LoginPage_slow.mp4';
// commented for now to test out stuff
>>>>>>> main

export default function LoginPage() {
    return(
        <div className="login-background">
            {/* The is the location of the Background Video */}
<<<<<<< HEAD
            <video autoPlay loop muted playsInline className="bg-video">
                <source src={bgVideo} type='video/mp4'/>
            </video>
=======

            {/* comment this out, since video file is too big */}
            {/* { <video autoPlay loop muted playsInline className="bg-video">
                <source src={bgVideo} type='video/mp4'/>
            </video> } */}
>>>>>>> main

            {/* Dark Overlay for Readability */}
            <div className="video-overlay" />
            
            {/* Foreground Component */}
            <div className='login-card'>
                <h1> Log into your Garden</h1>
                <div className="login-style">
                        <SignIn routing="hash" />
                </div>
            </div>
        </div>
    );
}