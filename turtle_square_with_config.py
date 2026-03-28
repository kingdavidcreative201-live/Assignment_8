import configparser
import os
import turtle

def drawSquare(t, x, y, length):
    """Draws a square with the given turtle t, an upper‑left corner
    point (x, y) and a side’s length."""
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.down()
    for _ in range(4):
        t.forward(length)
        t.left(90)

def load_config():
    """Load configuration from turtle.cfg file."""
    # Get the directory where the script (.py file) is located
    base_path = os.path.dirname(os.path.abspath(__file__))
    # Combine it with the filename
    config_path = os.path.join(base_path, 'turtle_config.ini')

    cfg = configparser.ConfigParser()
    files_read = cfg.read(config_path)
    
    if not files_read:
        print(f"Error: Could not find configuration file at {config_path}. Using default settings.")
    
    return {
        'width': cfg.getint('DEFAULT', 'width', fallback=300),
        'height': cfg.getint('DEFAULT', 'height', fallback=200),
        'colormode': cfg.getint('DEFAULT','colormode', fallback=255),
        'using_IDLE': cfg.getboolean('DEFAULT','using_IDLE', fallback=True),
        'pen_color': cfg.get('DEFAULT', 'pen_color', fallback='blue'),
    }

def setup_turtle(config):
    """Initialize turtle and window with configuration."""
    window = turtle.Screen()
    window.setup(width=config['width'], height=config['height'])
    window.colormode(config['colormode'])
    
    t = turtle.Turtle()
    t.pencolor(config.get('pen_color','blue'))
    
    return t

def main():
    config = load_config()
    t = setup_turtle(config)
    
    drawSquare(t, 0, 0, 100)
    
    # Keep the window open until it is closed by the user
    turtle.done()

if __name__ == '__main__':
    main()