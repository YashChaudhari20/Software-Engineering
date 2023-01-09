import unittest
import otp_v1

class TestOtp(unittest.TestCase):
    def test_email(self):
        self.assertIn("@",otp_v1.userEmail,"Invalid Email")
        self.assertIn(".com",otp_v1.userEmail, "Invalid Email")
    def test_otpLength(self):
        otp = otp_v1.generateOtp
        self.assertGreaterEqual(len(otp),6,"Length of otp should be greater or equal to 6")

if __name__ == '__main__':
   unittest.main()
