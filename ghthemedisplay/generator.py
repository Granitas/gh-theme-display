import logging
import os

from jinja2 import Environment, PackageLoader

log = logging.getLogger('generator')


def save_themes(themes):
    """
    generates theme output file using theme template
    :returns file location
    """
    env = Environment(loader=PackageLoader('githeme', 'templates'))
    template = env.get_template('theme.html')
    loc = os.path.join(os.getcwd(), 'output.html')
    with open(loc, 'w') as f:
        log.info('output: {}'.format(loc))
        f.write(template.render(themes=themes))
    return loc
