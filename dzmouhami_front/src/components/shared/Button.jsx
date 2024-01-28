import PropTypes from 'prop-types'

const Button = ({ children, type, isDisabled }) => {
    return (
        <button type={type} disabled={isDisabled}
         className={`rounded-md
          ${isDisabled ? 'bg-gray-500 border-none' : 'bg-[#800020] text-white'} 
           py-2 px-4 hover:opacity-90`}>
            {children}
        </button>
    );
}

Button.defaultProps = {
    type: 'button',
    isDisabled: 'false'
} 

Button.propTypes = {
    children : PropTypes.node.isRequired,
    type : PropTypes.string,
    version : PropTypes.bool,
}

export default Button;