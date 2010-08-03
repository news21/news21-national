"""
Constants for the multimedia app
"""

LICENSE_DEFAULT = 'http://news21.com'
LICENSE_CHOICES = (
      ('http://news21.com',                                   'All Rights Reserved'),
      ('http://creativecommons.org/licenses/by/2.0/',         'CC Attribution'),
      ('http://creativecommons.org/licenses/by-nd/2.0/',      'CC Attribution-NoDerivs'),
      ('http://creativecommons.org/licenses/by-nc-nd/2.0/',   'CC Attribution-NonCommercial-NoDerivs'),
      ('http://creativecommons.org/licenses/by-nc/2.0/',      'CC Attribution-NonCommercial'),
      ('http://creativecommons.org/licenses/by-nc-sa/2.0/',   'CC Attribution-NonCommercial-ShareAlike'),
      ('http://creativecommons.org/licenses/by-sa/2.0/',      'CC Attribution-ShareAlike'),
)


STATUS_DEFAULT = 'Pending Approval'
STATUS_CHOICES = (
      ('Pending Approval', 'Pending Approval'),
	  ('Rejected', 'Rejected'),
	  ('Approved', 'Approved'),
)

STAGE_DEFAULT = ''
STAGE_CHOICES = (
	('Copy Edit Complete', 'Copy Edit Complete'),
	('1st Edit Complete', '1st Edit Complete'),
	('2nd Edit Complete', '2nd Edit Complete'),
)