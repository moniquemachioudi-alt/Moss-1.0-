
import React from 'react';
import { SignIn } from "@clerk/clerk-react";
import './LoginPage.css';

export default function LoginPage() {
    return (
        <div className="login-background">

            {/* Background video temporarily disabled */}

            {/* Dark Overlay for Readability */}
            <div className="video-overlay" />

            {/* Foreground Component */}
            <div className="login-card">
                <h1>Log into your Garden</h1>
                <div className="login-style">
                    <SignIn routing="hash" />
                </div>
            </div>

        </div>
    );
}
