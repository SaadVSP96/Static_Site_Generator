from textnode import TextNode   # type: ignore


def main():
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(node)


main()