pytest -s -v -m "sanity" --html=Reports\report.html  testCases/  --browser chrome

pytest -s -v -m "sanity" --html=Reports\report1.html  testCases/  --browser firefox

rem chrome

rem pytest -s -v --html=Reports\report.html  testCases/test_addCustomer.py --browser chrome
rem pytest -s -v -m "sanity and regression" --html=Reports\report.html  testCases/  --browser chrome
rem pytest -s -v -m "sanity or regression" --html=Reports\report.html  testCases/  --browser chrome
rem pytest -s -v -m "sanity" --html=Reports\report.html  testCases/  --browser chrome
rem pytest -s -v -m "regression" --html=Reports\report.html  testCases/  --browser chrome


rem firefox

rem pytest -s -v --html=Reports\report.html  testCases/test_addCustomer.py --browser firefox
rem pytest -s -v -m "sanity and regression" --html=Reports\report.html  testCases/  --browser firefox
rem pytest -s -v -m "sanity or regression" --html=Reports\report.html  testCases/  --browser firefox
rem pytest -s -v -m "sanity" --html=Reports\report.html  testCases/  --browser firefox
rem pytest -s -v -m "regression" --html=Reports\report.html  testCases/  --browser firefox

rem edge is default browser

rem pytest -s -v --html=Reports\report.html  testCases/test_addCustomer.py 
rem pytest -s -v -m "sanity and regression" --html=Reports\report.html  testCases/  
rem pytest -s -v -m "sanity or regression" --html=Reports\report.html  testCases/ 
rem pytest -s -v -m "sanity" --html=Reports\report.html  testCases/  
rem pytest -s -v -m "regression" --html=Reports\report.html  testCases/  