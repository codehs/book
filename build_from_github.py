# Import the pyyaml library
import yaml
import sys
import os

HEADER_HTML = "static/header.html"


def process_file(config_filename, output_filename):
    """This processe the filename to generate a html page."""

    config_dir = os.path.dirname(config_filename)

    with open(output_filename, 'w') as outfile:

        # Write out the HTML header
        with open(HEADER_HTML, 'r') as f:
            outfile.write(f.read())

        with open(config_filename, 'r') as f:
            # Change directory to the config file
            os.chdir(config_dir)
            # Now change to the directory of files
            # This way we can just access the files with the file names
            os.chdir('../files')

            book = yaml.load(f)
            for entry in book:
                chapter_file = entry['file']
                print chapter_file
                with open(chapter_file) as infile:
                    div = "<div id='%s' class='mkdown-text'>\n" % entry['name']
                    outfile.write(div)
                    outfile.write(infile.read())
                    outfile.write("</div>\n")

        outfile.write("</html>")


def start():
    if not len(sys.argv) == 3:
        print "Expecting two arguments"
        print "python build_html.py <configfile> <outputfile>"
        print "Example:"
        print "python build_html.py introcs/setup/config.yaml \
        introcs/build/book.html"
        sys.exit(1)

    process_file(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    start()
