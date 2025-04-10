OK_FORMAT = True

test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check minimum and maximum blood oxygen level  
          >>> bool(minBloodO2 == 90.79120814564097)
          True
          >>> bool(maxBloodO2 == 100.0)
          True
          >>> bool(meanBloodO2 == 97.84158102099076)
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