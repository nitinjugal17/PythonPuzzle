#
# Author : Jugal Kishore <jugalk1993@gmail.com>
# Homepage : https://nitinjugal17.github.io/
# License : BSD http://en.wikipedia.org/wiki/BSD_license
# Copyright (c) 2023, Jugal Kishore
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met: 
# 
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer. 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution. 
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Purpose : This script aims to get armstrong numbers within given series.
# Usage : arm, ntarm = armstrong_check(10000000)
# armstrong number 
'''
An Armstrong number is one whose sum of digits raised to the power three equals the number itself. 
371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371

'''

def armstrong_check(rangeint):

     
    listval = []
    listvalnot = []
    for i in range(0, rangeint + 1):
        chkarmstrng = 0
        # count number from converting int to strings
        strlen = len(str(i))
        strint = str(i)
        # print(strlen)
        for x in range(0, strlen):
            
            # convert to int
            convintstr = ''
            convintstr = strint[x]
            # print(convintstr)
            convint = int(convintstr)
            # print(strlen)
            chkarmstrng += convint ** strlen
        # print(chkarmstrng, i)
        
        if chkarmstrng == i:
            print(' {} : Is Armstrong : True'.format(i))
            listval.append(i)
        else:
            #print(' {} : False Armstrong '.format(i))
            listvalnot.append(i)

    return listval, listvalnot

arm, ntarm = armstrong_check(10000000)

print(len(arm), arm)
# print(ntarm)