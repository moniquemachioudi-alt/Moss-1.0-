import React from 'react';
import { SignIn } from "@clerk/clerk-react";
import './LoginPage.css';
// import bgVideo from '../../videos/LoginPage_slow.mp4';
// commented for now to test out stuff

export default function LoginPage() {
    return(
        <div className="login-background">
            {/* The is the location of the Background Video */}

            {/* comment this out, since video file is too big */}
            {/* { <video autoPlay loop muted playsInline className="bg-video">
                <source src={bgVideo} type='video/mp4'/>
            </video> } */}

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