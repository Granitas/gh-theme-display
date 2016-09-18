from distutils.core import setup

setup(
    name='githeme',
    version='0.1',
    packages=['githeme'],
    url='http://github.com/granitas/github_theme_viewer',
    license='GPLv3',
    author='granitas',
    author_email='bernardas.alisauskas@gmail.com',
    description='View generator for themes stored on github',
    entry_points="""
            [console_scripts]
            githeme=githeme.main:cli
        """,
    requires=['click', 'parsel', 'requests'],
    include_package_data=True,
)
