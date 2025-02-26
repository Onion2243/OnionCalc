
class onioncolors:
    # Pre Select Color Function Using Text Colors
    def text_color(color):
        if color == "red" or color == "Red":
            return "\033[31m"
    
        if color == "orange" or color == "Orange":
            return "\033[38;5;214m"
    
        if color == "green" or color == "Green":
            return "\033[32m"
    
        if color == "yellow" or color == "Yellow":
            return "\033[33m"
    
        if color == "blue" or color == "Blue":
            return "\033[34m"
    
        if color == "cyan" or color == "Cyan":
            return "\033[36m"
    
        if color == "magenta" or color == "Magenta":
            return "\033[35m"
    
        if color == "white" or color == "White":
            return "\033[38;2;255;255;255m"
    
        if color == "black" or color == "Black":
            return "\033[30m"
    
        if color == "gray" or color == "Gray":
            return "\033[90m"
    
    # Pre Select Color Function Using Background Colors
    def background_color(color):
        if color == "red" or color == "Red":
            return "\033[41m"
    
        elif color == "orange" or color == "Orange":
            return "\033[48;5;214m"
    
        elif color == "green" or color == "Green":
            return "\033[42m"
    
        elif color == "yellow" or color == "Yellow":
            return "\033[43m"
    
        elif color == "blue" or color == "Blue":
            return "\033[44m"
    
        elif color == "cyan" or color == "Cyan":
            return "\033[46m"
    
        elif color == "magenta" or color == "Magenta":
            return "\033[45m"
    
        elif color == "white" or color == "White":
            return "\033[48;2;255;255;255m"
    
        elif color == "black" or color == "Black":
            return "\033[40m"
    
        elif color == "gray" or color == "Gray":
            return "\033[100m"
    
        else:
            raise ValueError("Input Is Not A Recognized Color")
    
    
    
    # Change Text Color From Red, Green, Blue
    def text_rgb_color(red, green, blue):
        if red > 255 or green > 255 or blue > 255:
            raise ValueError("Invalid RGB Input, Must Be Between 0 and 255")
        else:
            return f"\033[38;2;{red};{green};{blue}m"
    
    # Change The Color Of The Background From Red Green And Blue
    def background_rgb_color(red, green, blue):
        if red > 255 or green > 255 or blue > 255:
            raise ValueError("Invalid RGB Input, Must Be Between 0 and 255")
        else:
            return f"\033[48;2;{red};{green};{blue}m"