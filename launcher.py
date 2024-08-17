import threading

import gui  # Assuming your Tkinter code is in gui.py
from app import app


def start_flask_server():
    app.run(debug=False, use_reloader=False)


def start_tkinter_gui():
    gui.main()  # Assuming you have a main function in your gui.py to initialize the Tkinter app


if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask_server)
    flask_thread.start()

    # Start the Tkinter GUI
    start_tkinter_gui()
