OK_FORMAT = True

test = {
  'name': 'Question 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Check to see if the mean HR changes when using imputation. 
          >>> bool(HeartRateMean == 75.13268404820141)
          True
          >>> bool(HeartRateMean == fullTableHRMean)
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