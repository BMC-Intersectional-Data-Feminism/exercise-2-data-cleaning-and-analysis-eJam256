OK_FORMAT = True

test = {
  'name': 'Question 6',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check minimum and maximum steps 
          >>> bool(minSteps == 0.9101380609604088)
          True
          >>> bool(maxSteps == 62486.690753464914)
          True
          >>> bool(meanSteps ==  6985.685884992229)
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}