from textnode import TextNode, TextType


def main():
    text = TextNode("Anchor text here", TextType.LINK, "https://www.boot.dev")
    print(text)

if __name__ == "__main__":
    main()    

