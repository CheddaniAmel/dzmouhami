const Card = ({ children, reverse, centered, col }) => {
    return (
        <div
            className={`flex ${col ? 'flex-col' : ''} ${centered ? 'justify-center items-center' : 'justify-between'}
             ${reverse ? 'bg-violet-950 text-white' : 'bg-white'} 
            w-full rounded-3xl my-3 relative`}>
            {children}
        </div>
    );
}

export default Card;