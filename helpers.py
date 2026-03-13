def center_window(window, width, height):

    window.update_idletasks()

    sw = window.winfo_screenwidth()
    sh = window.winfo_screenheight()

    x = int((sw - width) / 2)
    y = int((sh - height) / 2)

    window.geometry(f"{width}x{height}+{x}+{y}")
