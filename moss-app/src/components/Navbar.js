
import { useState } from "react";
import { Link } from "react-router-dom";
import { SignOutButton } from "@clerk/clerk-react";

const Navbar = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <nav className="navbar">
            <button onClick={() => setIsOpen(!isOpen)}>
                {isOpen ? "Close" : "Menu"}
            </button>

            {isOpen && (
                <div className="links">
                    <Link to="/garden">My Garden</Link>
                    <br />

                    <Link to="/garden/create">New Plant</Link>
                    <br />

                    <Link to="/garden/modify">Modify Plant</Link>
                    <br />

                    <Link to="/garden/remove">Remove Plant</Link>
                    <br />

                    <SignOutButton>
                        <button>Sign Out</button>
                    </SignOutButton>
                </div>
            )}
        </nav>
    );
};

export default Navbar;
