# Stress-Testing ( Flight booking for 400+ users booking tickests simultaneouslty for the total of more than 22k Bookings in 2 mins )

##Please dont use this for DDos or anything like that ##

Requiremts: Vs Code with python with v3.12.10 or later


Follow these steps to make it work for you
1. Have both py files in you base folder.
2. In terminal 1 run this - uvicorn main:app --reload
   This will start the uvicorn in your pc.
3. In terminal 2 run this - locust -f locustfile.py --host http://localhost:8000 -u 1000 -r 100 --run-time 2m --headless
   This will run the test with 400 users booking flight simultaneously for 2 minutes. 

Result: 
Response time percentiles (approximated)
Type     Name      50%    66%    75%    80%    90%  
  95%    98%    99%  99.9% 99.99%   100% # reqs     
--------||--------|------|------|------|------|------|------|------|------|------|------|------
POST     /api/book       21     38     71     99    
160    220    600   2200   2500   2600   2600  22054--------||--------|------|------|------|------|------|------|------|------|------|------|------
         Aggregated       21     38     71     99   
 160    220    600   2200   2500   2600   2600  22054

Explaination of result:
Metric | Value
Total requests | 22 054
Failures | 0 (0.00%)
Average latency | 93 ms
Minimum latency | 3 ms
Maximum latency | 2 615 ms
Median (50th pct.) | 21 ms
90th percentile | 160 ms
99th percentile | 2 600 ms
Requests/sec | ~185

