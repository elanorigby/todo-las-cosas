from setuptools import setup

setup(
    name="todo-las-cosas",
    version='0.2',
    py_modules=['todo'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        todo=todo:todo
    ''',
)

# copied from
# https://kushaldas.in/posts/building-command-line-tools-in-python-with-click.html