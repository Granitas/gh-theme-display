import logging
import webbrowser

import click
from ghthemedisplay.downloader import find_themes
from ghthemedisplay.generator import save_themes


@click.command()
@click.argument('url')
@click.option('--drop_without_images', help='drop themes without items', is_flag=True)
@click.option('--debug', help='print debug messages', is_flag=True)
@click.option('--open', '-o', 'open_in_browser', help='open in browser when done', is_flag=True)
def cli(url, drop_without_images, debug, open_in_browser):
    setup_loggers(debug)
    themes = list(find_themes(url, allow_no_images=not drop_without_images))
    output_loc = save_themes(themes)
    if open_in_browser:
        logging.info('Opening in browser')
        webbrowser.open(output_loc)


def setup_loggers(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    downloader = logging.getLogger('downloader')
    generator = logging.getLogger('generator')
    for log in [downloader, generator]:
        log.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        log.addHandler(ch)


if __name__ == '__main__':
    cli()

