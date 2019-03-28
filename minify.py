import re


def removeNewLine(content):
    """Remove new line."""
    return content.replace('\n', '')


def removeComment(content):
    """Remove code comments."""
    content = re.sub(re.compile('/\*.*?\*/', re.DOTALL), '', content)
    content = re.sub(re.compile('//.*?\n'), '', content)
    return content


def removeWhitespace(content):
    """Remove leading and ending whitespace."""
    return content.strip()


def removeSpace(content):
    """Remove space character."""
    return content.replace(' ','')


file = open('style.css', 'r')

if file.mode == 'r':
    content = file.read()

    minified_content = removeSpace(
        removeNewLine(
            removeWhitespace(
                removeComment(content)
            )
        )
    )

    print(minified_contents)
