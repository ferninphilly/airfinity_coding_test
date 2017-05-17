#!/usr/bin/env python3
import airfinity_coding_answer as aca
import unittest

class TestAdd(unittest.TestCase):
    
    def test_read_csv(self):
        self.assertIsInstance(aca.list_of_files(), list)
    
    def test_found_csv(self):    
        self.assertGreater(len(aca.list_of_files()),0)

    def test_tuple_return(self):
        self.assertIsInstance(aca.create_dataframes(aca.list_of_files()),tuple)
    
    def test_sanitized_df(self):
        frame_tup = aca.create_dataframes(aca.list_of_files())
        self.assertIsNotNone(aca.matchall_columns(frame_tup[0], frame_tup[1]))
    
    def test_improve_date(self):
        better = aca.improve_date('2/2/17')
        self.assertEqual(len(better), 8)
        
if __name__ == '__main__':
    unittest.main()
