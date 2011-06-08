#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgitb; cgitb.enable()
import random

print "Content-Type: text/html; charset=utf-8\n"

value=[ 'user1', 'user2', 'user3', 'user4', 'user5', 'user6' ]

print """
        <HTML><HEAD><TITLE>Random</TITLE></HEAD>
        <BODY vlink="black">

        <br/> <br/> <br/> <br/>
        <br/> <br/> <br/> <br/>
        <div align="center">
        
                <H1>%s</H1>
                <A HREF="">reload</A>
        </div>
        </BODY>
        </HTML>

""" % ( value[ random.randint( 0, (len(value)-1) ) ] )

