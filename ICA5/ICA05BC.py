ó
¤ÌVc           @   sd   d  Z  d d l Z d d l Z d d d d d g Z d   Z d	   Z d
 Z g  Z g  Z d   Z	 d S(   sd   

A short program to evaluate execution times of algoritmhs

Written by Martin Venaas 23.feb.2016


iÿÿÿÿNt   Martins   Tor Oles   Per-ottot   Tomast   Andreic         C   s%   x |  D] } | | k r t  Sq Wt S(   N(   t   Truet   False(   t   haystackt   needlet   item(    (    s+   /Users/martinvenaas/Desktop/is105/ICA05B.pyt   search_fast   s    c         C   s0   t  } x# |  D] } | | k r t } q q W| S(   N(   R   R   (   R   R   t   return_valueR   (    (    s+   /Users/martinvenaas/Desktop/is105/ICA05B.pyt   search_slow   s
    i   c         C   s   x t  |   D]z } t j t j t t d   } | j d  } t j |  t j t j t	 t d   } | j d  } t
 j |  q Wd  S(   NR    i@B (   t   ranget   timeitt   Timert	   functoolst   partialR   t   listt   testresultsFastt   appendR
   t   testresultsSlow(   t   numberOfLoopst   it   tt
   fastResultt
   slowResult(    (    s+   /Users/martinvenaas/Desktop/is105/ICA05B.pyt	   timeTests.   s    (
   t   __doc__R   R   R   R   R
   R   R   R   R   (    (    (    s+   /Users/martinvenaas/Desktop/is105/ICA05B.pyt   <module>   s   		