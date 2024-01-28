import { Link } from "react-router-dom";
import Card from "../shared/Card";

const AboutPage = () => {
    return (
        <div className="h-screen">
            <Card reverse={true} centered={true} col={true} >
                <div className="p-4">
                    <h1 className="font-bold">About this project</h1>
                    <p>This is a react app project to leave feedback for a product or service</p>
                    <p>Version 1.0.0</p>
                    <Link to='/' className="text-yellow-400 hover:underline">Go Back</Link>
                </div>
            </Card>
        </div>
    );
}

export default AboutPage;