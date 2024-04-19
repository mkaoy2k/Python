from absl import app
from absl import flags

FLAGS = flags.FLAGS
"""
# Flag names are globally defined!  So in general, we need to be
# careful to pick names that are unlikely to be used by other libraries.
# If there is a conflict, we'll get an error at import time.
"""

flags.DEFINE_string('name', 'Michael Kao', 'Your name.')
flags.DEFINE_integer('age', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_boolean('debug', False, 'Produces debugging output.')
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')


def main(argv):

  if FLAGS.debug:
    print('non-flag arguments:', argv)
  print('Happy Birthday', FLAGS.name)

  if FLAGS.age is not None:
    print('You are %d years old, and your job is %s' % (FLAGS.age, FLAGS.job))


if __name__ == '__main__':
  """Example: type in the following command line
  python flagsEx.py a b c --debug -name '1 3 4 2' -age 2 -job 'stopped'

  Output:
  non-flag arguments: ['flagsEx.py', 'a', 'b', 'c']
  Happy Birthday 1 3 4 2
  You are 2 years old, and your job is stopped
  """
  app.run(main)
