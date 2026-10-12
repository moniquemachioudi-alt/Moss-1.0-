import React from 'react';
import { SignUp } from "@clerk/clerk-react";
import './SIgnUpPage.css';
// import bgVideo from '../../videos/LoginPage_slow.mp4';
// comment out for now to test out stuff

export default function SignUpPage() {
    return(
        <div className="signup-background">
            {/*The is the location of the Background Video */}

            {/* comment this out, since video file is too big
            <video autoPlay loop muted playsInline className="bg-video">
                <source src={bgVideo} type='video/mp4'/>
            </video> */}

            {/* Dark Overlay for Readability */}
            <div className="video-overlay" />
            
            {/* Foreground Component */}
            <div className='signup-card'>
                <h1> Create your Garden</h1>
                <div className="signup-style">
                        <SignUp routing="path" path="https://singular-dove-5.accounts.dev//sign-up" />
                </div>
            </div>
        </div>
    );
}