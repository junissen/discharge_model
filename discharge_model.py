#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 18:52:04 2017

@author: julianissen
"""

#import numpy as np
from scipy.optimize import fsolve

class discharge_model(): 
    
    def __init__(self, both_dp, ax, xlim, ylim):
        
        #Input parameters from Carlson2009
        self.benthic_change = -2.30 
        self.planktonic_change = -0.8
        self.combined_change = self.benthic_change + self.planktonic_change
        
        self.dp = both_dp
        
        #Benthic parameters
        self.benthic_fo = 0.476
        self.benthic_do = 1.7
        self.benthic_fp1 = 0
        self.benthic_fp2 = 0.0856
        self.benthic_fi1 = 0
        
        #Planktonic parameters
        self.planktonic_fo = 0.159
        self.planktonic_do = 1.7
        self.planktonic_fp1 = 0.1157
        self.planktonic_fp2 = 0.03
        self.planktonic_fi1 = 0.0164
    
        #Variable LIS d18O from Ferguson2015
        self.di = -12.5
        self.di_end = -25.5
        self.di_change = -0.5
        
        self.ax = ax
        self.xlim = xlim
        self.ylim = ylim
        
        self.dp_lit = -7.7
        self.dp_source = -6.3
        
        self.d18o = r'$\delta^{18}\!O$'
        
    def discharge_benth_calc(self):
        
        ax = self.ax
        di = self.di
        di_array = []
        dis_array = []
        
        
        
        if -7.8 < self.dp < -7.6: 
            while di >= self.di_end:
                mr_1 = ((self.benthic_fo * self.benthic_do) + (self.benthic_fp1 * self.dp) + (self.benthic_fi1 * di))/(self.benthic_fo + self.benthic_fp1 + self.benthic_fi1)
                benthic_dis_func = lambda benthic_fi2 : (((self.benthic_fo * self.benthic_do) + (self.benthic_fp2 * self.dp) + (benthic_fi2 * di))/(self.benthic_fo + self.benthic_fp2 + benthic_fi2)) - mr_1 - self.benthic_change
                    
                benthic_fi2_initial_guess = 0
                benthic_fi2_calc = fsolve(benthic_dis_func, benthic_fi2_initial_guess)                                      
                dis_array.append(benthic_fi2_calc)
                di_array.append(di)
                 
                if di == -25.0:
                    print "Benthic -25.0 discharge using -7.7: " + str(benthic_fi2_calc)
                elif di == -25.5:
                    print "Benthic -25.5 discharge using -7.7: " + str(benthic_fi2_calc)
                elif di == -12.5:
                    print "Benthic -12.5 discharge using -7.7: " + str(benthic_fi2_calc)
                
                di = di + self.di_change
                
            
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_benth = ax.plot(dis_array, di_array, color = 'black', label = self.d18o + " precip Aharon2006", linewidth = 1)
            
            
        elif -6.4 < self.dp < -6.2: 
            while di >= self.di_end:
                mr_1 = ((self.benthic_fo * self.benthic_do) + (self.benthic_fp1 * self.dp) + (self.benthic_fi1 * di))/(self.benthic_fo + self.benthic_fp1 + self.benthic_fi1)
                benthic_dis_func = lambda benthic_fi2 : (((self.benthic_fo * self.benthic_do) + (self.benthic_fp2 * self.dp) + (benthic_fi2 * di))/(self.benthic_fo + self.benthic_fp2 + benthic_fi2)) - mr_1 - self.benthic_change
                 
                benthic_fi2_initial_guess = 0
                benthic_fi2_calc = fsolve(benthic_dis_func, benthic_fi2_initial_guess)                                      
                dis_array.append(benthic_fi2_calc)
                di_array.append(di)
                
                if di == -25.5:
                    print "Benthic -25.5 discharge using -6.3: " + str(benthic_fi2_calc)
                elif di == -12.5:
                    print "Benthic -12.5 discharge using -6.3: " + str(benthic_fi2_calc)
                    
                di = di + self.di_change
            
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_benth = ax.plot(dis_array, di_array, color = 'dimgray', linewidth = 1, label = self.d18o + " precip SVC")
            
        else:
            while di >= self.di_end:
                mr_1 = ((self.benthic_fo * self.benthic_do) + (self.benthic_fp1 * self.dp) + (self.benthic_fi1 * di))/(self.benthic_fo + self.benthic_fp1 + self.benthic_fi1)
                benthic_dis_func = lambda benthic_fi2 : (((self.benthic_fo * self.benthic_do) + (self.benthic_fp2 * self.dp) + (benthic_fi2 * di))/(self.benthic_fo + self.benthic_fp2 + benthic_fi2)) - mr_1 - self.benthic_change
                 
                benthic_fi2_initial_guess = 0
                benthic_fi2_calc = fsolve(benthic_dis_func, benthic_fi2_initial_guess)                                      
                dis_array.append(benthic_fi2_calc)
                di_array.append(di)
                di = di + self.di_change
            
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_benth = ax.plot(dis_array, di_array, 'r-', linewidth = 1)
        
        
        return discharge_benth
    
    
    def discharge_planktonic_calc(self):
    
        ax = self.ax
        di = self.di
        di_array = []
        dis_array = []
        
        
        if -7.8 < self.dp < -7.6: 
        
            while di >= self.di_end:
                
                mr_1 = (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp1 * self.dp) + (self.planktonic_fi1 * di)) /
                        (self.planktonic_fo + self.planktonic_fp1 + self.planktonic_fi1))
                
                planktonic_dis_func = lambda planktonic_fi2 : (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp2 * self.dp) + (planktonic_fi2 * di)) /
                        (self.planktonic_fo + self.planktonic_fp2 + planktonic_fi2)) - mr_1 - self.planktonic_change
                
                planktonic_fi2_initial_guess = 0
                planktonic_fi2_calc = fsolve(planktonic_dis_func, planktonic_fi2_initial_guess)                                      
                dis_array.append(planktonic_fi2_calc)
                di_array.append(di)
                
                if di == -25.0:
                    print "Planktonic -25.0 discharge using -7.7: " + str(planktonic_fi2_calc)
                elif di == -25.5:
                    print "Planktonic -25.5 discharge using -7.7: " + str(planktonic_fi2_calc)                  
                elif di == -12.5:
                    print "Planktonic -12.5 discharge using -7.7: " + str(planktonic_fi2_calc)
                    
                di = di + self.di_change
                
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_planktonic = ax.plot(dis_array, di_array, 'black', label = self.d18o + " precip Aharon2006", linewidth = 1)
            
        elif -6.4 < self.dp < -6.2:
            
            while di >= self.di_end:
                
                mr_1 = (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp1 * self.dp) + (self.planktonic_fi1 * di)) /
                        (self.planktonic_fo + self.planktonic_fp1 + self.planktonic_fi1))
                
                planktonic_dis_func = lambda planktonic_fi2 : (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp2 * self.dp) + (planktonic_fi2 * di)) /
                        (self.planktonic_fo + self.planktonic_fp2 + planktonic_fi2)) - mr_1 - self.planktonic_change
                
                planktonic_fi2_initial_guess = 0
                planktonic_fi2_calc = fsolve(planktonic_dis_func, planktonic_fi2_initial_guess)                                      
                dis_array.append(planktonic_fi2_calc)
                di_array.append(di)
                
                if di == -25.5:
                    print "Planktonic -25.5 discharge using -6.3: " + str(planktonic_fi2_calc)
                     
                elif di == -12.5:
                    print "Planktonic -12.5 discharge using -6.3: " + str(planktonic_fi2_calc)
                    
                di = di + self.di_change
                
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_planktonic = ax.plot(dis_array, di_array, 'dimgray', label = self.d18o + " precip SVC", linewidth = 1)
        
        else: 
        
            while di >= self.di_end:
              
                mr_1 = (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp1 * self.dp) + (self.planktonic_fi1 * di)) /
                        (self.planktonic_fo + self.planktonic_fp1 + self.planktonic_fi1))
                
                planktonic_dis_func = lambda planktonic_fi2 : (((self.planktonic_fo * self.planktonic_do) + (self.planktonic_fp2 * self.dp) + (planktonic_fi2 * di)) /
                        (self.planktonic_fo + self.planktonic_fp2 + planktonic_fi2)) - mr_1 - self.planktonic_change
                
                planktonic_fi2_initial_guess = 0
                planktonic_fi2_calc = fsolve(planktonic_dis_func, planktonic_fi2_initial_guess)                                      
                dis_array.append(planktonic_fi2_calc)
                di_array.append(di)
                di = di + self.di_change
                
            ax.set_xlim(self.xlim)
            ax.set_ylim(self.ylim)
            discharge_planktonic = ax.plot(dis_array, di_array, 'b-', linewidth = 1)
        
        return discharge_planktonic

            
            
        
        
        
        
        
        
        
        
        