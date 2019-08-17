
1) start console on which ardXX.py available
2) on console type "export PATH=.:PATH" (chrome web driver stuff for selenium)
3) Start ardXX.py, "python ardXX.py"
4) Wait for data.json output file.
5) Create a local server where this data.json file available.
For this type on console 
python -m SimpleHTTPServer 8080
6) Open chrome web browser.
7) Make sure you have enabled CORS (cross origin resource sharing)
if there's a problem with CORS just install CORS plugin from chrome market.
8) Type "localhost:8080" on browser search bar.
9) select geochart.html file.
10) You should see POLAND map with airports and some informations based on METAR report for aviation especially Temperature.


Thank you.
