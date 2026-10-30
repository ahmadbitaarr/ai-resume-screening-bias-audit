import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from experiment import load_cases, validate, prompt, extract_json, weakened_resume, heuristic_screen

class ExperimentTests(unittest.TestCase):
    def test_matched_pairs(self):
        self.assertEqual(len(validate(load_cases())), 11)
    def test_no_name_leakage(self):
        for r in load_cases():
            self.assertNotIn(r['candidate_name'], r['anonymized_resume'])
    def test_parse(self):
        self.assertEqual(extract_json('{"score":75,"recommendation":"Yes","reason":"skills"}')['score'],75)
        with self.assertRaises(ValueError):
            extract_json('{"score":120,"recommendation":"Yes"}')
    def test_stress(self):
        row=load_cases()[0]
        a=heuristic_screen(row['job_description'],row['anonymized_resume'])
        b=heuristic_screen(row['job_description'],weakened_resume(row['anonymized_resume']))
        self.assertGreaterEqual(a['score'],b['score'])
    def test_prompt(self):
        self.assertIn('JOB DESCRIPTION',prompt('test job','test resume'))

if __name__ == '__main__': unittest.main()
