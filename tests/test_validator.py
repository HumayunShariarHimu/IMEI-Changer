import unittest
from imei_research.validator import calculate_check_digit, validate_imei
class TestValidator(unittest.TestCase):
 def test_known_valid(self): self.assertTrue(validate_imei('490154203237518').valid_format_and_checksum)
 def test_wrong_check_digit(self): self.assertFalse(validate_imei('490154203237519').valid_format_and_checksum)
 def test_separators(self): self.assertTrue(validate_imei('4901-5420-3237-518').valid_format_and_checksum)
 def test_wrong_length(self): self.assertFalse(validate_imei('49015420323751').valid_format_and_checksum)
 def test_check_digit(self): self.assertEqual(calculate_check_digit('49015420323751'),8)
if __name__=='__main__': unittest.main()
