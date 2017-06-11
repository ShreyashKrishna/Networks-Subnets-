# Networks-Subnets
Fallowing Internetwrok-
 It has 5 subnets and each host (H1 through H9) is attached to one of these
subnets.
 The MTU of each subnet has been given.
 It has 5 routers (S1 through S5).

Input
1 Source Ip address
2 Msg 
3 Desitination Ip address

Program
1 Compute the subnet number corresponding to the source ip address
2 Compute the Msg length and compare it with the MTU of the above subnet
3 If Msg length is smaller than MTU, make a ip like packet as follows:
---------------------------
source ip address
--------------------
destination ip address
------------------
sequence number
--------------------
off set
--------------------
Msg
----------------------
4 If Msg length is larger than MTU, make appropriate fragmented ip-packets
------------------------
source ip address
--------------------
destination ip address
---------------------
sequence number
--------------------
off set
--------------------
Fragmented Msg with length
as per the MTU of the current subnet
--------------------------------------
