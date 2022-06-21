def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("Text is too long")

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*")
banner_text("Health Points")
banner_text("*")
