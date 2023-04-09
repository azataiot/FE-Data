raw_csv_columns = ['symbol', 'name', 'market']
profile_csv_columns = raw_csv_columns + [
    'sector',
    'industry',
    'country',
    'start_date',
    'city',
    'zip',
    'state',
    'phone',
    'website',
    'address',
    'long_business_summary',
    'full_time_employees',
    'audit_risk',
    'board_risk',
    'compensation_risk',
    'share_holder_rights_risk',
    'overall_risk',
    'governance_epoch_date',
    'compensation_as_of_epoch_date',
]
extra_csv_columns = profile_csv_columns
default_csv_columns = raw_csv_columns + [
    'sector',
    'industry',
    'country',
    'start_date',
]
