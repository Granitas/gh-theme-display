from distutils.core import setup

setup(
    name='ghthemedisplay',
    version='0.1',
    packages=['ghthemedisplay'],
    url='http://github.com/granitas/github_theme_viewer',
    license='GPLv3',
    author='granitas',
    author_email='bernardas.alisauskas@gmail.com',
    description='View generator for themes stored on github',
    entry_points="""
            [console_scripts]
            gh-theme-display=ghthemedisplay.main:cli
        """,
    requires=['click', 'parsel', 'requests'],
    include_package_data=True,
)
