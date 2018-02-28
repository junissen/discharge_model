#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 17:10:14 2017

@author: julianissen
"""

import discharge_model


class discharge_model_vardp:
    
    def __init__(self, ax, xlim, ylim):
        
        self.ax = ax
        self.xlim = xlim
        self.ylim = ylim
        
        self.dp_start = -9.0
        self.dp_end = -5.0
        self.dp_change = 0.2
        
        
    def discharge_benthic_dp(self):
        
        dp = self.dp_start
        
        while dp <= self.dp_end:
            
            wb = discharge_model.discharge_model(dp, self.ax, self.xlim, self.ylim)
            
            wb.discharge_benth_calc()
            
            dp = dp + self.dp_change
            
            
    def discharge_planktonic_dp(self):
        
        dp = self.dp_start
        
        while dp <= self.dp_end:
            
            wb = discharge_model.discharge_model(dp, self.ax, self.xlim, self.ylim)
            
            wb.discharge_planktonic_calc()
            
            dp = dp + self.dp_change
            

        