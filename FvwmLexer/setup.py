from setuptools import setup, find_packages

setup (
  name='fvwmlexer',
  packages=find_packages(),
  entry_points =
  """
  [pygments.lexers]
  fvwmlexer = fvwmlexer.lexer:FvwmLexer
  """,
)
