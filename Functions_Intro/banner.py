"""Banner mechanism to illustrate a cool way of integrating the text around ***"""


def banner_text(text=" ", screen_width=80):
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Hello")
banner_text("World")
banner_text("*")
