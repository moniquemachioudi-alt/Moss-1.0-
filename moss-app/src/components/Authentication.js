import { SignIn } from "@clerk/clerk-react";

export default function LoginPage() {
    return(
        <div style={{
            display: 'flex',
            justifyContent:'center',
            alignItems:'center',
            height:'100vh',
            backgroundColor:'#f5f5f5'

        }}>
            <SignIn routing="hash" />
            </div>
    )
}