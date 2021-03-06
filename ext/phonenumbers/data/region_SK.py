"""Auto-generated file, do not edit by hand. SK metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SK = PhoneMetadata(id='SK', country_code=421, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='(?:[2-68]\\d{5,8}|9\\d{6,8})', possible_number_pattern='\\d{6,9}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='2(?:16\\d{3,4}|\\d{8})|[3-5](?:[1-8]16\\d{2,3}|\\d{8})', possible_number_pattern='\\d{6,9}', example_number='212345678'),
    mobile=PhoneNumberDesc(national_number_pattern='9(?:0(?:[1-8]\\d|9[1-9])|(?:1[0-24-9]|4[0489]|50)\\d)\\d{5}', possible_number_pattern='\\d{9}', example_number='912123456'),
    toll_free=PhoneNumberDesc(national_number_pattern='800\\d{6}', possible_number_pattern='\\d{9}', example_number='800123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:[78]\\d{7}|00\\d{6})', possible_number_pattern='\\d{9}', example_number='900123456'),
    shared_cost=PhoneNumberDesc(national_number_pattern='8[5-9]\\d{7}', possible_number_pattern='\\d{9}', example_number='850123456'),
    personal_number=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voip=PhoneNumberDesc(national_number_pattern='6(?:02|5[0-4]|9[0-6])\\d{6}', possible_number_pattern='\\d{9}', example_number='690123456'),
    pager=PhoneNumberDesc(national_number_pattern='9090\\d{3}', possible_number_pattern='\\d{7}', example_number='9090123'),
    uan=PhoneNumberDesc(national_number_pattern='96\\d{7}', possible_number_pattern='\\d{9}', example_number='961234567'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='(?:602|8(?:00|[5-9]\\d)|9(?:00|[78]\\d))\\d{6}|9090\\d{3}', possible_number_pattern='\\d{7,9}', example_number='800123456'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(2)(16)(\\d{3,4})', format='\\1 \\2 \\3', leading_digits_pattern=['216'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([3-5]\\d)(16)(\\d{2,3})', format='\\1 \\2 \\3', leading_digits_pattern=['[3-5]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(2)(\\d{3})(\\d{3})(\\d{2})', format='\\1/\\2 \\3 \\4', leading_digits_pattern=['2'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([3-5]\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1/\\2 \\3 \\4', leading_digits_pattern=['[3-5]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([689]\\d{2})(\\d{3})(\\d{3})', format='\\1 \\2 \\3', leading_digits_pattern=['[689]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9090)(\\d{3})', format='\\1 \\2', leading_digits_pattern=['9090'], national_prefix_formatting_rule='0\\1')],
    mobile_number_portable_region=True)
