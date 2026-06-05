import { useClerk, UserButton, useUser } from "@clerk/clerk-react";



const Navbar = () => {
    return (  
        <nav className ="navbar">
            <h1>Moss</h1>
            <div className="links">
                <a href="/">MyGarden</a>
                <a href="/create"> New Device</a>
                <a href="/modify">New Plant</a>
                <a href="/remove">Remove Device</a>
                {
                    !user ? (<button onClick={openSignIn} className="Login">
                        Login
                        </button>
                    ) : (
                        <UserButton></UserButton>
                    )
                }
            </div>
        </nav>
    );
}
 
const {user} = useUser();
const {openSignIn} = useClerk();
export default Navbar;