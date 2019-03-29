import sys, getopt
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


def main():
    input_file = sys.argv[1]
    output_file = input_file.strip().split('.')[0]
    file_type = input_file.strip().split('.')[1]

    file = open(input_file, 'r')

    if file.mode == 'r':
        content = file.read()

        minified_content = removeSpace(
            removeNewLine(
                removeWhitespace(
                    removeComment(content)
                )
            )
        )

        new_file = open(output_file + '.min.' + file_type, 'w')
        new_file.write(minified_content)
        new_file.close()

    if sys.argv[1] == 'help':
        print('Help menu')

if __name__ == '__main__':
    main()
