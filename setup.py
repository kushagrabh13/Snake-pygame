import cx_Freeze

executables = [cx_Freeze.Executable("snake.py")]

cx_Freeze.setup(
    name = "Snake - Developed By Kushagra Bhatnagar",
    options={"build_exe":{"packages":["pygame"],"include_files":["apple.png","snakeHead.png","snakeBody.png","icon.png","comic.ttf","comicbd.ttf"]}},
    description = "Snake - Developed By Kushagra Bhatnagar",
    executables = executables
    )
