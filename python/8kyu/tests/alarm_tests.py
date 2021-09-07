import unittest
import set_alarm

class TestAlarm(unittest.TestCase):
    def test_if_true_alarm(self):
        TrueAlarm = set_alarm.alarm(True, True) 
        self.assertEqual(TrueAlarm, False)
        
    def test_if_false_alarm(self):
        FalseAlarm = set_alarm.alarm(False, False)
        self.assertEqual(FalseAlarm, False)

    def test_if_still_false(self):
        StillFalse = set_alarm.alarm(False, True)
        self.assertEqual(StillFalse, False)

    def test_if_very_true(self):
        VeryTrue = set_alarm.alarm(True, False)
        self.assertEqual(VeryTrue, True)


