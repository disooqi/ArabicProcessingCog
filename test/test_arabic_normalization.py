#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
created on 2015 Apr 15
by disooqi
'''
from unittest import TestCase
from normalization import Arabic_normalization

__author__ = 'Mohamed_Eldesouki'


class TestArabic_normalization(TestCase):
    # a test method that will assert throwing an exception, if the discriminant of a quadratic equation is negative.
    # def test_negative_discr(self):
    #     s = Solver
    #     self.assertRaises(Exception,s.demo,2,1,2)

    def test_normalize_sentence(self):
        ## multiple space into one space
        self.assertEqual(Arabic_normalization.normalize_sentence(u'مدحت    حسن'), u'مدحت حسن')
        ## isolate TAA_Marbouta from the next word and replace it with HEH
        self.assertEqual(Arabic_normalization.normalize_sentence(u'مدرسةالمسلةالاعداديةبنات'), u'مدرسه المسله الاعداديه بنات')
        self.assertEqual(Arabic_normalization.normalize_sentence(u''), u'')
        self.assertEqual(Arabic_normalization.normalize_sentence(u'  '), u'')
        self.assertEqual(Arabic_normalization.normalize_sentence(u'أ'), u'ا')
        self.assertEqual(Arabic_normalization.normalize_sentence(u'وقال: لقد هرمنا من أجل هذه اللحظة،'), u'وقال لقد هرمنا من اجل هذه اللحظه')

        #self.fail()

    def test_normalize_token(self):
        self.assertEqual(Arabic_normalization.normalize_token(u'مدرسة'), u'مدرسه')
        self.assertEqual(Arabic_normalization.normalize_token(u'أحمد'), u'احمد')
        self.assertEqual(Arabic_normalization.normalize_token(u'إبراهيم'), u'ابراهيم')
        self.assertEqual(Arabic_normalization.normalize_token(u'آخرة'), u'اخره')
        self.assertEqual(Arabic_normalization.normalize_token(u'على'), u'علي')
        self.assertEqual(Arabic_normalization.normalize_token(u''), u'')
        self.assertEqual(Arabic_normalization.normalize_token(u'محمــــد'), u'محمد')
        self.assertEqual(Arabic_normalization.normalize_token(u'  '), u'')
        self.assertEqual(Arabic_normalization.normalize_token(u'ة'), u'ه')
        #exception if there is a space

# if __name__ == '__main__':
#     unittest.main()

